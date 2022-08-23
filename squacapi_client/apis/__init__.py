
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from squacapi_client.api.default_api import DefaultApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from squacapi_client.api.default_api import DefaultApi
from squacapi_client.api.user_api import UserApi
from squacapi_client.api.v10_api import V10Api
