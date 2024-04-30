#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects,
contained in the database
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(City, State).filter(City.state_id == State.id).all()

    for city, state in res:

        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()

