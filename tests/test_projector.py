import pytest

from ngi_projector import Projector
from data.coords import Coords
from data.coords import ProjSets


class TestParse:
    projector = Projector()

    @pytest.mark.parametrize(
        "transfDef",
        [
            ("25832-5105"),
            ("25832-5105"),
            ("25832-5106"),
            ("25832-5107"),
            ("25832-5108"),
            ("25832-5109"),
            ("25832-5110"),
            ("25832-5111"),
            ("25833-5112"),
            ("25833-5113"),
            ("25833-5114"),
            ("25833-5115"),
            ("25833-5116"),
            ("25833-5117"),
            ("25834-5118"),
            ("25834-5119"),
            ("25834-5120"),
            ("25834-5121"),
            ("25834-5122"),
            ("25834-5123"),
            ("25835-5124"),
            ("25835-5125"),
            ("25835-5126"),
            ("25835-5127"),
            ("25835-5128"),
            ("25835-5129"),
            ("25836-5130"),
            ("25831-23031"),
            ("25832-23032"),
            ("25833-23033"),
            ("25834-23034"),
            ("25835-23035"),
            ("25836-23036"),
            ("25830-3857"),
            ("25831-3857"),
            ("25832-3857"),
            ("25833-3857"),
            ("25834-3857"),
            ("25835-3857"),
            ("25836-3857"),
            ("25830-4326"),
            ("25831-4326"),
            ("25832-4326"),
            ("25833-4326"),
            ("25834-4326"),
            ("25835-4326"),
            ("25836-4326"),
        ],
    )
    def test_project(self, transfDef):

        projSet = ProjSets[transfDef]
        id = projSet["ID"]
        fc = projSet["fromCoord"]
        tc = projSet["toCoord"]
        expectedAccuracy = projSet["expectedAccuracy"]

        fromEast = Coords[id][fc][0]
        fromNorth = Coords[id][fc][1]

        toEast = Coords[id][tc][0]
        toNorth = Coords[id][tc][1]

        transformer = self.projector.get_transformer(transfDef)
        pEast, pNorth = self.projector.transform(transformer, fromEast, fromNorth)

        assert pEast == pytest.approx(toEast, expectedAccuracy)
        assert pNorth == pytest.approx(toNorth, expectedAccuracy)

        # Reverse the projection - use swapped coords
        p1, p2 = transfDef.split("-")
        reverseTransDef = f"{p2}-{p1}"
        transformer = self.projector.get_transformer(reverseTransDef)
        pEast, pNorth = self.projector.transform(transformer, toEast, toNorth)
        assert pEast == pytest.approx(fromEast, expectedAccuracy)
        assert pNorth == pytest.approx(fromNorth, expectedAccuracy)

    def test_get_supported_projections(self):
        supportedProjections = self.projector.get_supported_projections()
        print(f"Supported projections: {supportedProjections}")
