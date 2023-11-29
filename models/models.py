from sqlalchemy import Column, Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    ISBN10 = Column(String, primary_key=True)
    ISBN13 = Column(String, nullable=True)
    Title = Column(String, nullable=False)
    Author = Column(String, nullable=False)
    Cover = Column(String, nullable=True)
    Publisher = Column(String, nullable=True)
    Pages = Column(Integer, nullable=True)

    __table_args__ = (
        UniqueConstraint('ISBN10', name='uq_ISBN10'),
    )

    loans = relationship('BookLoan', back_populates='book')


class Borrower(Base):
    __tablename__ = 'borrowers'

    ID0000id = Column(String, primary_key=True)
    ssn = Column(String, nullable=True, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    phone = Column(String, nullable=True)


class BookLoan(Base):
    __tablename__ = 'book_loans'

    loan_id = Column(Integer, primary_key=True)
    ISBN10 = Column(String, ForeignKey('books.ISBN10'))
    borrower_id = Column(String, ForeignKey(
        'borrowers.ID0000id'), nullable=False)
    date_out = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    date_in = Column(Date)

    book = relationship('Book', back_populates='loans')
    borrower = relationship('Borrower', backref='loans')
