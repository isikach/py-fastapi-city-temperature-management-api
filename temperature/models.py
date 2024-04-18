from sqlalchemy import Integer, Column, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from city.models import DBCity
from db.database import Base


class DBTemperature(Base):
    __tablename__ = "temperature"

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey("city.id"), nullable=False)
    date_time = Column(DateTime, nullable=False)
    temperature = Column(Float, nullable=False)

    city = relationship(DBCity)
