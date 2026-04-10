import json
from function_app import validate_submission


def test_validate_all_fields_present():
    """All fields with valid values should pass."""
    data = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "id": "ABC123",
        "phone": "1234567890",
    }
    is_valid, errors = validate_submission(data)
    assert is_valid is True
    assert errors == {}


def test_validate_missing_name():
    """Missing name should fail."""
    data = {
        "name": "",
        "email": "jane@example.com",
        "id": "ABC123",
        "phone": "1234567890",
    }
    is_valid, errors = validate_submission(data)
    assert is_valid is False
    assert "name" in errors


def test_validate_invalid_email():
    """Invalid email should fail."""
    data = {
        "name": "Jane Doe",
        "email": "not-an-email",
        "id": "ABC123",
        "phone": "1234567890",
    }
    is_valid, errors = validate_submission(data)
    assert is_valid is False
    assert "email" in errors


def test_validate_missing_phone():
    """Missing phone should fail."""
    data = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "id": "ABC123",
        "phone": "",
    }
    is_valid, errors = validate_submission(data)
    assert is_valid is False
    assert "phone" in errors
