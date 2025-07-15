import pytest

from main import BooksCollector

@pytest.fixture()
def collector() -> BooksCollector:

    return BooksCollector()

def test_collections_are_empty_at_start(collector):
    assert collector.get_books_genre() == {}
    assert collector.get_list_of_favorites_books() == []

@pytest.mark.parametrize("title", ["Zorro", "Астерикс и Обеликс"])
def test_add_new_book_positive(collector, title):
    collector.add_new_book(title)
    assert title in collector.get_books_genre()
    assert collector.get_book_genre(title) == ""


@pytest.mark.parametrize(
    "bad_title",
    [
        "",  # пустая строка
        "Очень-очень длинное название книги, выходящее за 40 символов "
        "и потому не проходящее по условию проверки",
    ],
)
def test_add_new_book_rejects_invalid_titles(collector, bad_title):
    collector.add_new_book(bad_title)
    assert bad_title not in collector.get_books_genre()


# ---------- set_book_genre ----------

def test_set_book_genre_happy_path(collector):
    collector.add_new_book("Пирамидо-сосковая война")
    collector.set_book_genre("Пирамидо-сосковая война", "Детективы")
    assert collector.get_book_genre("Пирамидо-сосковая война") == "Детективы"


@pytest.mark.parametrize(
    "name, genre, expected_genre_after_call",
    [
        # книга есть, жанр неверный
        ("Кучерявая вилка", "Народный эпос", ""),
        # книги нет, жанр валидный
        ("Несуществующая книга", "Фантастика", None),
    ],
)
def test_set_book_genre_negative(collector, name, genre, expected_genre_after_call):
    if name != "Несуществующая книга":
        collector.add_new_book(name)          # создаём только в первом сценарии

    collector.set_book_genre(name, genre)
    assert collector.get_book_genre(name) == expected_genre_after_call


# ---------- get_books_with_specific_genre ----------

def test_get_books_with_specific_genre_returns_correct_list(collector):
    pairs = [
        ("Головочёс", "Мультфильмы"),
        ("Убийца Акамэ", "Детективы"),
        ("Брюквенный вождь", "Мультфильмы"),
    ]
    for name, genre in pairs:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

    expected = {"Головочёс", "Брюквенный вождь"}
    result = set(collector.get_books_with_specific_genre("Мультфильмы"))
    assert result == expected


def test_get_books_with_specific_genre_unknown_genre_returns_empty(collector):
    assert collector.get_books_with_specific_genre("Неизвестный жанр") == []


# ---------- get_books_for_children ----------

def test_get_books_for_children_filters_adult_genres(collector):
    data = [
        ("Дюймовочка", "Мультфильмы"),   # детское
        ("Снежная королева", "Ужасы"),   # взрослое
        ("Славянский дебош", "Комедии"), # детское
        ("Дед хейтит внуков", "Детективы"),  # взрослое
    ]
    for name, genre in data:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

    children_books = set(collector.get_books_for_children())
    assert children_books == {"Дюймовочка", "Славянский дебош"}
    assert all(
        collector.get_book_genre(b) not in collector.genre_age_rating
        for b in children_books
    )

# ---------- favorites ----------

def test_add_book_in_favorites_adds_once(collector):
    collector.add_new_book("Исподвольный кабачок")

    collector.add_book_in_favorites("Исподвольный кабачок")
    collector.add_book_in_favorites("Исподвольный кабачок")

    favs = collector.get_list_of_favorites_books()
    assert favs == ["Исподвольный кабачок"]


def test_add_book_in_favorites_ignores_unknown_book(collector):
    collector.add_book_in_favorites("Кошачья мягковость")
    assert collector.get_list_of_favorites_books() == []


def test_delete_book_from_favorites(collector):
    collector.add_new_book("Урюк в компоте")
    collector.add_book_in_favorites("Урюк в компоте")

    collector.delete_book_from_favorites("Урюк в компоте")
    assert "Урюк в компоте" not in collector.get_list_of_favorites_books()


def test_delete_book_from_favorites_unknown_title_is_noop(collector):
    collector.add_new_book("Бражконос")
    collector.add_book_in_favorites("Бражконос")

    collector.delete_book_from_favorites("Несуществующая книга")
    assert collector.get_list_of_favorites_books() == ["Бражконос"]

        books_collector.add_book_in_favorites('Внезапная голова')
        books_collector.delete_book_from_favorites('Внезапная голова')

        assert not books_collector.get_list_of_favorites_books()
