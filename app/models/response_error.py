from app.utils.utils_json import UtilsJSON

@UtilsJSON.JSON
class ResponseError:
    def __init__(self, status_code: int, status: str, message: str):
        self.__status_code = status_code
        self.__status = status
        self.__message = message