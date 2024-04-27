#!/usr/bin/python3
"""
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    stateName = sys.argv[4]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username, password, database), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(
            State.name == stateName).order_by(State.id).all()

    if states:
        print("{}".format(states[0].id))
    else:
        print("Not found")

    session.close()
