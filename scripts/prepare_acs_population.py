"""
Prepare 2024 ACS population data for Colorado census tract analysis.

Reads the raw 2024 ACS 5-Year B01003 Total Population dataset,
removes unnecessary Census formatting, creates an 11-digit tract GEOID
compatible with the 2024 TIGER/Line census tract data, and outputs a
cleaned CSV for use in the GIS analysis.

Input:
    data/raw/census/.../ACSDT5Y2024.B01003-Data.csv

Output:
    data/processed/acs_2024_population.csv
"""

import pandas as pd

input_file = "data/raw/census/ACSDT5Y2024.B01003_2026-08-26T124604/ACSDT5Y2024.B01003-Data.csv"
output_file = "data/processed/acs_2024_population.csv"

# Read in CSV file
df = pd.read_csv(input_file, skiprows=[1])

print(df.head())
print(df.shape)


# Clean and re-format data
df["GEOID"] = df["GEO_ID"].str[-11:]

df = df.rename(columns={
    "NAME": "TRACT_NAME",
    "B01003_001E": "POPULATION",
    "B01003_001M": "POP_MOE"
})

df = df[[
    "GEOID",
    "TRACT_NAME",
    "POPULATION",
    "POP_MOE"
]]

print(df.head())
print(df.shape)


# Run Validation checks
assert len(df) == 1447, f"Expected 1447 census tracts, found {len(df)}"
assert df["GEOID"].is_unique, "Duplicate GEOIDs found"
assert df["GEOID"].notna().all(), "Missing GEOIDs found"
assert df["POPULATION"].notna().all(), "Missing population values found"

# Write to output file
df.to_csv(output_file, index=False)
print(f"Cleaned ACS population data write to {output_file}")