from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///students.db')
Session = sessionmaker(bind=engine)
session = Session()

class Students(Base):
    __tablename__ = 'StudentsData'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    emailid = Column(String, unique=True)
    contact = Column(String, CheckConstraint('length(contact) = 10'), nullable=False)

Base.metadata.create_all(engine)
