# NGI Projector

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

This is the NGI Python package for projecting koordinates.

References:



Latest releases see [CHANGES.md](CHANGES.md)

# Installation (end user) 

```bash

pip install ngi-projector

```

## Basic usage

### Project a point

```python
from ngi_projector import Projector

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

   - Python 3.9 or higher
   - Poetry
   - black code formatter

2. Clone this repository

3. Install

   `poetry install`



# Build and Test

Run in the project root folder: 

    poetry install pytest 

Build the package wheel: 

    poetry build



# Publish

To publish the package to NGI's private Azure Artifacts repository set the following configuration: 

    poetry config repositories.ngi https://pkgs.dev.azure.com/ngi001/277b2f77-691a-4d92-bd89-8e7cac121676/_packaging/fieldmanager/pypi/upload

To publish the package to Azure Artifacts, make sure you have set up your NGI credentials.

You need to generate Personal Access Token (PAT). Follow
[this guide](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate)
for how to get a PAT via the Azure DevOps GUI. `Packaging (Read, write, & manage)` access is sufficient.

If you want to publish your newly built package you need to set your NGI credentials: 

    poetry config pypi-token.ngi <PAT>

    poetry publish -r ngi

# TODOs

- Handle lines
- Handle polygons
