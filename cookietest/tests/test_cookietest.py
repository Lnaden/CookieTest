"""
Unit and regression test for the cookietest package.
"""

# Import package, test suite, and other packages as needed
import cookietest
import pytest
import sys

def test_cookietest_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "cookietest" in sys.modules
