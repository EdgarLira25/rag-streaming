from sqlalchemy.sql.expression import Executable
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from src.apps.shared.database.daos.base import Base
from src.settings import DATABASE_URI

engine = create_engine(
    url=DATABASE_URI, enable_from_linting=False, pool_recycle=600, pool_pre_ping=True
)


class Database:

    def select_one(self, query: Executable) -> dict:
        session = sessionmaker(bind=engine)
        with session() as session:
            result = session.execute(query).fetchone()
            session.close()
            if not result:
                return {}
            return result._asdict()

    def select_all(self, query: Executable) -> list[dict]:
        session = sessionmaker(bind=engine)
        with session() as session:
            results = session.execute(query).fetchall()
            session.close()
            if not results:
                return []
            return [result._asdict() for result in results]

    def statement(self, statement: Executable):
        session = sessionmaker(bind=engine)
        with session() as session:
            session.execute(statement)
            session.commit()
            session.close()

    def migrate_all(self):
        Base.metadata.create_all(engine)
