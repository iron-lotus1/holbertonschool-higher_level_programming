#!/usr/bin/python3
"""Prints the first State object from the database."""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_first(username, password, database):
    """Prints the first state object from the database"""
    engine = create_engine('mysql://{}:{}@Localhost/{}'.format(
        username, password, database
    ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()
    if states:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    print_first(argv[1], argv[2], argv[3])
