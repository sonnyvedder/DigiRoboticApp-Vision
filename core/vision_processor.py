from models.vision import DetectedObject, Position
from typing import List
import os

async def process_image(image_data: str) -> List[DetectedObject]:
    # Placeholder for vision processing logic
    debug = os.getenv("VISION_DEBUG", "false").lower() == "true"
    
    if debug:
        print(f"Processing image data of length: {len(image_data)}")
    
    # Example detection
    return [
        DetectedObject(
            type="object",
            confidence=0.95,
            position=Position(x=0, y=0, z=0)
        )
    ]