from datetime import datetime

from pydantic import BaseModel


class TemperatureBase(BaseModel):
    date_time: datetime
    temperature: float


class TemperatureCreate(TemperatureBase):
    city_id: int


class TemperatureUpdate(TemperatureBase):
    pass


class TemperatureGet(TemperatureBase):
    id: int

    class Config:
        orm_mode = True


