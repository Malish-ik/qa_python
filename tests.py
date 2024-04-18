import pytest
from main import BooksCollector


class TestBooksCollector:

    books_wo_genre = [
        [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить'
        ],
        [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить',
            'Гордость и предубеждение и зомби',  # дубликат
            'Что делать, если ваш кот хочет вас убить'  # дубликат
        ],
        [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить',
            'Гордость и предубеждение и зомби Гордость и предубеждение и зомби',  # строка более 41 символа
        ]
    ]

    books_with_genres = {
        'Гордость и предубеждение и зомби': 'Ужасы',
        'Что делать, если ваш кот хочет вас убить': 'Детективы',
        'Доллар за 35 рублей': 'Фантастика',
        'Просто мультик': 'Мультфильмы',
        'Популярно о зарплате': 'Комедии',
        'Просто Фредди': 'Ужасы'
    }

    book_in_favorites = [
        'Доллар за 35 рублей',
        'Просто мультик',
        'Популярно о зарплате',
        'Что делать, если ваш кот хочет вас убить',
        'Просто мультик',  # дубликат
    ]

    delete_book_from_favorites = [
        'Просто мультик',
        'Популярно о зарплате',
        'Просто мультик',  # дубликат
    ]

    @pytest.fixture
    def collector(self):
        collector = BooksCollector()
        for name, genre in self.books_with_genres.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        return collector

    @pytest.fixture
    def collector_w_favorites(self, collector):
        for name in self.book_in_favorites:
            collector.add_book_in_favorites(name)
        return collector

    @pytest.mark.parametrize('books', books_wo_genre)
    def test_add_new_book_add_two_books(self, books):
        collector = BooksCollector()

        for book in books:
            collector.add_new_book(book)

        assert len(collector.books_genre) == 2

    def test_set_book_and_book_genre(self, collector):
        assert len(collector.books_genre) == 6

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
        for name in self.delete_book_from_favorites:
            collector_w_favorites.delete_book_from_favorites(name)
        assert len(collector_w_favorites.get_list_of_favorites_books()) == 2
