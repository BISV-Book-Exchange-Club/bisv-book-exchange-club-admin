from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Sellers(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    paypal = Column(String)
    collection = Column(String)
    total_number_of_books = Column(Integer, default=0)
    dropoff_location = Column(Integer, default=0)
    pricing_option = Column(Integer, default=0)
    proceed_option = Column(Integer, default=0)
    extrabook_option = Column(Integer, default=0)
    comments = Column(String)
    is_active = Column(Boolean(), default=True)
    date_added = Column(Date)
    books = relationship("Books", back_populates="seller")
