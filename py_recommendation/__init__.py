#!/usr/bin/env python

"""A library that provides a Python interface to the HERE APIs"""

__author__       = 'Kashyap Madariyil'
__email__        = 'kashyapmadariyil@gmail.com'
__copyright__    = 'Copyright (c) 2020 Kashyap Madariyil'
__license__      = 'MIT License'
__version__      = '0.0.4'
__url__          = 'https://github.com/kashy750/RecoSystem'
__download_url__ = 'https://pypi.org/project/general-utils/'
__description__  = 'A library that provides an easy ready-to-use Recommendation engine.'


import json

from .error import RecoError

# from .here_enum import (
#     RouteMode,
#     MatrixSummaryAttribute,
#     PlacesCategory,
#     PublicTransitSearchMethod,
#     PublicTransitRoutingMode,
#     PublicTransitModeType,
#     WeatherProductType,
#     EVStationConnectorTypes,
#     MultiplePickupOfferType
# )

# from .models import (
#     GeocoderResponse,
#     GeocoderReverseResponse,
#     RoutingResponse,
#     RoutingMatrixResponse,
#     GeocoderAutoCompleteResponse,
#     PlacesResponse,
#     PlacesSuggestionsResponse,
#     PlaceCategoriesResponse,
#     PublicTransitResponse,
#     RmeResponse,
#     TrafficIncidentResponse,
#     DestinationWeatherResponse,
#     EVChargingStationsResponse,
#     WaypointSequenceResponse
# )

# from .destination_weather_api import (
#     DestinationWeatherApi,
#     UnauthorizedError,
#     InvalidRequestError
# )

# from .routing_api import (
#     RoutingApi,
#     InvalidCredentialsError,
#     InvalidInputDataError,
#     WaypointNotFoundError,
#     NoRouteFoundError,
#     LinkIdNotFoundError,
#     RouteNotReconstructedError
# )

from .utils import Utils
from .input_data import ItemData, UserData
from .input_data import InputData
# from .geocoder_api import GeocoderApi
# from .geocoder_reverse_api import GeocoderReverseApi
# from .geocoder_autocomplete_api import GeocoderAutoCompleteApi
# from .places_api import PlacesApi
# from .public_transit_api import PublicTransitApi
# from .rme_api import RmeApi
# from .ev_charging_stations_api import EVChargingStationsApi
# from .fleet_telematics_api import FleetTelematicsApi