import logging

import asyncpg
from asyncpg import Connection

from api.database.repos.users import UsersRepo


class Repo:
    async def connect(self, *,
                 user: str, password: str,
                 database: str, host: str, port: int = None) -> bool:
        try:
            self.con: Connection = await asyncpg.connect(host=host, port=port,
                                                         user=user, password=password,
                                                         database=database)
        except Exception as e:
            logging.critical(e)
            return False
        
        return True

    async def disconnect(self) -> bool:
        try:
            await self.con.close()
        except Exception as e:
            logging.critical(e)
            return False

        return True

    # TODO Создание всех таблиц сразу
    async def create_tables(self) -> bool:
        pass


    @property
    def users(self) -> UsersRepo:
        return UsersRepo(connection=self.con)
        