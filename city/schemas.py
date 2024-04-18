from pydantic import BaseModel


class CityBase(BaseModel):
    name: str
    additional_info: str


class CityCreate(CityBase):
    pass


class CityGet(CityBase):
    id: int

    class Config:
        orm_mode = True


class CityUpdate(CityBase):
    pass
