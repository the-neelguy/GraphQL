from sqlalchemy import Column, Integer, String, create_engine, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Students(Base):
    __tablename__ = 'StudentsData'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    emailid = Column(String, unique=True)
    contact = Column(Integer, CheckConstraint('length(contact) = 10'), nullable=False)

engine = create_engine('sqlite:///studentsdata.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
  
    