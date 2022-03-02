from typing import Dict, Union

# projections: Dict[int, Dict[str, Union[str, int, Dict]]] = {
projections: Dict[int, Dict] = {
    23031: {
        "srid": 23031,
        "name": "ED50 / UTM zone 31N",
        "shortName": "ED50 UTM 31N",
        "definition": {
            "name": "EPSG:23031",
            "data": "+proj=utm +zone=31 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs",
        },
    },
    23032: {
        "srid": 23032,
        "name": "ED50 / UTM zone 32N",
        "shortName": "ED50 UTM 32N",
        "definition": {
            "name": "EPSG:23032",
            "data": "+proj=utm +zone=32 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs",
        },
    },
    23033: {
        "srid": 23033,
        "name": "ED50 / UTM zone 33N",
        "shortName": "ED50 UTM 33N",
        "definition": {
            "name": "EPSG:23033",
            "data": "+proj=utm +zone=33 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs",
        },
    },
    23034: {
        "srid": 23034,
        "name": "ED50 / UTM zone 34N",
        "shortName": "ED50 UTM 34N",
        "definition": {
            "name": "EPSG:23034",
            "data": "+proj=utm +zone=34 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs",
        },
    },
    23035: {
        "srid": 23035,
        "name": "ED50 / UTM zone 35N",
        "shortName": "ED50 UTM 35N",
        "definition": {
            "name": "EPSG:23035",
            "data": "+proj=utm +zone=35 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs",
        },
    },
    23036: {
        "srid": 23036,
        "name": "ED50 / UTM zone 36N",
        "shortName": "ED50 UTM 36N",
        "definition": {
            "name": "EPSG:2306",
            "data": "+proj=utm +zone=36 +ellps=intl +towgs84=-87,-98,-121,0,0,0,0 +units=m +no_defs",
        },
    },
    25830: {
        "srid": 25830,
        "name": "ETRS89 / UTM zone 30N",
        "shortName": "ETRS89 UTM 30N",
        "definition": {
            "name": "EPSG:25830",
            "data": "+proj=utm +zone=30 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    25831: {
        "srid": 25831,
        "name": "ETRS89 / UTM zone 31N",
        "shortName": "ETRS89 UTM 31N",
        "definition": {
            "name": "EPSG:25831",
            "data": "+proj=utm +zone=31 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    25832: {
        "srid": 25832,
        "name": "ETRS89 / UTM zone 32N",
        "shortName": "ETRS89 UTM 32N",
        "definition": {
            "name": "EPSG:25832",
            "data": "+proj=utm +zone=32 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    25833: {
        "srid": 25833,
        "name": "ETRS89 / UTM zone 33N",
        "shortName": "UTM 33N",
        "definition": {
            "name": "EPSG:25833",
            "data": "+proj=utm +zone=33 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    25834: {
        "srid": 25834,
        "name": "ETRS89 / UTM zone 34N",
        "shortName": "UTM 34N",
        "definition": {
            "name": "EPSG:25834",
            "data": "+proj=utm +zone=34 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    25835: {
        "srid": 25835,
        "name": "ETRS89 / UTM zone 35N",
        "shortName": "UTM 35N",
        "definition": {
            "name": "EPSG:25835",
            "data": "+proj=utm +zone=35 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    25836: {
        "srid": 25836,
        "name": "ETRS89 / UTM zone 36N",
        "shortName": "UTM 36N",
        "definition": {
            "name": "EPSG:25836",
            "data": "+proj=utm +zone=36 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    3857: {
        "srid": 3857,
        "name": "WGS 84 / Pseudo-Mercator",
        "shortName": "WGS 84",
        "definition": {
            "name": "EPSG:3857",
            "data": "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs",
        },
    },
    4326: {
        "srid": 4326,
        "name": "WGS 84",
        "shortName": "WGS 84",
        "definition": {
            "name": "EPSG:4326",
            "data": "+proj=longlat +datum=WGS84 +no_defs ",
        },
    },
    5105: {
        "srid": 5105,
        "name": "ETRS89 / NTM zone 5",
        "shortName": "NTM5",
        "definition": {
            "name": "EPSG:5105",
            "data": "+proj=tmerc +lat_0=58 +lon_0=5.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5106: {
        "srid": 5106,
        "name": "ETRS89 / NTM zone 6",
        "shortName": "NTM6",
        "definition": {
            "name": "EPSG:5106",
            "data": "+proj=tmerc +lat_0=58 +lon_0=6.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5107: {
        "srid": 5107,
        "name": "ETRS89 / NTM zone 7",
        "shortName": "NTM7",
        "definition": {
            "name": "EPSG:5107",
            "data": "+proj=tmerc +lat_0=58 +lon_0=7.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5108: {
        "srid": 5108,
        "name": "ETRS89 / NTM zone 8",
        "shortName": "NTM8",
        "definition": {
            "name": "EPSG:5108",
            "data": "+proj=tmerc +lat_0=58 +lon_0=8.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5109: {
        "srid": 5109,
        "name": "ETRS89 / NTM zone 9",
        "shortName": "NTM9",
        "definition": {
            "name": "EPSG:5109",
            "data": "+proj=tmerc +lat_0=58 +lon_0=9.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5110: {
        "srid": 5110,
        "name": "ETRS89 / NTM zone 10",
        "shortName": "NTM10",
        "definition": {
            "name": "EPSG:5110",
            "data": "+proj=tmerc +lat_0=58 +lon_0=10.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5111: {
        "srid": 5111,
        "name": "ETRS89 / NTM zone 11",
        "shortName": "NTM11",
        "definition": {
            "name": "EPSG:5111",
            "data": "+proj=tmerc +lat_0=58 +lon_0=11.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5112: {
        "srid": 5112,
        "name": "ETRS89 / NTM zone 12",
        "shortName": "NTM12",
        "definition": {
            "name": "EPSG:5112",
            "data": "+proj=tmerc +lat_0=58 +lon_0=12.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5113: {
        "srid": 5113,
        "name": "ETRS89 / NTM zone 13",
        "shortName": "NTM13",
        "definition": {
            "name": "EPSG:5113",
            "data": "+proj=tmerc +lat_0=58 +lon_0=13.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5114: {
        "srid": 5114,
        "name": "ETRS89 / NTM zone 14",
        "shortName": "NTM14",
        "definition": {
            "name": "EPSG:5114",
            "data": "+proj=tmerc +lat_0=58 +lon_0=14.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5115: {
        "srid": 5115,
        "name": "ETRS89 / NTM zone 15",
        "shortName": "NTM15",
        "definition": {
            "name": "EPSG:5115",
            "data": "+proj=tmerc +lat_0=58 +lon_0=15.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5116: {
        "srid": 5116,
        "name": "ETRS89 / NTM zone 16",
        "shortName": "NTM16",
        "definition": {
            "name": "EPSG:5116",
            "data": "+proj=tmerc +lat_0=58 +lon_0=16.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5117: {
        "srid": 5117,
        "name": "ETRS89 / NTM zone 17",
        "shortName": "NTM17",
        "definition": {
            "name": "EPSG:5117",
            "data": "+proj=tmerc +lat_0=58 +lon_0=17.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5118: {
        "srid": 5118,
        "name": "ETRS89 / NTM zone 18",
        "shortName": "NTM18",
        "definition": {
            "name": "EPSG:5118",
            "data": "+proj=tmerc +lat_0=58 +lon_0=18.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5119: {
        "srid": 5119,
        "name": "ETRS89 / NTM zone 19",
        "shortName": "NTM19",
        "definition": {
            "name": "EPSG:5119",
            "data": "+proj=tmerc +lat_0=58 +lon_0=19.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5120: {
        "srid": 5120,
        "name": "ETRS89 / NTM zone 20",
        "shortName": "NTM20",
        "definition": {
            "name": "EPSG:5120",
            "data": "+proj=tmerc +lat_0=58 +lon_0=20.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5121: {
        "srid": 5121,
        "name": "ETRS89 / NTM zone 21",
        "shortName": "NTM21",
        "definition": {
            "name": "EPSG:5121",
            "data": "+proj=tmerc +lat_0=58 +lon_0=21.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5122: {
        "srid": 5122,
        "name": "ETRS89 / NTM zone 22",
        "shortName": "NTM22",
        "definition": {
            "name": "EPSG:5122",
            "data": "+proj=tmerc +lat_0=58 +lon_0=22.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5123: {
        "srid": 5123,
        "name": "ETRS89 / NTM zone 23",
        "shortName": "NTM23",
        "definition": {
            "name": "EPSG:5123",
            "data": "+proj=tmerc +lat_0=58 +lon_0=23.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5124: {
        "srid": 5124,
        "name": "ETRS89 / NTM zone 24",
        "shortName": "NTM24",
        "definition": {
            "name": "EPSG:5124",
            "data": "+proj=tmerc +lat_0=58 +lon_0=24.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5125: {
        "srid": 5125,
        "name": "ETRS89 / NTM zone 25",
        "shortName": "NTM25",
        "definition": {
            "name": "EPSG:5125",
            "data": "+proj=tmerc +lat_0=58 +lon_0=25.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5126: {
        "srid": 5126,
        "name": "ETRS89 / NTM zone 26",
        "shortName": "NTM26",
        "definition": {
            "name": "EPSG:5126",
            "data": "+proj=tmerc +lat_0=58 +lon_0=26.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5127: {
        "srid": 5127,
        "name": "ETRS89 / NTM zone 27",
        "shortName": "NTM27",
        "definition": {
            "name": "EPSG:5127",
            "data": "+proj=tmerc +lat_0=58 +lon_0=27.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5128: {
        "srid": 5128,
        "name": "ETRS89 / NTM zone 28",
        "shortName": "NTM28",
        "definition": {
            "name": "EPSG:5128",
            "data": "+proj=tmerc +lat_0=58 +lon_0=28.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5129: {
        "srid": 5129,
        "name": "ETRS89 / NTM zone 29",
        "shortName": "NTM29",
        "definition": {
            "name": "EPSG:5129",
            "data": "+proj=tmerc +lat_0=58 +lon_0=29.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
    5130: {
        "srid": 5130,
        "name": "ETRS89 / NTM zone 30",
        "shortName": "NTM30",
        "definition": {
            "name": "EPSG:5130",
            "data": "+proj=tmerc +lat_0=58 +lon_0=30.5 +k=1 +x_0=100000 +y_0=1000000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs",
        },
    },
}