from asyncpg import Connection


class BaseRepo:
    def __init__(self, connection: Connection) -> None:
        self.con = connection

    # TODO
    def toJSON(self) -> dict:
        pass


class BaseData:
    def __init__(self):
        pass

    def __str__(self):
        data_str = ""
        data = vars(self).items()
        for num, name, data in enumerate(data):
            data_str += f"{name}={data}"

            if num + 1 < len(data):
                data += ","


        return f"{self.__class__.__name__}<{data_str}>"