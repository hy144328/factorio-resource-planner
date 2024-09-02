import importlib.resources
import typing

import pydantic

import factorio_resource_planner

class Ingredient(pydantic.BaseModel):
    id: str
    quantity: int

class Recipe(pydantic.BaseModel):
    craft_time: float
    input: typing.List[Ingredient]
    output: typing.List[Ingredient]
    produced_by: typing.List[str]

def load_recipes() -> typing.List[Recipe]:
    pkg_files = importlib.resources.files(factorio_resource_planner)
    recipe_files = pkg_files.joinpath("recipes")

    return [
        Recipe.model_validate_json(traversable_it.read_text())
        for traversable_it in recipe_files.iterdir()
    ]
