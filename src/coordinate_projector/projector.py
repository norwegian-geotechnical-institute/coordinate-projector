from pyproj import Transformer
from typing import Dict, Optional
from .projections import projections

_transformers: Dict[str, Transformer] = {}


class Projector:
    @staticmethod
    def get_supported_projections() -> Dict:
        return projections

    @staticmethod
    def _get_transformer(from_srid: int, to_srid: int) -> Transformer:
        global _transformers

        if transformer := _transformers.get(f"{from_srid}-{to_srid}"):
            return transformer

        from_def_desc: Optional[Dict] = projections.get(str(from_srid))
        if not from_def_desc:
            raise Exception(f"SRID: {from_srid} is not supported")
        from_definition = from_def_desc["definition"]["data"]

        to_def_desc: Optional[Dict] = projections.get(str(to_srid))
        if not to_def_desc:
            raise Exception(f"SRID: {to_srid} is not supported")
        to_definition = to_def_desc["definition"]["data"]

        transformer = Transformer.from_crs(from_definition, to_definition)

        _transformers[f"{from_srid}-{to_srid}"] = transformer

        return transformer

    def transform(self, from_srid: int, to_srid: int, east: float, north: float) -> tuple[float, float]:
        transformer: Transformer = self._get_transformer(from_srid, to_srid)
        projected_east, projected_north = transformer.transform(east, north)
        return projected_east, projected_north
