from sqlalchemy.orm import sessionmaker

from app.infrastructure.database.dao.holder import HolderDao


def dao_provider() -> HolderDao:
    ...


class DbProvider:
    def __init__(self, pool: sessionmaker):
        self.pool = pool

    async def dao(self):
        async with self.pool() as session:
            yield HolderDao(session=session)

