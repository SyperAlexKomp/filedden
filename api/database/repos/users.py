import logging

from asyncpg import Connection

from api.database.repos.base import BaseData


class UserData(BaseData):
    def __init__(self):
        super().__init__()


class BaseRepo:
    def __init__(self, connection: Connection) -> None:
        self.con = connection

    async def create_table(self) -> bool:
        try:
            await self.con.execute(
                """
                CREATE TABLE IF NOT EXISTS users(
                    id bigint UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    api_key text UNIQUE NOT NULL KEY,
                    telegram_id bigint UNIQUE NULL,
                    discord_id bigint UNIQUE NULL,
                    role int NOT NULL DEFAULT 0
                )
                """
            )
        except Exception as e:
            logging.critical(e)
            return False

        return True

    # TODO
    async def get(self, *, id: int) -> UserData:
        pass

    # TODO
    async def add(self) -> bool:
        pass