from src.password_validator import validate_password


def test_valid_password_returns_no_errors():
    result = validate_password("Password99!")
    assert result == {"valid": True, "errors": []}


def test_validator_requires_at_least_8_characters_long():
    result = validate_password("short99")
    assert result == {
        "valid": False,
        "errors": ["Password must be at least 8 characters"],
    }


def test_validator_requires_at_least_2_numbers():
    result = validate_password("Password9")
    assert result == {
        "valid": False,
        "errors": ["The password must contain at least 2 numbers"],
    }
