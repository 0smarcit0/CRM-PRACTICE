from src.database.db_connection import db

from sqlalchemy.orm import Mapped, mapped_column


class Colegio(db.Model):
    __tablename__ ="colegios"
    id: Mapped[int] = mapped_column(primary_key=True)
    colegio: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    escudo:Mapped[str]
    
    def __str__(self):
        return (f'{self.id}',f'{self.colegio}' )