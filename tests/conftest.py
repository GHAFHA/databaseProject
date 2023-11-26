import pytest
from src.db_actions import db_actions
import os


@pytest.fixture
def add_schema_instance():
    # __file__ is a special variable that gets the path of the current file.
    current_directory = os.path.dirname(__file__)

    # Construct absolute path to the CSV files
    filepath_one = os.path.join(
        current_directory, '..', 'data', 'books (1).csv')
    filepath_two = os.path.join(
        current_directory, '..', 'data', 'borrowers (1).csv')

    schema_instance = db_actions(filepath_one, filepath_two)

    return schema_instance
