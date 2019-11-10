
import pytest
import unittest
import os
import shutil

from foo import cuad, store

def test_simple():
    r = cuad(3)
    assert r == 9

def test_zero():
    r = cuad(0)
    assert r == 0

def test_negative():
    r = cuad(-3)
    assert r == 9

def test_complex():
    r = cuad(3j)
    assert r == -9

def test_char():
    with pytest.raises(TypeError) as err:
        cuad("a")
    assert str(err.value) == "Solo nros"


@pytest.fixture
def tempdir():
    os.mkdir("/tmp/temp")
    yield "/tmp/temp"
    shutil.rmtree("/tmp/temp")


def test_zero_store(tempdir):
    path = os.path.join(tempdir, "testarch")
    store(0, path)
    assert not os.path.exists(path)

def test_store_simple(tempdir):
    store(7, "/tmp/temp/testarch")
    with open("/tmp/temp/testarch", "rt", encoding='ascii') as fh:
        data = fh.read()
    assert int(data) == 7

def test_bignum(tempdir):
    bignum = 123 ** 123
    store(bignum, "/tmp/temp/testarch")
    with open("/tmp/temp/testarch", "rt", encoding='ascii') as fh:
        data = fh.read()
    assert int(data) == bignum

