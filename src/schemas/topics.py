from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.models.topics import Themes



class TopicsSchema(BaseModel):
    id: int
    name: str
    theme: Themes
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)



class TopicsAdd(BaseModel):
    name: str
    theme: Themes
    description: Optional[str] = None