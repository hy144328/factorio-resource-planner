import typing

import factorio_resource_planner.model.util

from factorio_resource_planner.model.part import Part
from factorio_resource_planner.model.recipe import Ingredient, Recipe

def load_recipes() -> typing.List[Recipe]:
    return factorio_resource_planner.model.util.load_models(Recipe, "recipes")

def load_parts() -> typing.List[Part]:
    return factorio_resource_planner.model.util.load_models(Part, "parts")
