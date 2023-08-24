"""
Tests of the datetime conversion utilities
"""
from datetime import datetime

import pytest
from dateutil import tz

from coordinate_projector.datetime_parser import datetime_to_json


class TestDatetime:
    def test_datetime_to_json(self):
        """
        Test the datetime_parser.datetime_to_json() method
        """

        assert not datetime_to_json(None), "None if nothing is passed in"
        assert not datetime_to_json(""), "None if nothing is passed in"
        assert not datetime_to_json({}), "None if nothing is passed in"

        # Pass unexpected type
        with pytest.raises(Exception):
            datetime_to_json(5, match=r".*unexpected type.*")

        #
        # Timezone naive datetime
        #

        # Without summertime
        assert datetime_to_json(datetime(1968, 6, 27, 12)) == "1968-06-27T11:00:00+00:00", (
            "Naive datetime without any location is assumed to be in norwegian timezone and "
            "should be converted to UTC (-1h). Note that summertime was not used in Norway year 1968"
        )

        # With summer time
        assert datetime_to_json(datetime(1980, 6, 27, 12)) == "1980-06-27T10:00:00+00:00", (
            "Naive datetime without any location is assumed to be in norwegian timezone and "
            "should be converted to UTC (-2h). Note that summertime was used in Norway year 1980"
        )

        #
        # Timezone aware datetime
        #

        # Norway
        time_zone = tz.gettz("Europe/Oslo")
        # Without summertime
        assert datetime_to_json(datetime(1968, 6, 27, 12, tzinfo=time_zone)) == "1968-06-27T11:00:00+00:00"
        # With summertime
        assert datetime_to_json(datetime(1980, 6, 27, 12, tzinfo=time_zone)) == "1980-06-27T10:00:00+00:00"

        # UTC
        time_zone = tz.UTC
        assert datetime_to_json(datetime(1968, 6, 27, 12, tzinfo=time_zone)) == "1968-06-27T12:00:00+00:00"

        # Australia
        time_zone = tz.gettz("Australia/Canberra")
        # Without summertime year 1970
        assert datetime_to_json(datetime(1970, 11, 27, 12, tzinfo=time_zone)) == "1970-11-27T02:00:00+00:00"
        # With summertime year 2020
        assert datetime_to_json(datetime(2020, 11, 27, 12, tzinfo=time_zone)) == "2020-11-27T01:00:00+00:00"

        #
        # Timezone from location
        #

        # Paris summertime
        # Paris lon=2.2768485 lat=48.8589506
        assert (
            datetime_to_json(datetime(2021, 5, 18, 10), longitude=2.2768485, latitude=48.858956)
            == "2021-05-18T08:00:00+00:00"
        )
        # Paris Lat(6250962.06) Lon(253457.62) EPSG:3857 is in metres - 2D projection
        assert (
            datetime_to_json(datetime(2021, 5, 18, 10), longitude=253457.62, latitude=6250962.06, srid=3857)
            == "2021-05-18T08:00:00+00:00"
        )
        # Paris X: -283194.06 Y: -4170.15 metre EPSG:5107 ETRS89 / NTM zone 7
        assert (
            datetime_to_json(datetime(2021, 5, 18, 10), longitude=-4170.15, latitude=-283194.06, srid=5107)
            == "2021-05-18T08:00:00+00:00"
        )

        # BST summertime
        # Royal Observatory Greenwich lon=0.0005° W lat=51.4769° N
        assert (
            datetime_to_json(datetime(2021, 5, 18, 10), longitude=0.0005, latitude=51.4769)
            == "2021-05-18T09:00:00+00:00"
        )

        # Timezone in datetime, but also passing location. The passed timezone should override the location!
        # Berlin lon=13.358 lat=52.5061 (should not have any effect when timezone is passed)
        # New York summertime
        time_zone = tz.gettz("America/New_York")
        assert (
            datetime_to_json(
                datetime(2021, 5, 18, 6, tzinfo=time_zone),
                longitude=13.358,
                latitude=52.5061,
            )
            == "2021-05-18T10:00:00+00:00"
        )
