import pytest

from config import config_from_json


@pytest.fixture(scope="session")
def config_data():
    return config_from_json("conf.json", read_from_file=True)
