"""Test the main module."""
from test_package.main import hello

def test_hello():
    """Test the hello function."""
    assert hello() == "Hello from test_package!"
