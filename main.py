from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from api.vision_handler import router

# Load environment variables
load_dotenv()

app = FastAPI(title="Robot Vision Service")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# Include the API router
app.include_router(router)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 9001))
    uvicorn.run(app, host="0.0.0.0", port=port)