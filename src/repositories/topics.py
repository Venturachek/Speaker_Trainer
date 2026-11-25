from src.repositories.base import BaseRepository
from src.models.topics import TopicsOrm
from src.repositories.mappers.topics import TopicsDataMapper


class TopicsRepository(BaseRepository):
    model = TopicsOrm
    mapper = TopicsDataMapper