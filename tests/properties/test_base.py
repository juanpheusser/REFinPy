import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.insert(0, path)

import pytest
from src.properties.base import Property

# Fixtures for test data
@pytest.fixture
def valid_location():
    return (40.7128, -74.0060)

@pytest.fixture
def valid_address_dict():
    return {
        "street_number": 123,
        "street_name": "Main St",
        "city": "New York",
        "state": "NY",
        "zip_code": "10001"
    }

@pytest.fixture
def invalid_address_type():
    return [123, "Main St"]  # Example of an invalid type (list)

@pytest.fixture
def address_invalid_keys(valid_address_dict):
    # Create a copy to avoid modifying the fixture for other tests
    address = valid_address_dict.copy()
    address['neighborhood'] = 'Neighborhood 1'
    return address

@pytest.fixture
def address_invalid_value_type(valid_address_dict):
    # Create a copy to avoid modifying the fixture for other tests
    address = valid_address_dict.copy()
    address["street_number"] = "123A"  # String instead of int
    return address

# Individual tests for specific scenarios
def test_initialization_with_valid_data(valid_location, valid_address_dict):
    prop = Property(name="Test Property", location=valid_location, address=valid_address_dict)
    assert prop.name == "Test Property"
    assert prop.location == valid_location
    assert prop.address == valid_address_dict

def test_initialization_missing_optional():
    prop = Property(name="Basic Property") 
    assert prop.name == "Basic Property"
    assert prop.address is None
    assert prop.location is None

def test_invalid_name(valid_location, valid_address_dict):
    with pytest.raises(TypeError):
        Property(name=123, location=valid_location, address=valid_address_dict)

def test_invalid_location_type(valid_address_dict):
    with pytest.raises(TypeError):
        Property(name="Test Property", location="Not a tuple", address=valid_address_dict)

def test_invalid_location_values(valid_address_dict):
    with pytest.raises(ValueError):
        Property(name="Test Property", location=(200, 90), address=valid_address_dict)  # Latitude out of range

def test_invalid_address_type(invalid_address_type):
    with pytest.raises(TypeError):
        Property(name="Test Property", address=invalid_address_type)

def test_address_invalid_keys(address_invalid_keys):
    with pytest.raises(ValueError):
        Property(name="Test Property", address=address_invalid_keys)

def test_address_invalid_value_type(address_invalid_value_type):
    with pytest.raises(ValueError):
        Property(name="Test Property", address=address_invalid_value_type)