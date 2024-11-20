import json
from classes import Book, Author, Genre, FictionBook, Textbook, LibraryUser
from exceptions import InvalidFileTypeException, InvalidGenreException

class BookFactory:
    @staticmethod
    def create_book(genre, title, author, year_published, **kwargs):
        if genre.genre_name == "учебный":
            return Textbook(title, author, year_published, kwargs.get("subject"), kwargs.get("level"))
        elif genre.genre_name == "художественный":
            return FictionBook(title, author, year_published, genre)
        else:
            raise InvalidGenreException(genre.genre_name)

    @staticmethod
    def save_to_json(books, filename):
        if not filename.endswith(".json"):
            raise InvalidFileTypeException(filename.split(".")[-1])

        book_list = []
        for book in books:
            book_data = {
                "title": book.title,
                "author": {"name": book.author.name, "birth_year": book.author.birth_year},
                "year_published": book.year_published,
            }
            book_list.append(book_data)

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(book_list, file, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_json(filename):
        if not filename.endswith(".json"):
            raise InvalidFileTypeException(filename.split(".")[-1])

        with open(filename, "r", encoding="utf-8") as file:
            book_list = json.load(file)

        books = []
        for book_data in book_list:
            author = Author(book_data["author"]["name"], book_data["author"]["birth_year"])
            book = Book(book_data["title"], author, book_data["year_published"])
            books.append(book)

        return books

class UserFactory:
        @staticmethod
        def save_users_to_json(users, borrow_records, filename):
            user_list = []
            for user in users:
                has_debt = any(record.library_user == user and record.is_not_returned() for record in borrow_records)
                user_data = {
                    "name": user.name,
                    "last_name": user.last_name,
                    "address": user.address,
                    "phone": user.phone,
                    "has_debt": has_debt,
                }
                user_list.append(user_data)

            with open(filename, "w", encoding="utf-8") as file:
                json.dump(user_list, file, ensure_ascii=False, indent=4)

        @staticmethod
        def load_users_from_json(filename):
            with open(filename, "r", encoding="utf-8") as file:
                user_list = json.load(file)

            users = []

            for user_data in user_list:
                user = LibraryUser(
                    user_data["name"],
                    user_data["last_name"],
                    user_data["address"],
                    user_data["phone"],

                )
                user.has_debt = user_data.get("has_debt")
                users.append(user)

            return users

