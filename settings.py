import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"  # С подгрузкой из .env тест на платформе не проходит
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
