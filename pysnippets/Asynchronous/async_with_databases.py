import asyncio
import asyncpg
import logging

async def fetch_from_db():
    conn = await asyncpg.connect(user='user', password='password', database='db', host='localhost')
    logging.info("Connected to database")
    data = await conn.fetch('SELECT * FROM my_table')
    await conn.close()
    return data

async def main():
    data = await fetch_from_db()
    logging.info(f"Data fetched from database: {data}")

if __name__ == "__main__":
    asyncio.run(main()) 