import pytest

import data

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    for name, genre in data.books_with_genres.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector


@pytest.fixture
def collector_w_favorites(collector):
    for name in data.book_in_favorites:
        collector.add_book_in_favorites(name)
    return collector
