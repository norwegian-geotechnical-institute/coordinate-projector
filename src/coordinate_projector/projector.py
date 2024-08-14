from functools import cache

import pyproj
from pyproj import Transformer, CRS

_transformers: dict[str, Transformer] = {}


class Projector:
    @staticmethod
    @cache
    def get_supported_projections() -> dict[str, CRS]:
        all_crs_codes = pyproj.database.get_codes("EPSG", pyproj.enums.PJType.PROJECTED_CRS, False)

        return {code: pyproj.CRS.from_epsg(code) for code in all_crs_codes} | {"4326": pyproj.CRS.from_epsg("4326")}

    @staticmethod
    def _get_transformer(from_srid: int | str, to_srid: int | str) -> Transformer:
        global _transformers

        if transformer := _transformers.get(f"{from_srid}-{to_srid}"):
            return transformer

        from_crs = CRS.from_epsg(from_srid)
        to_crs = CRS.from_epsg(to_srid)
        transformer = Transformer.from_crs(from_crs, to_crs, always_xy=True)

        _transformers[f"{from_srid}-{to_srid}"] = transformer

        return transformer

    def transform(self, from_srid: int | str, to_srid: int | str, east: float, north: float) -> tuple[float, float]:
        transformer: Transformer = self._get_transformer(from_srid, to_srid)
        projected_east, projected_north = transformer.transform(east, north)
        return projected_east, projected_north
