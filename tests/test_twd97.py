import pytest

from coordinate_projector.projector import Projector


WGS84 = 4326  # degree
TDW97 = 3823  # degree
TDW97_METRE = 3822  # TWD97 metre
TM2ZONE121 = 3826  # TWD97 / TM2 zone 121 metre


@pytest.mark.parametrize(
    "from_srid, x, y, to_srid, expected_northing, expected_easting",
    (
        (WGS84, 119.95309745, 24.26204097, TDW97, 24.26204016, 119.95309755),
        (TM2ZONE121, 141981.081, 2684412.806, WGS84, 24.261651, 119.936180),
        (TM2ZONE121, 141981.081, 2684412.806, TDW97, 24.261651, 119.936180),
        (TM2ZONE121, 134545.885, 2681606.433, TDW97, 24.235787, 119.863191),
        (TM2ZONE121, 126655.925, 2678883.348, TDW97, 24.210605, 119.785750),
        (TDW97, 119.785750, 24.210605, TM2ZONE121, 2678883.348, 126655.925),
    ),
)
def test_twd97(from_srid, x, y, to_srid, expected_northing, expected_easting):
    """
    Test data above taken from internal project documents:
    https://dev.azure.com/ngi001/NGI%20Digital/_workitems/edit/12270

    """
    projector = Projector()
    easting, northing = projector.transform(from_srid=from_srid, to_srid=to_srid, east=x, north=y)
    assert easting == pytest.approx(expected_easting)
    assert northing == pytest.approx(expected_northing)
