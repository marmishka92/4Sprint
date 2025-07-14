import random
import pytest


class TestBooksCollector:

    def test_books_genre_fav_dict_is_empty(self, books_collector):

        assert len(books_collector.books_genre) == 0 and len(books_collector.favorites) == 0

    def test_genre_list_is_not_empty(self, books_collector):

        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_list_is_not_empty(self, books_collector):

        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('book', ['Zorro', 'Астерикс и Обеликс'])
    def test_add_new_book_positive(self, books_collector, book):

        books_collector.add_new_book(book)
        assert books_collector.books_genre[book] == ''

    @pytest.mark.parametrize('book', ['', 'Как левша подковал блоху, съездил в Париж и проглотил волшебные бобы'])
    def test_add_new_book_more_negative_sizes(self, books_collector, book):

        assert not books_collector.add_new_book(book)

    def test_set_book_genre_valid_name(self, books_collector):

        books_collector.add_new_book('Пирамидо-сосковая война')
        books_collector.set_book_genre('Пирамидо-сосковая война', 'Детективы')
        assert books_collector.books_genre['Пирамидо-сосковая война'] == 'Детективы'

    @pytest.mark.parametrize('name, genre', [
        ['Вторая пуническая война Тутанхамона Новоблагословенного', 'Детективы'],
        ['Близорукая увертюра', 'Народный эпос ']
    ])
    def test_set_book_genre_negative_case(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        assert not books_collector.set_book_genre(name, genre)

    def test_get_book_genre_return_valid_name(self, books_collector):

        books_collector.add_new_book('Иерархиус')
        books_collector.set_book_genre('Иерархиус', 'Фантастика')
        assert books_collector.get_book_genre('Иерархиус') == 'Фантастика'

    def test_get_books_with_specific_genre_when_valid_genre(self, books_collector):

        books_collector.add_new_book('Головочёс')
        books_collector.set_book_genre('Головочёс', 'Мультфильмы')
        assert books_collector.get_books_with_specific_genre('Мультфильмы') \
               and type(books_collector.get_books_with_specific_genre('Мультфильмы')) == list

    @pytest.mark.parametrize('name, genre', [['', 'Фантастика'], ['Бирманский', 'Комедии']])
    def test_get_books_with_specific_genre_empty_list_book_false_genre(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        assert not books_collector.get_books_with_specific_genre('Шутёхи')

    def test_get_books_genre_filled_dict(self, books_collector):

        books = ['Торадора', 'Закупяченский движ', 'Суета на ферме', 'Огорошен и ладно']
        for name in books:
            books_collector.add_new_book(name)

        random_book = random.choice(books)
        assert random_book in books_collector.get_books_genre() \
            and type(books_collector.get_books_genre()) == dict

    def test_get_books_genre_empty_dict(self, books_collector):

        assert not books_collector.get_books_genre()

    def test_get_books_for_children_correct_genre(self, books_collector):

        books = ['Бивнеглазый', 'Кучерявая вилка', 'Дуремар', 'Брюквенный вождь', 'Окрест']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre[x])
            x += 1

        for rating in books_collector.genre_age_rating:
            assert rating not in books_collector.get_books_for_children()

    def test_get_books_for_children_adult_rating(self, books_collector):

        books = ['Дюймовочка', 'Снежная королева']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre_age_rating[x])
            x += 1

        assert not books_collector.get_books_for_children()

    def test_add_book_in_favorites_when_books_in_list(self, books_collector):

        books_collector.add_new_book('Исподвольный кабачок')
        books_collector.add_book_in_favorites('Исподвольный кабачок')

        assert 'Исподвольный кабачок' in books_collector.favorites

    def test_add_book_in_favorites_when_book_not_in_list(self, books_collector):

        books = ['Воркователь иглу', 'Горячий слух', 'Бражконос']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert not books_collector.add_book_in_favorites('Кошачья мягковость')

    def test_delete_book_from_favorites(self, books_collector):

        books_collector.add_new_book('Убийца Акамэ')
        books_collector.add_book_in_favorites('Убийца Акамэ')

        books_collector.delete_book_from_favorites('Убийца Акамэ')
        assert 'Убийца Акамэ' not in books_collector.favorites

    def test_delete_book_from_favorites_no_name_in_list(self, books_collector):

        books_collector.add_new_book('Урюк в компоте')
        books_collector.add_book_in_favorites('Урюк в компоте')

        assert not books_collector.delete_book_from_favorites('Комплаенс в Слизерин')

    def test_get_list_of_favorites_books_not_empty(self, books_collector):

        books = ['Славянский дебош', 'Кринж в посёлке', 'Дед хейтит внуков']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert books_collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty_list(self, books_collector):

        books_collector.add_new_book('Внезапная голова')
        books_collector.add_book_in_favorites('Внезапная голова')
        books_collector.delete_book_from_favorites('Внезапная голова')

        assert not books_collector.get_list_of_favorites_books()
