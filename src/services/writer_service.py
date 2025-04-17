from querys.writer_query import WriterQuerys
from schemas.requests.writer_schema import WriterSchema
from utils.objects_model import DataResponse, MessagesWriterServices
from http import HTTPStatus


class WriterServices:
    
    writer_schema = WriterSchema()
    writer_querys = WriterQuerys()
    message = MessagesWriterServices()    
    
    def service_get_writers(self, writer_id: int =None):
        data_response = DataResponse()
        
        
        try:
            if writer_id:
                writer = self.writer_querys.get_writer_by_id(writer_id=writer_id)
                if not writer:
                    
                    data_response.status = HTTPStatus.BAD_REQUEST
                    data_response.message = self.message.NOT_SEARCH_WRITER
                    
                    return data_response
                
                data_response.data = dict(self.writer_schema.dump(writer))
                data_response.status = HTTPStatus.OK
                data_response.message = self.message.SEARCH_CORRECT_WRITER
                
                return data_response
            
            else:
                
                writers = self.writer_querys.get_all_writer()
                
                data_response.data = self.writer_schema.dump(writers)
                data_response.status = HTTPStatus.OK
                data_response.message = self.message.SEARCH_CORRECT_WRITERS
                
                return data_response
            
        except Exception as ex:
            
            data_response.message = self.message.ERROR_RETURN_WRITER
            data_response.status = HTTPStatus.INTERNAL_SERVER_ERROR
            data_response.errors = [{"error": str(ex.args)}]
            
            return data_response
    

