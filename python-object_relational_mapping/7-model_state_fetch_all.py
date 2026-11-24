#!/usr/bin/python3
"""Lists all State objects from the database."""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_states(username, password, database):
    """Prints the state objects in database"""
    engine = create_engine('mysql://{}:{}@Localhost/{}'.format(
        username, password, database
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    print_states(argv[1], argv[2], argv[3])
