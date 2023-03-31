from sqlalchemy import Column, Integer, String, Boolean, func, DATE
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contact"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    date_of_birth = Column(DATE)
    created_at = Column('created_at', DateTime, default=func.now())
    updated_at = Column('created_at', DateTime, default=func.now())

