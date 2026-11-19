from sqlalchemy import insert
from pydantic import BaseModel



class BaseRepository():
    model = None
    schema = None

    def __init__(self, session):
        self.session = session


    async def add(self, data: BaseModel):
        query = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(query)
        model = result.scalars().one()
        return self.schema.model_validate(model)