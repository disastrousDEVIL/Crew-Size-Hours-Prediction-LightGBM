import numpy as np
import pandas as pd

BASE_FEATURES = [
    "job_size_sqft",
    "num_rooms",
    "num_heavy_items",
    "num_light_items",
    "distance_km",
    "floor_number",
    "has_elevator",
    "past_avg_hours",
    "past_avg_crew_size",
]


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Take a DataFrame with base features and return a copy
    with extra engineered columns.
    """
    df = df.copy()

    # ensure boolean is numeric
    df["has_elevator"] = df["has_elevator"].astype(int)

    # avoid divide by zero by using (rooms + 1)
    df["heavy_items_per_room"] = df["num_heavy_items"] / (df["num_rooms"] + 1)
    df["light_items_per_room"] = df["num_light_items"] / (df["num_rooms"] + 1)

    df["sqft_per_room"] = df["job_size_sqft"] / (df["num_rooms"] + 1)

    # extra cost for high floors
    df["floor_penalty"] = np.where(df["floor_number"] > 2,
                                   df["floor_number"] - 2,
                                   0)

    # elevator reduces that penalty
    df["elevator_relief"] = df["has_elevator"] * df["floor_penalty"]

    return df