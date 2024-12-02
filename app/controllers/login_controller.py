from flask import request, Response, Blueprint, jsonify

from app.models.response_data import ResponseData
from app.models.user_entity import UserEntity
from app.service.user_entity_services import UserEntityService
from app.utils.utils import UtilsJWT

login_route: Blueprint = Blueprint("/login/", __name__, url_prefix="/login/")

class LogingController:

    @staticmethod
    @login_route.route(rule="/", methods=["POST"])
    def login() -> tuple[Response, int]:
        request_data:dict = request.get_json()
        user_authenticated: UserEntity = UserEntityService.authenticated(request=request_data)

        response_data:ResponseData = ResponseData(
            status="OK",
            status_code=200,
            data=UtilsJWT.generatedToken(user=user_authenticated)
        )

        return jsonify(response_data.getJSON()), 200