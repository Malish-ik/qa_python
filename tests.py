import pytest

import data

from main import BooksCollector


class TestBooksCollector:
    @pytest.mark.parametrize('books', data.books_wo_genre)
    def test_add_new_book_add_two_books(self, books):
        collector = BooksCollector()

        for book in books:
            collector.add_new_book(book)

        assert len(collector.get_books_genre()) == 2

    def test_set_book_and_book_genre(self, collector):
        assert len(collector.get_books_genre()) == 6

    def test_get_book_genre(self, collector):
        assert collector.get_book_genre(
            'Что делать, если ваш кот хочет вас убить') == 'Детективы'

    def test_get_book_w_specific_genre(self, collector):
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_for_children(self, collector):
        assert len(collector.get_books_for_children()) == 3

    def test_add_get_books_in_favorites(self, collector_w_favorites):
        assert len(collector_w_favorites.get_list_of_favorites_books()) == 4

    def test_delete_book_from_favorites(self, collector_w_favorites):
        for name in data.delete_book_from_favorites:
            collector_w_favorites.delete_book_from_favorites(name)
        assert len(collector_w_favorites.get_list_of_favorites_books()) == 2
