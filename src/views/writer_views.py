from flask.views import MethodView
from services.writer_service import WriterServices
from utils.http_response import http_response
from flask import request

class WriterAPI(MethodView):
    
    services = WriterServices()
    
    
    def get(self, writer_id=None): 
        service = self.services.service_get_writers(writer_id=writer_id)
        return http_response(message=service.message, data=service.data, status=service.status, errors=service.errors)
