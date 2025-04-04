from fastapi import APIRouter, HTTPException
from models.vision import VisionData, VisionResponse, DetectedObject, Position
from core.vision_processor import process_image

router = APIRouter(prefix="/api")

@router.post("/vision/process", response_model=VisionResponse)
async def process_vision(data: VisionData):
    try:
        detected_objects = await process_image(data.image_data)
        return VisionResponse(
            status="processed",
            robot_id=data.robot_id,
            detected_objects=detected_objects
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))