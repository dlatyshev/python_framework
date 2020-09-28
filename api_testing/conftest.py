import pytest
import requests


class ApiClient:

    def __init__(self, url):
        self.base_url = url

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_url + path
        return requests.post(url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        return requests.get(url=self.base_url + path, params=params)


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://www.google.com",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return ApiClient(base_url)
