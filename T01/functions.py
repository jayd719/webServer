
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def get_location_name(cords):
    name=1
    # try:
    #     geoLoc = Nominatim(user_agent="GetLoc")
    #     location = geoLoc.reverse((cords[0], cords[1]), exactly_one=True)
    #     name = location.address if location else None
    # except GeocoderTimedOut as g:
    #     print(f"Error occurred: {g}")
    #     name = None  # Handle timeout error
    # except Exception as e:
    #     print(f"Error occurred: {e}")
    #     name = None  # Handle other exceptions
    return name