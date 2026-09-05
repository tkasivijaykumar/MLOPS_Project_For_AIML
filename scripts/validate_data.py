#!/usr/bin/env python
import sys
from pathlib import Path
import pandas as pd

EXPECTED_COLUMNS = [
    "CustomerID","ProdTaken","Age","TypeofContact","CityTier","Occupation","Gender",
    "NumberOfPersonVisiting","PreferredPropertyStar","MaritalStatus","NumberOfTrips",
    "Passport","OwnCar","NumberOfChildrenVisiting","Designation","MonthlyIncome",
    "PitchSatisfactionScore","ProductPitched","NumberOfFollowups","DurationOfPitch"
]

def validate(path):
    df = pd.read_csv(path)
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    assert not missing, f"Missing columns: {missing}"
    assert df["ProdTaken"].dropna().isin([0,1]).all(), "ProdTaken must be binary."
    print(f"VALID: {path}")
    print(f"Rows={len(df):,}, Columns={len(df.columns)}")
    print(df["ProdTaken"].value_counts().sort_index().to_string())
    return 0

if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/tourism.csv")
    raise SystemExit(validate(path))
