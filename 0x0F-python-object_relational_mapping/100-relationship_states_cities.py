#!/usr/bin/python3
"""
creates the State “California” with the City “San
Francisco” from the database hbtn_0e_100_usa
"""
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name="California")
    session.add(newState)
    session.commit()
    newCity = City(name="San Francisco", state_id=newState.id)
    session.add(newCity)
    session.commit()
    session.close()
