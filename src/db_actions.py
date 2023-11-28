from models.Models import Book, Borrower, BookLoan
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import or_
from sqlalchemy import cast, String
from sqlalchemy import inspect
from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy import URL
# import psycopg2
import pandas as pd
from typing import List


# url_object = URL.create(
#     "postgresql",
#     "noeljohnson",
#     "",
#     "localhost:5432",
#     "test_server"
# )


class db_actions:
    def __init__(self, filepath_one, filepath_two):
        self.filepath_one = filepath_one
        self.filepath_two = filepath_two
        self.engine = create_engine(
            'postgresql://noeljohnson:''@localhost:5432/postgres', echo=True
        )
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_tables(self):
        try:
            BookLoan.metadata.create_all(self.engine)
            return True
        except SQLAlchemyError as e:
            print(f"An error occurred while creating tables: {e}")
            return False

    # this method got a little weird
    def add_book_avail(self) -> bool:
        try:
            with self.engine.connect() as connection:
                # Check if the column exists
                inspector = inspect(connection)
                columns = [col['name']
                           for col in inspector.get_columns('books')]
                if 'book_availability' in columns:
                    # drop the column if it exists
                    connection.execute(
                        'ALTER TABLE books DROP COLUMN book_availability;'
                    )
                else:
                    print('Column "book_availability" does not exist.')
            return True
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            return False

    def add_loans(self) -> bool:
        try:
            BookLoan.metadata.create_all(self.engine)
            return True
        except SQLAlchemyError as e:
            print(f"An error occurred while creating 'book_loans' table: {e}")
            return False

    def checkout_books(self, isbn_list, card_no):
        pass


def main():
    schema_adder = db_actions('data/books (1).csv', 'data/borrowers (2).csv')
    schema_adder.add_books()
    schema_adder.add_borrowers()
    schema_adder.create_tables()


if __name__ == '__main__':
    main()
