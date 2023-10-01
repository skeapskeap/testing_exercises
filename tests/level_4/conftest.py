from pathlib import Path
from uuid import uuid4

import pytest


@pytest.fixture
def tg_user_name():
    return "tg_test_user"


@pytest.fixture
def uuid_filename() -> str:
    return str(uuid4())


@pytest.fixture
def create_test_file(uuid_filename):

    def inner(content: str) -> str:
        with Path(uuid_filename).open(mode="w") as file:
            file.write(content)
        return uuid_filename

    try:
        yield inner
    finally:
        Path(uuid_filename).unlink()


@pytest.fixture
def create_test_dir(uuid_filename):

    def inner() -> str:
        Path(uuid_filename).mkdir(exist_ok=True)
        return uuid_filename

    try:
        yield inner
    finally:
        Path(uuid_filename).rmdir()
