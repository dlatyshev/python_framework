import pytest


@pytest.mark.parametrize("test_input", [1, 2, 3])
def test_one_2(test_input):
    print(test_input)


@pytest.mark.parametrize("test_input", [1, 2, 3])
class TestClassParameterized:

    def test_one(self, test_input):
        pass

    def test_two(self, test_input):
        pass
