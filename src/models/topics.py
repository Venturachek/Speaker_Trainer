import enum
from sqlalchemy import Enum

from src.database import Base
from sqlalchemy.orm import mapped_column, Mapped


class Themes(enum.Enum):
    SPACE = "Space"
    HISTORY = "History"
    BIOLOGY = "Biology"
    TECHNOLOGY = "Technology"
    PHYSICS = "Physics"
    GEOGRAPHY = "Geography"
    PSYCHOLOGY = "Psychology"
    MEDICINE = "Medicine"
    ECONOMICS = "Economics"
    ART = "Art"

class TopicsOrm(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    theme: Mapped[Themes] = mapped_column(Enum(Themes))
    description: Mapped[str | None] = mapped_column(default=None)
