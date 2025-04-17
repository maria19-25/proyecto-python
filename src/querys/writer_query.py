from models.writer_model import Writer
from database.db_sqlalchemy import db

class WriterQuerys:
    
    
    def get_all_writers(self):
        return Writer.query.all()
    
    def get_writer_by_id(self, people_id):
        return Writer.query.get(people_id)
    
    def create_writer(self, data:dict):
        writer_new = Writer(**data)
        db.session.add(writer_new)
        db.session.commit()
        return writer_new
    
    def update_writer(self, writer_id:int, data:dict):
        writer = writer.query.filter_by(id=writer_id).update(data)
        db.session.commit()
        return writer
    
    def delete_writer(self, writer: Writer):
        db.session.delete(writer)
        db.session.commit()
    
    
    