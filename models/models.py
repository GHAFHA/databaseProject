from sqlalchemy import Column, Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    ISBN10 = Column(String, primary_key=True)
    ISBN13 = Column(String)
    Title = Column(String)
    Authro = Column(String)
    Cover = Column(String)
    Publisher = Column(String)
    Pages = Column(Integer)

    # Define a unique constraint for ISBN10
    __table_args__ = (
        UniqueConstraint('ISBN10', name='uq_ISBN10'),
    )

    loans = relationship('BookLoan', back_populates='book')


class Borrower(Base):
    __tablename__ = 'borrowers'

    ID0000id = Column(String, primary_key=True)
    ssn = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    phone = Column(String)


class BookLoan(Base):
    __tablename__ = 'book_loans'

    loan_id = Column(Integer, primary_key=True)
    ISBN10 = Column(String, ForeignKey('books.ISBN10'))
    ID0000id = Column(String, ForeignKey('borrowers.ID0000id'))
    date_out = Column(Date)
    due_date = Column(Date)
    date_in = Column(Date)

    book = relationship('Book', back_populates='loans')
