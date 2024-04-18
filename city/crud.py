from http.client import HTTPException

from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas


async def get_cities_list(db: AsyncSession):
    query = select(models.DBCity)
    result = await db.execute(query)
    return [city[0] for city in result.fetchall()]


async def create_city(db: AsyncSession, city: schemas.CityCreate):
    query = insert(models.DBCity).values(city.__dict__)
    result = await db.execute(query)
    await db.commit()
    resp = {**city.model_dump(), "id": result.lastrowid}
    return resp


async def get_city_by_id(
        db: AsyncSession,
        city_id: int
):
    query = select(models.DBCity).where(models.DBCity.id == city_id)
    result = await db.execute(query)
    city_record = result.fetchone()
    if not city_record:
        raise HTTPException(status_code=404, detail="City not found")
    return city_record[0]


async def update_city(db: AsyncSession, city: schemas.CityUpdate, city_id: int):
    existing_city = await get_city_by_id(db, city_id)
    if existing_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    query = (
        update(models.DBCity)
        .where(models.DBCity.id == city_id)
        .values(name=city.name, additional_info=city.additional_info)
    )
    await db.execute(query)
    await db.commit()
    return dict(city)


async def delete_city(db: AsyncSession, city_id: int):
    try:
        query = delete(models.DBCity).where(models.DBCity.id == city_id)
        result = await db.execute(query)
        await db.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="City not found")
    except Exception as e:
        await db.rollback()
        raise e
