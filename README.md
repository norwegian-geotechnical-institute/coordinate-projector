# Coordinate Projector

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

This is the Norwegian Geotechnical Institute (NGI) Python package for projecting coordinates. 
It is a small shim on top of the library [pyproj](https://github.com/pyproj4/pyproj) that again is an interface to 
 [PROJ](https://proj.org/).  

References:

Latest releases see [CHANGES.md](CHANGES.md)

# Installation (end user) 

```bash

pip install coordinate-projector

```

## Basic usage

### Project a point

```python
from coordinate_projector import Projector

projector = Projector()
 
from_srid = "4326"
to_srid = "3857"

# Paris Lat(48.8589506) Lon(2.2768485) EPSG:4326
from_east, from_north = 2.2768485, 48.8589506 

projected_east, projected_north = projector.transform(from_srid, to_srid, from_east, from_north)

# Paris Lat(6250962.06) Lon(253457.62) EPSG:3857 is in metres - 2D projection
assert abs(projected_east - 253457.62) <= 0.01
assert abs(projected_north - 6250962.06) <= 0.01 

print(f"{projected_east=}, {projected_north=}")
# projected_east=253457.6156334287, projected_north=6250962.062720417
```

# Getting Started developing

1. Software dependencies

   - Python 3.10 or higher
   - uv
   - Ruff code formatter

2. Clone this repository

3. Install

   `uv sync --all-extras --dev`



# Build and Test

Run in the project root folder: 

    uv run pytest 

Build the package wheel: 

    uv build

# Publish

Publish the package to PyPi:

    uv publish --token ${PYPI_TOKEN}

# TODOs

- Handle lines
- Handle polygons

# Contribute

Please start by adding an issue before submitting any pull requests.

