from database.db_sqlalchemy import db
import datetime

class Writer(db.Model):
    __tablename__ = "writer"
    
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    created_at =db.Column(db.DateTime, default=datetime.datetime.now())
    
