import typing

import pydantic

class Ingredient(pydantic.BaseModel):
    id: str
    quantity: int

class Recipe(pydantic.BaseModel):
    craft_time: float
    id: str
    input: typing.List[Ingredient]
    output: typing.List[Ingredient]
    produced_by: typing.List[str]
