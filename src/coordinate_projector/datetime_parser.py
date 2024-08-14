"""
Datetime utilities for converting to and from datetime.datetime, json, naive and time zone aware
"""

from datetime import datetime


from dateutil import tz
from timezonefinder import TimezoneFinder

from coordinate_projector.projector import Projector

projector = Projector()

_time_zone_finder: TimezoneFinder | None = None


def ensure_tz(
    dt: datetime | None,
    longitude: float | None = None,
    latitude: float | None = None,
    srid: int = 4326,
) -> datetime | None:
    """
    Return passed datetime dt enriched with timezone.

    If timezone already present in the input then it is returned untouched.

    If datetime does not contain a timezone, then try to find the timezone by the
    optional location (longitude, latitude in EPSG:4326 in degrees).

    If no location or timezone is provided, then assume the passed datetime is
    recorded in the norwegian timezone.
    """
    global _time_zone_finder

    if not dt:
        return dt

    if not isinstance(dt, datetime):
        raise Exception("Got unexpected type for datetime!")

    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
        # timezone naive (no time zone in dt)
        if longitude is not None and latitude is not None:
            if srid and srid != 4326:
                longitude, latitude = projector.transform(from_srid=srid, to_srid=4326, east=longitude, north=latitude)

            # find timezone from position
            if not _time_zone_finder:
                _time_zone_finder = TimezoneFinder()

            input_timezone = tz.gettz(_time_zone_finder.timezone_at(lng=longitude, lat=latitude))
        else:
            # Assume Norway
            input_timezone = tz.gettz("Europe/Oslo")

        dt = dt.replace(tzinfo=input_timezone)

    return dt


def datetime_to_json(
    dt: datetime | None,
    longitude: float | None = None,
    latitude: float | None = None,
    srid: int = 4326,
) -> str | None:
    """
    Return passed datetime.datetime as json-formatted (iso-8601) string with UTC timezone. Sub-second time information
    is removed.

    If datetime contains timezone information that timezone is used.
    If datetime does not contain a timezone, then assume timezone by the
    optional recording location (longitude, latitude in EPSG:4326 in degrees).
    If no location or timezone is provided, then assume the passed datetime is recorded in the norwegian timezone.
    """
    if not dt:
        return None

    dt = ensure_tz(dt, longitude, latitude, srid=srid)

    if not dt:
        return None

    return dt.replace(microsecond=0).astimezone(tz.UTC).isoformat()
