from src.database.db_connection import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Employee(db.Model):
    __tablename__ = "employees"
    id_employee:Mapped[int] =mapped_column(primary_key=True, nullable=False)
    name:Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(nullable=False, unique=True)
    password:Mapped[str] = mapped_column(nullable=False)
    admin:Mapped[bool] = mapped_column(nullable=False)
    id_colegio:Mapped[int] =mapped_column(ForeignKey("colegios.id",ondelete="CASCADE"),nullable=False)
    cedula:Mapped[str] = mapped_column(nullable=False)
    position:Mapped[str] = mapped_column(nullable=False)