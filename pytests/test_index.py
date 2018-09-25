# importing testing framwork
import pytest
# library used to check working virtual environment
import importlib

# importing objects from the jupyter notebook here
from ipynb.fs.full.index import # variable names go here

# format for writing tests
# all functions that are to be run by test suite *must* be prepended with test_
def test_name_of_test_here():
    assert True, "AssertionError will *not* raise and this message will not show"
    assert False, "AssertionError will raise and output this message in the trace"

# tests to ensure correct environment is loaded
def test_conda_environment_activated():
    assert importlib.util.find_spec("obscure"), "It looks like you didn't 'conda activate learn-env' - try that then run the test again!"

def test_boolean_compare():
    assert boolean_compare == False
    assert boolean_compare2 == False

def test_number_compare():
    assert number_compare == True
    assert number_compare2 == True
    assert number_compare3 == False

def test_string_compare():
    assert string_compare == True
    assert string_compare2 == False
    assert string_compare3 == True

def test_list_compare():
    assert list_compare == True
    assert list_compare2 == True
    assert list_compare3 == False
    assert list_compare4 == True
    assert list_compare5 == False

def test_logical_compare():
    assert logical_compare == []
    assert logical_compare2 == True
    assert logical_compare3 == 0
    assert logical_compare4 == 2
    assert logical_compare5 == 2
    assert logical_compare6 == False
    assert logical_compare7 == False

def test_identity_compare():
    assert identity_compare == False
    assert identity_compare2 == True
    assert identity_compare3 == True
    assert identity_compare4 == True
    assert identity_compare5 == False
    assert identity_compare6 == False
