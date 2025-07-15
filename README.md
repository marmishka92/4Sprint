## Описание тестовых функций для класса *BooksCollector*

### Создание объекта вынесено фикстурой в конфтест


1. Проверяет словари конструктора при создании объекта
```
    def test_books_genre_fav_dict_is_empty(self, books_collector):

        assert len(books_collector.books_genre) == 0 and len(books_collector.favorites) == 0
```
---

2. Проверяет что у созданного объекта есть заполненный список с жанрами
```
    def test_genre_list_is_not_empty(self, books_collector):

        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
```
---
3. Проверяет что у созданного объекта есть список с жанрами 18+

```
    def test_genre_age_rating_list_is_not_empty(self, books_collector):

        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']        
```
---
4. Тест с параметризацией проверяет добавление новых книг в список 
```
    @pytest.mark.parametrize('book', ['Zorro', 'Астерикс и Обеликс'])
    def test_add_new_book_positive(self, books_collector, book):

        books_collector.add_new_book(book)
        assert books_collector.books_genre[book] == ''
```
---
5. Тест проверяет что книги с названиями 40+ символов не будут добавлены в список книг
```
    @pytest.mark.parametrize('book', ['', 'Как левша подковал блоху, съездил в Париж и проглотил волшебные бобы'])
    def test_add_new_book_more_negative_sizes(self, books_collector, book):

        assert not books_collector.add_new_book(book)
```
---
6. Тест с параметризацией добавляет новые книги и проверяет задавание книгам жанров
```
    @pytest.mark.parametrize('name, genre', [
        ['Пирамидо-сосковая война', 'Детективы'],
        ['Мастер и Минотавр', 'Ужасы']
])
    def test_set_book_genre_valid_name(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.books_genre[name] == genre
```
---
7. Тест проверяет задавание книгам с невалидными значениями жанра. 
Создается список из добавленных книг, где первая не добавляется из-за размера,
а вторая добавляется, но имеет для задавания невалидный жанр.
```
    @pytest.mark.parametrize('name, genre', [
        ['Вторая пуническая война Тутанхамона Новоблагословенного', 'Детективы'],
        ['Близорукая увертюра', 'Народный эпос ']
    ])
    def test_set_book_genre_negative_case(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        assert not books_collector.set_book_genre(name, genre)

```
---
8. Тест проверяет возвращение жанра книги по названию
Добавляется книга, задается жанр. Проверяется что по названию возвращается жанр.
```
    def test_get_book_genre_return_valid_name(self, books_collector):

        books_collector.add_new_book('Иерархиус')
        books_collector.set_book_genre('Иерархиус', 'Фантастика')
        assert books_collector.get_book_genre('Иерархиус') == 'Фантастика'
```
---
9. Тест проверяет что выводится список книг по определенным жанрам.
Добавляется книга, задается жанр, проверяется жанр и проверяется что отдается список
```
    def test_get_books_with_specific_genre_when_valid_genre(self, books_collector):

        books_collector.add_new_book('Головочёс')
        books_collector.set_book_genre('Головочёс', 'Мультфильмы')
        assert books_collector.get_books_with_specific_genre('Мультфильмы') \
               and type(books_collector.get_books_with_specific_genre('Мультфильмы')) == list

```
---
10. Тест проверяет что нельзя получить список по определенному жанру, если список пустой или жанр невалидный.
Через параметризацию добавляем книги и пробуем получить по жанру список
```
    @pytest.mark.parametrize('name, genre', [['', 'Фантастика'], ['Бирманский', 'Комедии']])
    def test_get_books_with_specific_genre_empty_list_book_false_genre(self, books_collector, name, genre):

        books_collector.add_new_book(name)
        assert not books_collector.get_books_with_specific_genre('Шутёхи')

```
---
11. Тест проверяет что в список добавились все книги и что все они помещаются в словарь.
Циклом добавляем книги, в переменную кладем рандомное название книги и проверяем.
```
    def test_get_books_genre_filled_dict(self, books_collector):

        books = ['Торадора', 'Закупяченский движ', 'Суета на ферме', 'Огорошен и ладно']
        for name in books:
            books_collector.add_new_book(name)

        random_book = random.choice(books)
        assert random_book in books_collector.get_books_genre() \
            and type(books_collector.get_books_genre()) == dict

```
---
12. Тест проверяет что нельзя получить пустой список
```
    def test_get_books_genre_empty_dict(self, books_collector):

        assert not books_collector.get_books_genre()

```
---
13. Тест проверяет что в списке с книгами есть только книги с рейтингом для детей.
Циклом создаем список и добавляем всем книгам разные жанры.
Вторым циклом проверяем есть ли в первом списке жанры 18+
```
    def test_get_books_for_children_correct_genre(self, books_collector):

        books = ['Бивнеглазый', 'Кучерявая вилка', 'Дуремар', 'Брюквенный вождь', 'Окрест']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre[x])
            x += 1

        for rating in books_collector.genre_age_rating:
            assert rating not in books_collector.get_books_for_children()

```
---
14. Тест проверяет что книги с рейтингом жанров 18+ не попадают в список книг для детей.
Циклом добавляем книги и задаем им жанры 18+, далее ассертим.
```
    def test_get_books_for_children_adult_rating(self, books_collector):

        books = ['Дюймовочка', 'Снежная королева']
        x = 0
        for name in books:
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, books_collector.genre_age_rating[x])
            x += 1

        assert not books_collector.get_books_for_children()

```
---
15. Тест проверяет что книга добавленная в избранное есть в избранном 
Циклом добавляем книги в список, затм добавляем одну книгу по названию в избранное и ассертим СПИСОК ИЗБРАННОГО
```
    def test_add_book_in_favorites_when_books_in_list(self, books_collector):

        books = ['Исподвольный кабачок', 'Блич', 'Камень супа', 'Уругвайский лилии']
        for name in books:
            books_collector.add_new_book(name)
        books_collector.add_book_in_favorites('Исподвольный кабачок')

        assert 'Исподвольный кабачок' in books_collector.favorites

```
---
16. Тест проверяет что нельзя добавить книгу в избранное, если её нет в списке книг.
Циклом добавляем книги в список, затем все их добавляем в избранное, ассертим добавление незнакомой книги.
```
    def test_add_book_in_favorites_when_book_not_in_list(self, books_collector):

        books = ['Воркователь иглу', 'Горячий слух', 'Бражконос']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert not books_collector.add_book_in_favorites('Кошачья мягковость')

```
---
17. Тест проверяет удаление книги из избранного.
Циклом добавляем книги в список, затем добавляем всех в избранное и удаляем книгу по названию.
В заключении ассертим удаление книги из списка избранного
```
    def test_delete_book_from_favorites(self, books_collector):

        books = ['Брокер на кухне', 'Вольная', 'Убийца Акамэ']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        books_collector.delete_book_from_favorites('Брокер на кухне')
        assert 'Брокер на кухне' not in books_collector.favorites

```
---
18. Тест проверяет удаление книги, которой в избранном нет.
Циклом добавляем книги в список, затем добавляем  всех в избранное.
Ассертим попытку удаления несуществующей книги.
```
    def test_delete_book_from_favorites_no_name_in_list(self, books_collector):

        books = ['Борхес', 'Бобовоз', 'Урюк в компоте']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert not books_collector.delete_book_from_favorites('Комплаенс в Слизерин')

```
---
19. Тест проверяет метод который возвращает список избранных книг.
Циклом добавляем книги в список, затем добавляем  всех в избранное.
Ассертим получение списка.
```
    def test_get_list_of_favorites_books_not_empty(self, books_collector):

        books = ['Славянский дебош', 'Кринж в посёлке', 'Дед хейтит внуков']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert books_collector.get_list_of_favorites_books()
```
---
20. Тест проверяет что после удаления единственной книги из списка избранного, 
метод получения списка избранного вернет пустой список.
Добавляем книгу, зате добавляем её в избранное и удаляем из избранного.
Ассертим метод.
```
        def test_get_list_of_favorites_books_empty_list(self, books_collector):

        books_collector.add_new_book('Внезапная голова')
        books_collector.add_book_in_favorites('Внезапная голова')
        books_collector.delete_book_from_favorites('Внезапная голова')
        
        assert not books_collector.get_list_of_favorites_books()

```
---
