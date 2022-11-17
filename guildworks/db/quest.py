from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from manager import Base


class Quest(Base):
    __tablename__ = "quest"

    id = Column(Integer, primary_key=True)
    type = Column(String)  # TODO define dedicated table for quest types
    title = Column(String)
    required_rank = Column(String)
    reward = Column(String)
    rank_reward = Column(String)
    status = Column(String)  # TODO define dedicated table for status types
    assigned_party = Column(Integer, ForeignKey("party.id"))
    expiration = Column(DateTime)
