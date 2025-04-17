class DataResponse():
    
    message: str = ""
    errors:dict | list = {}
    data:dict | list = {}
    status: int = 200
    
    
class MessagesPeopleServices:
    NOT_SEARCH_WRITER = "Writer not found"
    SEARCH_CORRECT_WRITER = "Return data writers"
    ERROR_RETURN_WRITERs = "Error return data writers"