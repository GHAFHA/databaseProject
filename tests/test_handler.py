import pytest
from sqlalchemy import inspect
from models.Models import Book, Borrower


def test_create_table(add_schema_instance):
    add_schema_instance.create_tables()
    inspector = inspect(add_schema_instance.engine)
    assert inspector.has_table('book_loans') is True


def test_add_loans(add_schema_instance):
    assert add_schema_instance.add_loans() is True


def test_add_avail(add_schema_instance):
    assert add_schema_instance.add_book_avail() is True
