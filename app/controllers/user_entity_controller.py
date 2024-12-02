from flask import request, Response, Blueprint, jsonify

from app.models.response_data import ResponseData
from app.service.user_entity_services import UserEntityService
from app.utils.utils import UtilsJWT

user_route: Blueprint = Blueprint("user", __name__, url_prefix="/user")

class UserEntityController:

    @staticmethod
    @user_route.route(rule="/", methods=["GET"])
    @UtilsJWT.token_required(roles=["admin", "user"])
    def getAll() -> tuple[Response, int]:
        listData:list[dict] = UserEntityService.getALl()
        response_data:ResponseData = ResponseData(
            status="OK",
            status_code=200,
            data=listData
        )

        return jsonify(response_data.getJson()), 200

    @staticmethod
    @user_route.route(rule="/", methods=["POST"])
    @UtilsJWT.token_required(roles=["admin"])
    def create() -> tuple[Response, int]:
        request_data:dict = request.get_json()

        response_data:ResponseData = ResponseData(
            status="CREATED",
            status_code=201,
            data=UserEntityService.create(request_data)
        )

        return jsonify(response_data.getJson()), 201