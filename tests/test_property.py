import pytest
from REFinPy.property import Property 

@pytest.fixture
def valid_location():
    return (40.7128, -74.0060)  


def test_initialization_with_valid_data():
    my_property = Property(name="Test Property", purchase_price=150000, 
                           market_value=200000, property_type="Single Family",
                           address="123 Main St", location=valid_location())

    assert my_property.name == "Test Property"
    assert my_property.purchase_price == 150000

def test_initialization_missing_optional():
    my_property = Property(name="Basic Property") 
    assert my_property.purchase_price is None

def test_invalid_price():
    with pytest.raises(ValueError):
        Property(purchase_price=-5000) 

def test_invalid_location_type():
    with pytest.raises(TypeError):
        Property(location="Not a tuple")

def test_invalid_location_values():
    with pytest.raises(ValueError):
        Property(location=(200, 90))  # Latitude out of range 

# ... Add tests for _validate_address. You might need additional fixtures
#     to create valid and invalid address dictionaries. 
