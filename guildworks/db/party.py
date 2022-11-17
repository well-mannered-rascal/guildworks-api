from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from manager import Base


class Party(Base):
    __tablename__ = "party"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    leader = Column(Integer, ForeignKey("adventurer.id"))
    members = relationship("Adventurer", back_populates="party")
    # rank TODO Add calculated rank based on averaging of members rank
