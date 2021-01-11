from sqlalchemy import desc

from db import get_session
from models.models import Recipe


def get_recipe(sort_by, offset: int = None,) -> list:
    session = get_session()
    try:
        results = (
            session.query(Recipe).order_by(desc(sort_by)).offset(offset).limit(25).all()
        )
        return results
    except Exception as ex:
        session.rollback()
        raise ex


def insert_recipe(recipe: Recipe) -> Recipe:
    session = get_session()
    try:
        session.add(recipe)
        session.commit()
        return recipe
    except Exception as ex:
        session.rollback()
        raise ex
    finally:
        session.close()


def update_recipe(recipe_id: int, update_data: dict) -> None:
    session = get_session()
    try:
        session.query(Recipe).filter(Recipe.recipe_id == recipe_id).update(
            update_data
        )
        session.commit()
    except Exception as ex:
        session.rollback()
        raise ex
    finally:
        session.close()

def delete_recipe(recipe_id: int) -> None:
    session = get_session()
    try:
        session.query(Recipe).filter(Recipe.recipe_id == recipe_id).delete()
        session.commit()
    except Exception as ex:
        session.rollback()
        raise ex
    finally:
        session.close()
