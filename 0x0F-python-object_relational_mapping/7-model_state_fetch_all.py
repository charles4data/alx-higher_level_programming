#!/usr/bin/python3
""" list all state objects in database """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}:@localhost:3306/{}'
                           .fomart(user, passwd, db))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(state).order_by(state_id):
        print(instance.id, instance.name, sep=": ")
