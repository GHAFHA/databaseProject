import pytest
from sqlalchemy import inspect
from models.Models import Book, Borrower


def test_add_borrowers(add_schema_instance):
    results = add_schema_instance.add_borrowers()
    assert len(results) == 1000
    print(results[0])


def test_add_books(add_schema_instance):
    results = add_schema_instance.add_books()
    assert len(results) == 25000
    print(results[0])


def test_add_loans(add_schema_instance):
    assert add_schema_instance.add_loans() is True


def test_add_avail(add_schema_instance):
    assert add_schema_instance.add_avail() is True


def test_add_new_borrower(add_schema_instance):
    # Create a new Borrower instance with test data
    test_borrower = Borrower(
        ID0000id="test",
        ssn="123-45-6789",
        first_name="John",
        last_name="Doe",
        email="johndoe@example.com",
        address="123 Test St",
        city="Testville",
        state="TS",
        phone="123-456-7890"
    )

    # Add the borrower to the database
    add_schema_instance.session.add(test_borrower)
    add_schema_instance.session.commit()

    # Retrieve the borrower to verify addition
    retrieved_borrower = add_schema_instance.session.query(
        Borrower).filter_by(ID0000id="test").first()

    assert retrieved_borrower is not None
    assert retrieved_borrower.first_name == "John"
    assert retrieved_borrower.last_name == "Doe"

    # Cleanup - remove the test borrower
    add_schema_instance.session.delete(retrieved_borrower)
    add_schema_instance.session.commit()
