from pyproj import Transformer
from typing import Dict, Optional
from .projections import projections


class Projector:
    transformers: Dict[str, Transformer] = {}

    def get_supported_projections(self) -> Dict:
        return projections

    def get_transformer(self, transformDef: str) -> Transformer:
        print(f"transformDef: {transformDef}")

        if transformer := self.transformers.get(transformDef):
            return transformer

        from_def_str, to_def_str = transformDef.split("-")
        fromDefDesc: Optional[Dict] = projections.get(from_def_str)
        if not fromDefDesc:
            raise Exception(f"SRID: {from_def_str} is not supported")
        fromDef = fromDefDesc["definition"]["data"]

        toDefDesc: Optional[Dict] = projections.get(to_def_str)
        if not toDefDesc:
            raise Exception(f"SRID: {to_def_str} is not supported")
        toDef = toDefDesc["definition"]["data"]
        transformer = Transformer.from_crs(fromDef, toDef)
        self.transformers[transformDef] = transformer
        return transformer

    def transform(self, transformer: Transformer, east: float, north: float) -> tuple[float, float]:
        eastPyProj, northPyProj = transformer.transform(east, north)
        return eastPyProj, northPyProj
