from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    fullname = Column(String, unique=True, nullable=False)
    born_date = Column(String)
    born_location = Column(String)
    description = Column(Text)

class Quote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="quotes")
    tags = Column(String)

Author.quotes = relationship("Quote", order_by=Quote.id, back_populates="author")
