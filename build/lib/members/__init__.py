from .celery import app as celery_app

__all__ = ('celery_app',)

from . import _version
__version__ = _version.get_versions()['version']
