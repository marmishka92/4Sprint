import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def books_collector():
    books_collector = BooksCollector()

    return books_collector
