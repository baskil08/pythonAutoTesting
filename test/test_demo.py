import pytest

@pytest.fixture()
def before_after():
    print("Before test")
    yield  None
    print("\nAfter test")


def test_demo():
    assert 1 == 1

def test_demo2(before_after):
    assert 1 == 1