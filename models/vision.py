from pydantic import BaseModel
from typing import List, Optional

class Position(BaseModel):
    x: float
    y: float
    z: float

class DetectedObject(BaseModel):
    type: str
    confidence: float
    position: Position

class VisionData(BaseModel):
    robot_id: str
    image_data: str

class VisionResponse(BaseModel):
    status: str
    robot_id: str
    detected_objects: List[DetectedObject]