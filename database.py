from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool


db_config: dict = {
            "DB_USER": "postgres",
            "DB_PASSWORD": None,
            "DB_HOST": "localhost",
            "DB_PORT": 5432,
            "DB_NAME": "new_db"
        }


class DBAsyncPg:
    """
    db = DBAsyncPg(config)
    pool = await db.create_pool()
    result = await db.execute("SELECT * FROM users WHERE id = $1", user_id, fetchval=True)
    """
    def __init__(self, config):
        self.pool: Union[Pool, None] = None
        self.config: dict = config or {
            "DB_USER": "postgres",
            "DB_PASSWORD": None,
            "DB_HOST": "localhost",
            "DB_PORT": 5432,
            "DB_NAME": "new_db"
        }

    async def create_pool(self):
        dsn = "postgres://{user}:{password}@{host}:{port}/{database}".format(
            user=self.config["DB_USER"], password=self.config["DB_PASSWORD"], host=self.config["DB_HOST"],
            port=self.config["DB_PORT"], database=self.config["DB_NAME"]
        )
        self.pool = await asyncpg.create_pool(
            dsn,
            command_timeout=60,
            min_size=10,  # in bytes,
            max_size=10,  # in bytes,
            max_queries=50000,
            max_inactive_connection_lifetime=300,
        )
        return self.pool

    async def execute(self, command: str, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
        return result
