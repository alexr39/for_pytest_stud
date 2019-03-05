import pytest

def setup_module(module):
    pass


def teardown_module(midule):
    pass

def test_upper():
    assert 'foo'.upper() == 'FOO'

def test_isupper():
    assert 'FOO'.isupper()

def test_faild_upper():
    assert 'foo'.upper() == 'FOo'