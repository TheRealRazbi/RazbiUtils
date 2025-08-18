from importlib.metadata import PackageNotFoundError, version

from . import deprecated

try:
    __version__ = version("stage-click")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["deprecated", "__version__"]
