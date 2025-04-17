import os

class Settings:
    """ @author: Maria Angelica Teheran aguilera,
        @version: v1 2025-04-09
        @Functionality: These are the application configuration variables """
    
    HOST = os.getenv("HOST_IP")
    PORT = os.getenv("PORT_HOST")
    DEBUG = os.getenv("DEBUG")
    
    
    DB_USER = os.getenv("POSTGRES_USER")
    DB_HOST = os.getenv("POSTGRES_HOST")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB_NAME = os.getenv("POSTGRES_DB")
    DB_PORT = os.getenv("POSTGRES_PORT")