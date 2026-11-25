from typing import TypeVar

from pydantic import BaseModel

from src.database import Base



DBModelType = TypeVar("DBModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class DataMapper:
    db_model: type[DBModelType]
    schema: type[SchemaType]

    @classmethod
    def map_to_domain(cls, data):
        return cls.schema.model_validate(data, from_attributes=True)


    @classmethod
    def map_to_persistance(cls, data):
        return data.model_dump()