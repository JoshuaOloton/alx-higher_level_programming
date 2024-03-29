#!/usr/bin/python3
"""
script that lists all City objects
from the database hbtn_0e_101_usa
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    cities = sess.query(City).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    sess.close()
