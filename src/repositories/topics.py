from src.repositories.base import BaseRepository
from src.models.topics import TopicsOrm
from src.schemas.topics import TopicsSchema



class TopicsRepository(BaseRepository):
    model = TopicsOrm
    schema = TopicsSchema