from conf import MODEL
import random
import faker
import json

def pk(start):
    yield start
    while True:
        start += 1
        yield start


def title():
    with open("books.txt", "r", encoding="utf-8") as f:
        book = random.choice(f.read().splitlines())
    return book

def year():
    year = random.choice(range(2000, 2022))
    return year

def pages():
    pages = random.choice(range(1, 500))
    return pages

def isbn13():
    fake = faker.Faker()
    for _ in range(101):
        return fake.isbn10()

def rating():
    rating = (round(random.uniform(0, 5), 1) for x in range(5))
    return next(rating)

def price():
    price = (round(random.uniform(0, 2000), 1) for x in range(100))
    return next(price)


def author():
    fake = faker.Faker()
    return [fake.name() for _ in range(random.randint(1,3))]


def get_dict(start=1):
    gen_pk = pk(start)
    while True:
        yield {"model": MODEL, "pk": next(gen_pk), "fields": {"title": title(), "year": year(), "pages": pages(),
                                                              "isbn13": isbn13(), "rating": rating(), "price": price(),
                                                              "author": author()}}


def main():
    list_book = [next(get_dict()) for _ in range(100)]
    with open("result.json", "w", encoding="utf8") as f:
        json.dump(list_book, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()