from src.repositories.mappers.base import DataMapper
from src.models.topics import TopicsOrm
from src.schemas.topics import TopicsSchema



class TopicsDataMapper(DataMapper):
    db_model = TopicsOrm
    schema = TopicsSchema