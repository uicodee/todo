from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.models.base import BaseModel


class User(BaseModel):

    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    def __str__(self):
        return f"{self.name}\n" \
               f"{self.email}\n" \
               f"{self.password}"
