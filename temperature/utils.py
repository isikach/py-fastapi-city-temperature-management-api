import asyncio
import os

import httpx


#API_KEY = os.getenv("API_KEY")
API_KEY = "604203a9a0524ef7939145558242503"

async def fetch_temperature_for_city(city: str) -> float:
    payload = {"key": API_KEY, "q": city}
    URL = "http://api.weatherapi.com/v1/current.json"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(URL, params=payload)
            data = response.json()
            celsius = data["current"]["temp_c"]
            print(f"Temperature in {city}: {celsius}°C")
            return celsius
    except httpx.HTTPError as exc:
        print(f"HTTP error occurred: {exc}")
    except httpx.RequestError as exc:
        print(f"Request error occurred: {exc}")


if __name__ == "__main__":
    city_names = ["Paris", "Lion"]

    async def main():
        await asyncio.gather(*(fetch_temperature_for_city(city) for city in city_names))


    asyncio.run(main())
