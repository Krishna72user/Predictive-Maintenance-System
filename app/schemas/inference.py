from pydantic import BaseModel

class InferenceModel(BaseModel):
    type:str
    air_temp:float
    process_temp:float
    rot_speed:int
    torque:float
    tool_wear:int
