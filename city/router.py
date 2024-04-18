from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import db
from city import crud, schemas
from dependencies import get_db


router = APIRouter()


@router.get("/cities/", response_model=list[schemas.CityGet])
async def get_cities(db: AsyncSession = Depends(get_db)):
    return await crud.get_cities_list(db=db)


@router.post("/cities/", response_model=schemas.CityCreate)
async def post_city(
        city: schemas.CityCreate,
        db: AsyncSession = Depends(get_db),
):
    return await crud.create_city(db=db, city=city)


@router.get("/cities/{city_id}/", response_model=schemas.CityGet)
async def get_city_by_id(city_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_city_by_id(db=db, city_id=city_id)


@router.patch("/cities/{city_id}/")
async def update_city(
        city: schemas.CityUpdate,
        city_id: int,
        db: AsyncSession = Depends(get_db),
):
    return await crud.update_city(db=db, city=city, city_id=city_id)


@router.delete("/cities/{city_id}/")
async def delete_city(city_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_city(db=db, city_id=city_id)
