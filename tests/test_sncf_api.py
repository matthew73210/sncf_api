from sncf_api import __version__
from sncf_api.sncf_api import sncf_api as sncf

line_code = '903000'

def test_version():
    """Check version"""
    if __version__ != '0.1.0':
        raise AssertionError


def test_cancallclass():
    """Check test method can be called"""
    test = sncf(line_code)
    if not test.test():
        raise AssertionError


def test_connection():
    """Check connection and that API is up"""
    test = sncf(line_code)
    if not test.check_site():
        raise AssertionError


def test_check_list_construction_site():
    """Check method works"""
    test = sncf(line_code)
    if not test.list_construction_site():
        raise AssertionError


def test_convert_to_pandas_db():
    """Check method works"""
    test = sncf(line_code)
    test.list_construction_site()
    a = test.convert_to_pandas_db()
    if a.empty:
        raise AssertionError


def test_list_line_status():
    """Check method works"""
    test = sncf(line_code)
    a = test.list_line_status()
    if a == 0:
        raise AssertionError


def test_list_line_type():
    """Check method works"""
    test = sncf(line_code)
    a = test.list_line_type()
    if a == 0:
        raise AssertionError
