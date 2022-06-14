__version__ = "0.0.6"
DEMO_TOKEN = "476c477d8a039529478ebd690d35ddd80e3308ffc49b59c65b142321aee963a4"
API_ENDPOINT = "https://api.tibber.com/v1-beta/gql"
SUBSCRIPTION_ENDPOINT = "wss://api.tibber.com/v1-beta/gql/subscriptions"

# Import modules after defining constants to avoid circular import error.
import tibber.networking
import tibber.exceptions
import tibber.types
from .client import Client

from .types.home import TibberHome
from .types.home import NonDecoratedTibberHome
