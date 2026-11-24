#!/usr/bin/python3
"""Lists all State objects containing the letter a."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_states_with_a():
    """
    Connects to MySQL database and prints all State objects
    containing the letter 'a' ordered by states.id.
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

    # Query states containing the letter 'a' ordered by id
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    filter_states_with_a()
