from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from declarate import Address, Base, Person

engine = create_engine('sqlite:///sqlalchemy_example.db', echo=True)
DBSession = sessionmaker(bind=engine)
session =  DBSession()

new_person = Person(name='new person 3', last_name='last3')
session.add(new_person)
session.commit()

new_address = Address(post_code='999', person = new_person)
session.add(new_address)
session.commit()
