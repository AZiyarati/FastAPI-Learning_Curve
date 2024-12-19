from typing import Annotated

def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"

# better explanation at:
# https://fastapi.tiangolo.com/python-types/#type-hints-with-metadata-annotations
