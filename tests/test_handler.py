import pytest
from sqlalchemy import inspect
from models.models import Book, Borrower


def test_parser(add_schema_instance):
    df_one, df_two = add_schema_instance.parse_csv()
    assert not df_one.empty
    assert not df_two.empty
    print(df_one.head())
    print(df_two.head())


def test_add_borrowers(add_schema_instance):
    results = add_schema_instance.add_borrowers()
    assert len(results) == 1000
    print(results[0])


def test_add_books(add_schema_instance):
    results = add_schema_instance.add_books()
    assert len(results) == 25000
    print(results[0])


def test_add_avail(add_schema_instance):
    assert add_schema_instance.add_avail() is True


def test_search_books(add_schema_instance):
    pass


def test_checkout_books(add_schema_instance):
    pass


# def test_add_schema(add_schema_instance):
#     # Use the fixture to call add_schema
#     results = add_schema_instance.add_schema(
#         'books', 'data/books (1).csv', Book)
#     assert len(results) == 1000  # Add assertions as needed
#     print(results[0])  # Print the first row of the results
