from models.Models import Book, Borrower, BookLoan
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import or_
from sqlalchemy import cast, String
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

    def parse_csv(self):
        df_one = pd.read_csv(self.filepath_one)
        df_two = pd.read_csv(self.filepath_two)
        return df_one, df_two

    def add_avail(self) -> bool:
        try:
            with self.engine.begin() as connection:
                connection.execute(
                    'ALTER TABLE books ADD COLUMN IF NOT EXISTS availability BOOLEAN DEFAULT TRUE;')
            return True
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            return False

    def add_books(self) -> List:
        data = pd.read_csv(self.filepath_one, delimiter='\t', encoding='utf-8')
        data.to_sql('books', con=self.engine,
                    if_exists='replace', index=False)
        results = self.session.query(Book).all()

        return results

    def add_borrowers(self) -> List:
        data = pd.read_csv(self.filepath_two)
        data.to_sql('borrowers', con=self.engine,
                    if_exists='replace', index=False)
        results = self.session.query(Borrower).all()

        return results

    def add_loans(self) -> bool:
        try:
            BookLoan.metadata.create_all(self.engine)
            return True
        except SQLAlchemyError as e:
            print(f"An error occurred while creating 'book_loans' table: {e}")
            return False

    def search_books(self, search_query):
        search_query = '%' + search_query.lower() + '%'  # for substring matching

        results = self.session.query(Book).filter(
            or_(
                cast(Book.ISBN10, String).ilike(search_query),
                cast(Book.ISBN13, String).ilike(search_query),
                Book.Title.ilike(search_query),
                Book.Authro.ilike(search_query),
            )
        ).all()

        search_results = []
        for book in results:
            availability = 'Available' if book.availability else 'Checked out'
            search_results.append({
                'ISBN': book.ISBN10,
                'Title': book.Title,
                'Author': book.Authro,
                'Availability': availability
            })

        return search_results

    def checkout_books(self, isbn_list, card_no):
        pass

    # def add_schema(self, table_name: str, filepath: str, schema) -> None:
    #     data = pd.read_csv(filepath)
    #     data.to_sql(table_name, con=self.engine,
    #                 if_exists='replace', index=False)
    #     results = self.session.query(schema).all()

    #     self.query_table(schema, results)


def main():
    schema_adder = db_actions('data/books (1).csv', 'data/borrowers (2).csv')
    schema_adder.add_books()
    schema_adder.add_borrowers()


if __name__ == '__main__':
    main()
