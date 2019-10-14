import pytest
import pandas as pd 

@pytest.mark.example_1
def test_if_list(conftest_list):
#   assert that the variable(arguement) is infact a list object.
    assert isinstance(conftest_list, list), "friends is not of type list"


@pytest.mark.example_1
def test_length(conftest_list):
#   assert that the dictionary is 3 elements long
    assert len(conftest_list) == 3, "This doesn't have 3 keys"

@pytest.mark.example_2
def test_function(conftest_function, conftest_list):
#   assert that function exists
    assert conftest_function, "You don't have a function called capitalize"
    
#   assert that the last name is uppercase.
    assert ~conftest_function(conftest_list)[0].islower()
    