from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASES

connection_string = "postgresql+psycopg2://{}:{}@{}/{}".format(
    DATABASES["default"]["USER"],
    DATABASES["default"]["PASSWORD"],
    DATABASES["default"]["HOST"],
    DATABASES["default"]["NAME"],
)

engine = create_engine(connection_string)


def get_session():
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    return Session()
