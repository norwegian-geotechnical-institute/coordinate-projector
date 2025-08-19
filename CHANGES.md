# NGI Python Coordinate Projector Package


## Version 0.0.14
_2025-08-19_

Internal

- Replace the package `timezonefinder` with `tzfpy` for improved performance.

## Version 0.0.13
_2025-05-21_

Internal

- Refactor release workflow for PyPI publishing.


## Version 0.0.12
_2025-05-21_

Internal

- Move from Poetry to uv.
- Update packages.


_2024-08-13_

Version 0.0.11

Add

- Support for all EPSG SRID codes that PYPROJ does.

_2024-01-15_

Version 0.0.10

Add

- Swedish projections SWEREF99 with EPSG SRID 3006 to 3018.

_2023-08-24_

Version 0.0.9

- Update packages.

_2023-05-16_

Version 0.0.8

- Change valid Python versions to ">=3.9,<4".
- Update packages.

_2023-03-03_

Version 0.0.7

- Update packages and support Python version 3.11.

_2023-03-03_

Version 0.0.6

- Add new projection epsg 23030.

_2022-10-19_

Version 0.0.5

- Restrict python version to >=3.9 and <3.11. Done so we can upgrade a dependant library (`timezonefinder`). The old
  version of `timezonefinder` use a version of numpy that is flagged by `safety` with a security issue.
- Upgrade other dependant packages.
- Use poetry version 1.2.2 in the build pipeline.

_2022-08-27_

Version 0.0.4

- Remove timezonefinder version requirement.
- Add safety package.

_2022-03-08_

Version 0.0.3

- Breaking change: Removed the Projector.get_transformer() method and changed the
  method signature to Projector.transform(from_srid, to_srid, from_east, from_north).
- Add two new methods ensure_tz() and datetime_to_json().

_2022-03-02_

Version 0.0.1

- Initial version
