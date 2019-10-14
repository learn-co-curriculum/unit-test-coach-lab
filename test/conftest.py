import pytest
from example_index import friends, capitalize

@pytest.fixture
def conftest_list():
    return friends

@pytest.fixture
def conftest_function():
    return capitalize