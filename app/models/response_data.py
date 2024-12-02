class ResponseData:

    def __init__(self, status_code:int, status:str, data:object):
        self.__status_code = status_code
        self.__status = status
        self.__data = data

    def getJson(self) -> dict:
        return {
            "statusCode": self.__status_code,
            "status": self.__status,
            "data": self.__data
        }