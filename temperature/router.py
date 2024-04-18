from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import db
from temperature import crud, schemas
from dependencies import get_db


router = APIRouter()


@router.get("/temperatures/", response_model=list[schemas.TemperatureGet])
async def get_temperature(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_temperatures_with_city_names(db=db)


@router.get("/temperatures/{city_id}/", response_model=schemas.TemperatureGet)
async def get_temperature_by_city_id(
        city_id: int,
        db: AsyncSession = Depends(get_db),
):
    return await crud.get_temperature_for_city(db=db, city_id=city_id)


@router.post("/temperatures/update/", response_model=List[schemas.TemperatureGet])
async def get_temperature(
        db: AsyncSession = Depends(get_db),
):
    await crud.update_temperature_for_city(db=db)
    temperatures = await crud.get_all_temperatures_with_city_names(db)
    return temperatures
