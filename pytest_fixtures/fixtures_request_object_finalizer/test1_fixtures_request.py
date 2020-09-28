import pytest


@pytest.fixture
def first_fixture_for_request(request):
    print("-" * 10)
    print(f"{request.node}")
    print(f"{request.scope}")
    print(f"{request.cls}")
    print(f"{request.module}")


def test_one(first_fixture_for_request):
    print(f"\n Print from test one")


class TestClass:

    def test_one_class(self, first_fixture_for_request):
        print(f"\n Print from test_one_class")
