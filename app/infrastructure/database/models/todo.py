from sqlalchemy import String, Text, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app import dto
from app.infrastructure.database.models.base import BaseModel


class Todo(BaseModel):
    __tablename__ = "todo"

    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(Enum(dto.Status), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    def __str__(self):
        return f"{self.name}\n" \
               f"{self.description}\n" \
               f"{self.status}\n" \
               f"{self.user_id}"
