import json

from flask import Flask, request, Response

from crud import crud_recipe
from http_response_code import HTTPResponseCode
from models.models import Recipe

app = Flask(__name__)
http_response_code = HTTPResponseCode()


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/get_recipe", methods=["GET"])
def get_recipe() -> Response:
    try:
        page_size = 25
        page = request.args.get("page", default=1, type=int)
        offset = page * page_size - page_size
        recipes = crud_recipe.get_recipe(sort_by=Recipe.created_on, offset=offset)
        response_recipe_data = []
        for recipe in recipes:
            recipe_data = {
                "recipe_id": recipe.recipe_id,
                "dish_name": recipe.dish_name,
                "ingredients": recipe.ingredients,
                "is_vegetarian": recipe.is_vegetarian,
                "dish_recipe": recipe.dish_recipe,
                "created_on": recipe.created_on.strftime("%d-%m-%Y %H:%M:%S"),
            }
            response_recipe_data.append(recipe_data)
        success_message = {
            "status": "success",
            "recipe_data": response_recipe_data,
            "success_message": "recipes fetched successfully",
        }
        return Response(
            response=json.dumps(success_message), status=http_response_code.HTTP_200_OK
        )
    except Exception as ex:
        error_message = {"status": "failed", "error_message": ex.args[0]}
        return Response(
            json.dumps(error_message),
            status=http_response_code.HTTP_500_INTERNAL_SERVER_ERROR,
            mimetype="application/json",
        )


@app.route("/insert_recipe", methods=["POST"])
def insert_recipe() -> Response:
    try:
        if not recipe_validation(request.json):
            error_message = {"status": "failed", "error_message": "invalid data"}
            return Response(
                json.dumps(error_message),
                status=http_response_code.HTTP_406_NOT_ACCEPTABLE,
                mimetype="application/json",
            )
        else:
            recipe = Recipe()
            recipe.dish_name = request.json.get("dish_name")
            recipe.is_vegetarian = request.json.get("is_vegetarian")
            recipe.people_count = request.json.get("people_count")
            recipe.ingredients = json.dumps(request.json.get("ingredients"))
            recipe.dish_recipe = request.json.get("dish_recipe")
            recipe = crud_recipe.insert_recipe(recipe)
            success_message = {
                "status": "success",
                "success_message": "successfully inserted recipe",
                "recipe_id": recipe.recipe_id,
            }
            return Response(
                json.dumps(success_message),
                status=http_response_code.HTTP_200_OK,
                mimetype="application/json",
            )
    except Exception as ex:
        error_message = {"status": "failed", "error_message": ex.args[0]}
        return Response(
            json.dumps(error_message),
            status=http_response_code.HTTP_500_INTERNAL_SERVER_ERROR,
            mimetype="application/json",
        )


@app.route("/update_recipe", methods=["PUT"])
def update_recipe() -> Response:
    try:
        recipe_id = request.json.get("recipe_id")
        update_data = request.json.get("update_data")
        crud_recipe.update_recipe(recipe_id=recipe_id, update_data=update_data)
        success_message = {
            "status": "success",
            "success_message": "successfully updated recipe",
            "recipe_id": recipe_id,
        }
        return Response(
            json.dumps(success_message),
            status=http_response_code.HTTP_200_OK,
            mimetype="application/json",
        )
    except Exception as ex:
        error_message = {"status": "failed", "error_message": ex.args[0]}
        return Response(
            json.dumps(error_message),
            status=http_response_code.HTTP_500_INTERNAL_SERVER_ERROR,
            mimetype="application/json",
        )


@app.route("/delete_recipe", methods=["DELETE"])
def delete_recipe() -> Response:
    try:
        recipe_id = request.json.get("recipe_id")
        crud_recipe.delete_recipe(recipe_id=recipe_id)
        success_message = {
            "status": "success",
            "success_message": "successfully deleted recipe",
            "recipe_id": recipe_id,
        }
        return Response(
            json.dumps(success_message),
            status=http_response_code.HTTP_200_OK,
            mimetype="application/json",
        )
    except Exception as ex:
        error_message = {"status": "failed", "error_message": ex.args[0]}
        return Response(
            json.dumps(error_message),
            status=http_response_code.HTTP_500_INTERNAL_SERVER_ERROR,
            mimetype="application/json",
        )

## Test cases
def recipe_validation(recipe_json) -> bool:
    if (
        not "dish_name" in recipe_json
        or not "is_vegetarian" in recipe_json
        or not "people_count" in recipe_json
        or not "ingredients" in recipe_json
        or not "dish_recipe" in recipe_json
    ):
        return False

    else:
        return True


if __name__ == "__main__":
    app.run()
