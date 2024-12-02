class ResponseError:
    def __init__(self, status_code: int, status: str, message: str):
        self.__status_code = status_code
        self.__status = status
        self.__message = message

    def getJSON(self) -> dict:
        return {
            "statusCode": self.__status_code,
            "status": self.__status,
            "message": self.__message
        }