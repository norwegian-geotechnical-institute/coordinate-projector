import pytest

from coordinate_projector.projector import Projector
from data.coords import Coords
from data.coords import ProjSets


class TestParse:
    projector = Projector()

    @pytest.mark.parametrize(
        "from_srid,to_srid",
        [
            (25832, 5105),
            (25832, 5105),
            (25832, 5106),
            (25832, 5107),
            (25832, 5108),
            (25832, 5109),
            (25832, 5110),
            (25832, 5111),
            (25833, 5112),
            (25833, 5113),
            (25833, 5114),
            (25833, 5115),
            (25833, 5116),
            (25833, 5117),
            (25834, 5118),
            (25834, 5119),
            (25834, 5120),
            (25834, 5121),
            (25834, 5122),
            (25834, 5123),
            (25835, 5124),
            (25835, 5125),
            (25835, 5126),
            (25835, 5127),
            (25835, 5128),
            (25835, 5129),
            (25836, 5130),
            (25831, 23031),
            (25832, 23032),
            (25833, 23033),
            (25834, 23034),
            (25835, 23035),
            (25836, 23036),
            (25830, 3857),
            (25831, 3857),
            (25832, 3857),
            (25833, 3857),
            (25834, 3857),
            (25835, 3857),
            (25836, 3857),
            (25830, 4326),
            (25831, 4326),
            (25832, 4326),
            (25833, 4326),
            (25834, 4326),
            (25835, 4326),
            (25836, 4326),
        ],
    )
    def test_project(self, from_srid, to_srid):
        trans_def = f"{from_srid}-{to_srid}"
        proj_set = ProjSets[trans_def]
        id = proj_set["ID"]
        fc = proj_set["fromCoord"]
        tc = proj_set["toCoord"]
        expected_accuracy = proj_set["expectedAccuracy"]

        from_east = Coords[id][fc][0]
        from_north = Coords[id][fc][1]

        to_east = Coords[id][tc][0]
        to_north = Coords[id][tc][1]

        projected_east, projected_north = self.projector.transform(from_srid, to_srid, from_east, from_north)

        assert projected_east == pytest.approx(to_east, expected_accuracy)
        assert projected_north == pytest.approx(to_north, expected_accuracy)

        # Reverse the projection - use swapped coords
        projected_east, projected_north = self.projector.transform(to_srid, from_srid, to_east, to_north)
        assert projected_east == pytest.approx(from_east, expected_accuracy)
        assert projected_north == pytest.approx(from_north, expected_accuracy)

    def test_get_supported_projections(self):
        supported_projections = self.projector.get_supported_projections()
        assert "23031" in supported_projections
        assert "4326" in supported_projections  # WGS 84 -- WGS84 - World Geodetic System 1984, used in GPS
        assert "5105" in supported_projections
        assert "3006" in supported_projections
        assert "3010" in supported_projections
        assert "3018" in supported_projections
