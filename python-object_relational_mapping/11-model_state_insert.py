#!/usr/bin/python3
"""Adds the State Louisiana to the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_state():
    """
    Connects to MySQL database, adds the State 'Louisiana',
    commits the session, and prints the new state's id.
    """
    if len(sys.argv) != 4:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")

    # Add the new state to the session and commit to the database
    session.add(new_state)
    session.commit()

    # Print the newly generated id
    print(new_state.id)

    session.close()


if __name__ == "__main__":
    insert_state()
