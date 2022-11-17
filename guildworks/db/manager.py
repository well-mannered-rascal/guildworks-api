from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text


Base = declarative_base()


if __name__ == '__main__':
    engine = create_engine(
        """postgresql://postgres:guildworkspass@localhost:5432
        /guildworksdb""",
        echo=True)
    with engine.connect() as conn:
        result = conn.execute(text("select current_database()"))
        print(result.all())
