import os
class Config:

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:my-secret-pw@db/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)