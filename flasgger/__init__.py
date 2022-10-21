
__author__ = 'Patrick Huck'
__email__ = 'phuck@lbl.gov'

# Based on works of Bruno Rocha and the Flasgger open source community

from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution("flasgger-tschaume").version
except DistributionNotFound:  # pragma: no cover
    # package is not installed
    pass

from jsonschema import ValidationError  # noqa
from .base import Swagger, Flasgger, NO_SANITIZER, BR_SANITIZER, MK_SANITIZER, LazyJSONEncoder  # noqa
from .utils import swag_from, validate, apispec_to_template, LazyString  # noqa
from .marshmallow_apispec import APISpec, SwaggerView, Schema, fields  # noqa
from .constants import OPTIONAL_FIELDS  # noqa
