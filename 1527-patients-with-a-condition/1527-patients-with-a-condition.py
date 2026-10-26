
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = patients["conditions"].str.split().apply(
        lambda conditions: any(c.startswith("DIAB1") for c in conditions)
    )
    return patients.loc[mask, ["patient_id", "patient_name", "conditions"]]
