from sqlalchemy import Column, Integer, String

from db.database import Base


class DBCity(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    additional_info = Column(String(1024))
