from .sendfile import sendfile  # noqa
from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

# old versions of django-sendfile have this, so keep it for compatibility
VERSION = tuple(__version__.split("+")[0].split("."))
