from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
)
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class Recipe(Base):
    __tablename__ = "tbl_recipe_records"
    __table_args__ = {"schema": "public"}

    recipe_id = Column(Integer, primary_key=True)
    dish_name = Column(String(50))
    is_vegetarian = Column(Boolean)
    ingredients = Column(String)
    dish_recipe = Column(String)
    people_count = Column(Integer)
    created_on = Column(DateTime, default=datetime.utcnow())
