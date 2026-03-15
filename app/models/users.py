from app.db import Base
import enum
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,Integer

class RoleEnum(enum.Enum):
    admin="admin",
    doctor="doctor",
    patient="patient"

class User(Base):
    __tablename__="users"
    name:Mapped[str] = mapped_column(String(100) , nullable=False)
    email:Mapped[str] = mapped_column(String(255) , unique=True, nullable=False)
    hashed_password:Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )
    role:Mapped[RoleEnum] = mapped_column(String(20), nullable=False)