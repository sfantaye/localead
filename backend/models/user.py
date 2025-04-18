import uuid
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from backend.database import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name: Mapped[str] = mapped_column(String(length=255), nullable=True)
