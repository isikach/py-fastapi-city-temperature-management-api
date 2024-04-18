import asyncio
from datetime import datetime

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from city.crud import get_city_by_id
from city.models import DBCity
from temperature.models import DBTemperature
from temperature.utils import fetch_temperature_for_city


async def get_all_temperatures_with_city_names(db: AsyncSession):
    temperatures = await db.execute(select(DBTemperature).join(DBCity))
    temperatures_with_city_names = []
    for temperature, city in temperatures.scalars():
        temperatures_with_city_names.append({
            "city_name": city.name,
            "temperature": temperature.temperature,
            "date_time": temperature.date_time
        })
    return temperatures_with_city_names


async def get_temperature_for_city(db: AsyncSession, city_id: int):
    temperatures = await db.execute(select(DBTemperature).filter_by(city_id=city_id))
    return temperatures.scalars().first()


async def update_temperature_for_city(db: AsyncSession):
    query = select(DBCity.id)
    result = await db.execute(query)
    city_ids = [row[0] for row in result]
    for city_id in city_ids:
        query = select(DBCity.name).where(DBCity.id == city_id)
        res = await db.execute(query)
        city_name = res.scalar_one() if res.rowcount > 0 else None
        temp = await fetch_temperature_for_city(city_name)
        query = insert(DBTemperature).values(
            city_id=city_id,
            date_time=datetime.now(),
            temperature=temp
        )
        result = await db.execute(query)
        temperatures = result.fetchall()

        return temperatures

