from sqlalchemy import String, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    type: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    air_temperature: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    process_temperature: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    rotational_speed: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    torque: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    tool_wear: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    prediction: Mapped[int]=mapped_column(
        Integer,
        nullable=False
    )