from sqlalchemy import insert
from pydantic import BaseModel

from src.repositories.mappers.base import *



class BaseRepository():
    model: type[DBModelType]
    mapper: type[DataMapper[DBModelType, SchemaType]]

    def __init__(self, session):
        self.session = session


    async def add(self, data: BaseModel):
        query = insert(self.model).values(self.mapper.map_to_persistance(data)).returning(self.model)
        result = await self.session.execute(query)
        model = result.scalars().one()
        return self.mapper.map_to_domain(model)