from typing import Union

class Property:
    """
    Represents a generic real estate property and its basic information
    """
    def __init__(self, name: str = None, address: Union[str, dict] = None, location: tuple[float, float] = None):
        
        """
        Initializes a Property object.

        Args:
            name (str, optional): The name of the property.
            address (str or dict, optional): The address of the property. Can be given as a string or as a dictionary with the following structure;

                    address = {
                        "street_number": int,
                        "street_name": str,
                        "unit_number": int,
                        "city": str,
                        "state": str,
                        "province": str,
                        "region": str,
                        "zip_code": str,
                        "country": str
                    }

            location (float, optional): A tuple containing the (latitude, longitude) of the property.
        """

        self._validate_and_assign(name, "name", str)
        self._validate_address(address)
        self._validate_location(location)


    def _validate_and_assign(self, value, name, expected_type, positive=False):
        """
        Validates the given value and assigns it to the corresponding attribute.

        Args:
            value: The value to be assigned to the attribute.
            name (str): The name of the attribute.
            expected_type (type): The expected data type of the value.
            positive (bool, optional): If True, enforces that the value must be positive. Defaults to False.

        Raises:
            TypeError: If the value is not of the expected type.
            ValueError: If the 'positive' flag is set and the value is not positive.
        """

        if not isinstance(value, expected_type) and value is not None:
            raise TypeError(f"{name} must be of type {expected_type}")
        if positive and value <= 0:
            raise ValueError(f"{name} must be positive")
        setattr(self, name, value)


    def _validate_location(self, location: tuple[float, float]):
        """
        Validates the location attribute and assigns it if all checks pass.

        Args:
            location: The proposed location value.

        Raises:
            TypeError: If the location is not a tuple of length 2 or doesn't contain numeric values.
            ValueError: If the latitude or longitude values are outside the valid range.
        """

        if location is None:
            self.location = None  # Assign None if location is optional

        if not isinstance(location, tuple) or len(location) != 2:
            raise TypeError("Location must be a tuple of length 2")

        try:
            lat, lon = location
            float(lat)  
            float(lon)  
        except (ValueError, TypeError) as exc:
            raise ValueError("Location tuple must contain two numeric values") from exc

        if not (-90 <= lat <= 90):
            raise ValueError("Invalid latitude. Must be between -90 and 90")
        if not (-180 <= lon <= 180):
            raise ValueError("Invalid longitude. Must be between -180 and 180")

        # All checks passed!
        self.location = location 

        
    def _validate_address(self, address):
            """
            Validates the address attribute.

            Args:
                address: The proposed address value.

            Raises:
                TypeError: If the address is not a string or dictionary.
                ValueError: If the address dictionary has invalid keys or value types.
            """

            valid_address_keys = {
                "street_number": int,
                "street_name": str,
                "unit_number": int,  
                "city": str,
                "state": str,
                "province": str,
                "region": str,
                "zip_code": str,
                "country": str
            }

            if isinstance(address, str):
                # Basic validation if only a street address string is provided
                pass  
            elif isinstance(address, dict):
                # Validate the dictionary structure
                if not set(address.keys()).issubset(valid_address_keys):
                    raise ValueError("Address dictionary contains invalid keys")

                # Validate value types
                for key, expected_type in valid_address_keys.items():
                    if key in address and not isinstance(address[key], expected_type):
                        raise ValueError(f"Invalid type for address key '{key}'. Expected: {expected_type}")
            else:
                raise TypeError("Address must be either a string or a dictionary")
            

