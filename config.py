import os

class Config:
    # PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql://app_user:1234@localhost/appdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MongoDB
    MONGO_URI = 'mongodb://app_user:secure_password@localhost:27017/appdb'

    # JWT
    JWT_SECRET_KEY = 'supersecretkey'
