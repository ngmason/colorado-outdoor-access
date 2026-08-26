# Colorado Outdoor Access

A GIS portfolio project exploring geographic access to public outdoor recreation opportunities across Colorado communities.

## Project Status

Initial project setup.

## Planned Workflow

- Define recreation-access metrics
- Gather public GIS datasets
- Clean and prepare spatial data
- Perform proximity/accessibility analysis
- Create final cartographic outputs
- Document methods and findings
- Add Python/ArcPy automation where useful

## Data Sources

### U.S. Census Bureau

- **Dataset:** 2024 TIGER/Line Shapefiles - Census Tracts, Colorado
- **File:** `tl_2024_08_tract`
- **Provider:** U.S. Census Bureau, Geography Division
- **Year:** 2024
- **Purpose:** Census tract boundaries used as the geographic units for the accessibility analysis.
- **Source:** [U.S. Census Bureau TIGER/Line Shapefiles](https://www.census.gov/geographies/mapping-files/2024/geo/tiger-line-file.html)

### U.S. Census Bureau — American Community Survey

- **Dataset:** 2024 ACS 5-Year Estimates — B01003: Total Population
- **File:** `ACSDT5Y2024.B01003_2026-08-26T124604`
- **Provider:** U.S. Census Bureau
- **Year:** 2024
- **Purpose:** Provides total population estimates for each Colorado census tract. Population data are joined to the 2024 TIGER/Line census tract geography using tract GEOIDs.
- **Source:** [2024 ACS 5-Year B01003 — Total Population](https://data.census.gov/table/ACSDT5Y2024.B01003)