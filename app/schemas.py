from pydantic import BaseModel

class JobFeatures(BaseModel):
    job_size_sqft: float
    num_rooms: int
    num_heavy_items: int
    num_light_items: int
    distance_km: float
    floor_number: int
    has_elevator: bool
    past_avg_hours: float
    past_avg_crew_size: float

class PredictionResponse(BaseModel):
    predicted_crew_size: int
    predicted_hours_required: float
