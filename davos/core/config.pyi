from pathlib import PurePosixPath
from typing import (
    Any, 
    ClassVar, 
    Final, 
    Literal, 
    NoReturn, 
    Optional, 
    Protocol, 
    TypeVar, 
    Union
)
from ipykernel.zmqshell import ZMQInteractiveShell

__all__: list[Literal['DavosConfig']]

_Environment = Literal['Colaboratory', 'IPython<7.0', 'IPython>=7.0', 'Python']
_IpyShell = TypeVar('_IpyShell', bound=ZMQInteractiveShell)
_PathLike = Union[PurePosixPath, str]

class _IpyShowSyntaxErrorPre7(Protocol):
    def __call__(self, filename: Optional[str] = ...) -> None: ...
    
class _IpyShowSyntaxErrorPost7(Protocol):
    def __call__(self, filename: Optional[str] = ..., running_compile_code: bool = ...) -> None: ...

class SingletonConfig(type):
    __instance: ClassVar[Optional[DavosConfig]]
    def __call__(cls, *args, **kwargs) -> DavosConfig: ...
    
class DavosConfig(metaclass=SingletonConfig):
    _active: bool
    _allow_rerun: bool
    _conda_avail: Optional[bool]
    _conda_env_path: Optional[str]
    _confirm_install: bool
    _environment: Final[_Environment]
    _ipy_showsyntaxerror_orig: Final[Optional[Union[_IpyShowSyntaxErrorPre7, _IpyShowSyntaxErrorPost7]]]
    _ipython_shell: Final[Optional[_IpyShell]]
    _pip_executable: str
    _smuggled: dict[str: str]
    _stdlib_modules: Final[set[str]]
    _suppress_stdout: bool
    @staticmethod
    def _get_stdlib_modules() -> set[str]: ...
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def active(self) -> bool: ...
    @active.setter
    def active(self, state: bool) -> None: ...
    @property
    def allow_rerun(self) -> bool: ...
    @allow_rerun.setter
    def allow_rerun(self, value: bool) -> None: ...
    @property
    def conda_avail(self) -> bool: ...
    @conda_avail.setter
    def conda_avail(self, _: Any) -> NoReturn: ...
    @property
    def conda_env_path(self) -> Optional[str]: ...
    @conda_env_path.setter
    def conda_env_path(self, env_path: _PathLike) -> None: ...
    @property
    def confirm_install(self) -> bool: ...
    @confirm_install.setter
    def confirm_install(self, value: bool) -> None: ...
    @property
    def environment(self) -> _Environment: ...
    @environment.setter
    def environment(self, _: Any) -> NoReturn: ...
    @property
    def ipython_shell(self) -> Optional[_IpyShell]: ...
    @ipython_shell.setter
    def ipython_shell(self, _: Any) -> NoReturn: ...
    @property
    def pip_executable(self) -> str: ...
    @pip_executable.setter
    def pip_executable(self, exe_path: _PathLike) -> None: ...
    @property
    def smuggled(self) -> _Environment: ...
    @smuggled.setter
    def smuggled(self, _: Any) -> NoReturn: ...
    @property
    def suppress_stdout(self) -> bool: ...
    @suppress_stdout.setter
    def suppress_stdout(self, value) -> None: ...