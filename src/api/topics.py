from fastapi import APIRouter

from src.api.dependencies.database import DBDep
from src.schemas.topics import TopicsAdd



router = APIRouter(prefix="/topics", tags=["topics"])


@router.post("")
async def add_topic(
    db: DBDep,
    topic_data: TopicsAdd,
):
    topic = await db.topics.add(topic_data)
    await db.commit()

    return {"status": "OK", "data": topic}