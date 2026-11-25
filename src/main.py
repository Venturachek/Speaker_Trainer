from fastapi import FastAPI
import uvicorn

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.api.topics import router as topics_router



app = FastAPI()

app.include_router(topics_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)