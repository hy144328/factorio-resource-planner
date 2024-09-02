import importlib.resources
import typing

import pydantic

T = typing.TypeVar("T", bound=pydantic.BaseModel)

def load_models(
    model_type: typing.Type[T],
    model_path: typing.Union[str, typing.Sequence[str]],
) -> typing.List[T]:
    import factorio_resource_planner

    model_path = model_path if not isinstance(model_path, str) else [model_path]

    pkg_files = importlib.resources.files(factorio_resource_planner)
    recipe_files = pkg_files.joinpath(*model_path)

    return [
        model_type.model_validate_json(traversable_it.read_text())
        for traversable_it in recipe_files.iterdir()
    ]
