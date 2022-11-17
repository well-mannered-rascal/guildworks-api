from sqlalchemy import Column, String, Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from manager import Base


class Adventurer(Base):
    __tablename__ = "adventurer"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(String)
    # rank TODO calculate this value based on rank points
    rank_points = Column(Integer)
    career_earnings = Column(Numeric)
    party_id = Column(Integer, ForeignKey("party.id"))
    party = relationship("Party", back_populates="adventurer")
