from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from .models import Base


class DBManager:
    def __init__(self, connection: str):
        self.connection = connection
        self.engine = create_engine(connection, echo=True)
        self.sessionmaker = sessionmaker(bind=self.engine)

        Base.metadata.create_all(bind=self.engine)
        self.engine.connect()

    def insert(self, records: list[Base]):
        with self.sessionmaker() as session:
            for record in records:
                session.add(record)
            session.commit()
