from sqlalchemy import Column, Integer, String, func, DATE
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    date_of_birth = Column(DATE)
    created_at = Column('created_at', DateTime, default=func.now())
    updated_at = Column('created_at', DateTime, default=func.now())

