from src.password_validator import validate_password


def test_valid_password_returns_no_errors():
    result = validate_password("Password99!")
    assert result == {"valid": True, "errors": []}


def test_validator_requires_at_least_8_characters_long():
    result = validate_password("Pas99!")
    assert result == {
        "valid": False,
        "errors": ["Password must be at least 8 characters"],
    }


def test_validator_requires_at_least_2_numbers():
    result = validate_password("Password9!")
    assert result == {
        "valid": False,
        "errors": ["The password must contain at least 2 numbers"],
    }


def test_validator_handles_multiple_errors():
    result = validate_password("Pass9!")
    assert result == {
        "valid": False,
        "errors": [
            "Password must be at least 8 characters",
            "The password must contain at least 2 numbers",
        ],
    }


def test_validator_requires_at_least_one_capital_letter():
    result = validate_password("password99!")
    assert result == {
        "valid": False,
        "errors": ["password must contain at least one capital letter"],
    }


def test_validator_requires_at_least_one_special_char():
    result = validate_password("Password99")
    assert result == {
        "valid": False,
        "errors": ["password must contain at least one special character"],
    }
