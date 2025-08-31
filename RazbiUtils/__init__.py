from importlib.metadata import PackageNotFoundError, version

from . import deprecated
from . import core

try:
    __version__ = version("stage-click")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["deprecated", "core", "__version__"]
