from typing import Optional
from davos._davos import SmuggleFunc

__all__: list[str]

def register_parsers_colab() -> None: ...

smuggle_colab: SmuggleFunc
# def smuggle_colab(pkg_name: str, as_: Optional[str] = ...) -> None: ...

def smuggle_parser_colab(line: str) -> str: ...
