from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TestModel(Base):
    __tablename__ = "test_model"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "TestModel: id='%i' name='%s'" % (self.id, self.name)


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

    def __repr__(self):
        return "Adventurer: '%s' '%s', '%s'" % (
            self.first_name,
            self.last_name,
            self.role,
        )


class Party(Base):
    __tablename__ = "party"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # leader = Column(Integer, ForeignKey("adventurer.id"))
    members = relationship("Adventurer")
    # rank TODO Add calculated rank based on averaging of members rank


# class Quest(Base):
#     __tablename__ = "quest"

#     id = Column(Integer, primary_key=True)
#     type = Column(String)  # TODO define dedicated table for quest types
#     title = Column(String)
#     required_rank = Column(String)
#     reward = Column(String)
#     rank_reward = Column(String)
#     status = Column(String)  # TODO define dedicated table for status types
#     assigned_party = Column(Integer, ForeignKey("party.id"))
#     expiration = Column(DateTime)
