# Импорты из стандартной библиотеки:
import random
import json

# Импорты сторонних библиотек:
import faker

# Импорты модулей текущего проекта:
from conf import MODEL


def pk(start: int = 1) -> int:
    """
    Функция генератор возвращающая счетчик, который увеличивается на единицу при каждом вызове функции.
    :param start: начальное значение счетчика.
    :return: значение счетчика.
    """
    yield start
    while True:
        start += 1
        yield start


def title() -> str:
    """
    Функция читающая файл books.txt и берущая из него рандомное наименование книги.
    :return: наименовании кники.
    """
    with open("books.txt", "r", encoding="utf-8") as f:
        book = random.choice(f.read().splitlines())
    return book


def year() -> int:
    """
    Функция генерирующая случайный год в дипозоне от 2000 до 2022 годов.
    :return: случайный год.
    """
    year = random.choice(range(2000, 2022))
    return year


def pages() -> int:
    """
    Функция генерирующая случайную страницу книги в дипозоне от 1 до 500.
    :return: слуайная страница.
    """
    pages = random.choice(range(1, 500))
    return pages


def isbn13() -> str:
    """
    Функция генерирующая международный стандартный книжный номер при помщи модуля Faker.
    :return: случайный книжный номер.
    """
    fake = faker.Faker()
    for _ in range(101):
        return fake.isbn10()


def rating() -> float:
    """
    Функция генерирующая рандомный рейтинг книги, являющийся числом с плавающей запятой в диапозоне от 0 до 5.
    :return: рейтинг книги
    """
    rating = (round(random.uniform(0, 5), 1) for x in range(5))
    return next(rating)

def price() -> float:
    """
    Функция генерирующая цену книги, являющаяся числом с плавающей запятой в диапозоне от 0 до 2000.
    :return: цена книги
    """
    price = (round(random.uniform(0, 2000), 1) for x in range(100))
    return next(price)


def author() -> list[str]:
    """
    Функция генерирующая список авторов при помщи модуля Faker. Содержит от 1 до 3 авторов.
    :return: список авторов
    """
    fake = faker.Faker()
    return [fake.name() for _ in range(random.randint(1, 3))]

def get_dict(start: int = 1) -> dict[dict]:
    """
    Функция генератор возвращающая словарь со всеми данными книги.
    :param start: начальное значение счетчика.
    :return: словарь с данными о книгах
    """
    gen_pk = pk(start)
    while True:
        yield {"model": MODEL, "pk": next(gen_pk), "fields": {"title": title(), "year": year(), "pages": pages(),
                                                              "isbn13": isbn13(), "rating": rating(), "price": price(),
                                                              "author": author()}}

def main() -> None:
    """
    Функция, которая при помощи функции get_dict(), формирует список из 100 книг и записывает его в json файл.
    :return:
    """
    gen = get_dict()
    list_book = [next(gen) for _ in range(100)]
    with open("result.json", "w", encoding="utf8") as f:
        json.dump(list_book, f, ensure_ascii=False, indent=4)
        return None


if __name__ == "__main__":
    main()

