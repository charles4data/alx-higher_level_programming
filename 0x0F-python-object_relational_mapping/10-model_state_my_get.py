#!/usr/bin/python3
""" lists states with letter a from database """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f"mysql://{user}:{passwd}@localhost:3306/{db}")

    Session = sessionmaker(bind=engine)

    session = Session()

    session.query(State).filter(State.name == sys.argv[4]).first()

    for state in states:
        print(state)

    session.close()
