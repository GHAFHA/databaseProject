from sqlalchemy import Column, Integer, String, Date, ForeignKey, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean

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


class Borrower(Base):
    __tablename__ = 'borrowers'

    id_sequence = Sequence('borrower_id_seq', metadata=Base.metadata)

    ID0000id = Column(String, primary_key=True,
                      default=lambda: f"ID{Borrower.id_sequence.next_value():04d}")
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
    isbn = Column(String, ForeignKey('books.ISBN10'))
    card_no = Column(String, ForeignKey('borrowers.ID0000id'))
    date_out = Column(Date)
    due_date = Column(Date)
    date_in = Column(Date)

    book = relationship('Book', backref='loans')
    borrower = relationship('Borrower', backref='loans')
