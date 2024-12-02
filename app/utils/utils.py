from datetime import datetime, timedelta
from functools import wraps

import jwt
import json

from app.exceptions.exception_token import ExceptionExpiredSignatureError, ExceptionInvalidTokenError, \
    ExceptionRoleNotAllowedError, ExceptionRoleNotPermittedError
from app.models.user_entity import UserEntity
from flask import Request, request

from app.validators.validators_jwt import ValidatorsJWT

SECRET:str = "secret"

class UtilsJWT:

    @staticmethod
    def getToken(requestData: Request) -> str:
        return requestData.headers["Authorization"].split(" ")[1]

    @staticmethod
    def generatedToken(user: UserEntity) -> str:
        payload = {
            'exp': int((datetime.now() + timedelta(minutes=10)).timestamp()),
            'iat': int(datetime.now().timestamp()),
            'sub': json.dumps(user.getJSON())
        }

        token = jwt.encode(payload=payload, key=SECRET, algorithm='HS256')
        return token

    @staticmethod
    def validateToken(requestData: Request) -> dict:

        ValidatorsJWT.validateHeaderAuthorization(request=requestData)

        token:str = UtilsJWT.getToken(requestData=requestData)

        ValidatorsJWT.validateToken(token=token)

        try:
            decoded_token = jwt.decode(token, SECRET, algorithms=['HS256'])
            return decoded_token
        except jwt.ExpiredSignatureError as e:
            raise ExceptionExpiredSignatureError(e)
        except jwt.InvalidTokenError as e:
            raise ExceptionInvalidTokenError(e)

    @staticmethod
    def token_required(roles=None):
        roles: list = ValidatorsJWT.ValidateListRolesOnTokenRequired(roles=roles)
        def wrapper(function):
            @wraps(function)
            def decorated(*args, **kwargs):
                try:
                    decoded_token = UtilsJWT.validateToken(request)
                    request.user = json.loads(decoded_token['sub'])
                    user_role = request.user.get('role')

                    ValidatorsJWT.validateRolesPermitted(listRoles=roles, role=user_role)

                except Exception as e:
                    raise ExceptionRoleNotPermittedError(e)

                return function(*args, **kwargs)

            return decorated
        return wrapper
