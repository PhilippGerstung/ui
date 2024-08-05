import math

from models.geo import GeoSquare


def calculate_square(lat: float, lon: float, distance: float) -> GeoSquare:
    """Calculates a square around a central geocoordinate.

    Args:
      lat: Latitude of the central point.
      lon: Longitude of the central point.
      distance: Side length of the square in kilometers.

    Returns:
      A tuple of (min_lat, max_lat, min_lon, max_lon).
    """
    assert lat >= -90 and lat <= 90, "Latitude must be between -90 and 90"
    assert lon >= -180 and lon <= 180, "Longitude must be between -180 and 180"
    assert distance > 0, "Distance must be greater than 0"

    # Approximate Earth's radius
    earth_radius = 6371.0

    # Convert distance to radians
    distance_rad = distance / earth_radius

    # Calculate latitude and longitude offsets in degrees
    lat_offset = math.degrees(distance_rad)
    lon_offset = math.degrees(distance_rad / math.cos(math.radians(lat)))

    # Calculate corners of the square
    min_lat = lat - lat_offset / 2
    max_lat = lat + lat_offset / 2
    min_lon = lon - lon_offset / 2
    max_lon = lon + lon_offset / 2

    return GeoSquare(min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon)
