import pytest


# @pytest.fixture
# def first_fixture():
#     print("Print from first fixture")


def test_one(first_fixture):
    pass


class TestFunction:

    def test_from_test_class_one(self, first_fixture):
        pass

    def test_from_test_class_two(self, first_fixture):
        pass
