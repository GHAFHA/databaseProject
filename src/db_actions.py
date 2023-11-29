from models.Models import Book, Borrower, BookLoan, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import or_
from sqlalchemy import cast, String
from sqlalchemy import inspect
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
from typing import List


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
            data = pd.read_csv(self.filepath_one,
                               delimiter='\t', encoding='utf-8')
            data.to_sql('books', con=self.engine,
                        if_exists='append', index=False)

            data = pd.read_csv(self.filepath_two)
            data.to_sql('borrowers', con=self.engine,
                        if_exists='append', index=False)

            Base.metadata.create_all(self.engine)

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

    def search_books(self, search_query) -> List:
        try:
            results = self.session.query(Book).filter(
                or_(
                    Book.Title.ilike(f'%{search_query}%'),
                    Book.Author.ilike(f'%{search_query}%'),
                    # Add other fields if needed
                )
            ).all()
            return results
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            return []


def main():
    schema_adder = db_actions('data/books (1).csv', 'data/borrowers (2).csv')
    schema_adder.create_tables()


if __name__ == '__main__':
    main()
