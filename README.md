# NGI Projecter

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

This is the NGI Python package for projecting koordinates.

References:



Latest releases see [CHANGES.md](CHANGES.md)

# Installation (end user) 

```bash

pip install ngi-projecter

```

## Basic usage

### Project a point
```python
from ngi_projecter import Projecter

projecter = Projecter()
#SRIDS 
fromSrid = "<SRID>"
toSrid = "<SRID>"

transformer = projecter.get_transformer(f"{fromSrid}-{toSrid}")
projectedEast, projectedNorth = projecter.transform(transformer,fromEastCoord,fromNorthCoord)

             
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

- 
