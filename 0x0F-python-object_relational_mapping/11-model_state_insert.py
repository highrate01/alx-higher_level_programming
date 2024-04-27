#!/usr/bin/python3
"""
adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy.orm  import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name="Louisiana")
    session.add(newState)
    session.commit()
    print(newState.id)
    session.close()
