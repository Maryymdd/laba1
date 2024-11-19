from classes import( Book, FictionBook,ScienceBook, HistoricalBook, HorrorBook, PoetryBook,
                     BiographyBook, AdventureBook, RomanceBook, MysteryBook, FantasyBook)
import json
from exceptions import InvalidGenreException, InvalidFileTypeException

class BookFactory:
    genres = {
        "классика": lambda genre, title, author: FictionBook(genre, title, author),
        "научная": lambda genre, title, author: ScienceBook(genre, title, author),
        "фантастика": lambda genre, title, author: FantasyBook(genre, title, author),
        "мистика": lambda genre, title, author: MysteryBook(genre, title, author),
        "романтика": lambda genre, title, author: RomanceBook(genre, title, author),
        "история": lambda genre, title, author: HistoricalBook(genre, title, author),
        "ужасы": lambda genre, title, author: HorrorBook(genre, title, author),
        "биография": lambda genre, title, author: BiographyBook(genre, title, author),
        "приключения": lambda genre, title, author: AdventureBook(genre, title, author),
        "поэма": lambda genre, title, author: PoetryBook(genre, title, author),
    }

    @staticmethod
    def create_book(genre, title, author):
        """Создаёт книгу в зависимости от жанра."""
        if genre not in BookFactory.genres:
            raise InvalidGenreException(genre)
        return BookFactory.genres[genre](genre, title, author)
    @staticmethod
    def save_to_json(books, filename):
        """Сохраняет книги в JSON файл."""
        if ".json" not in filename:
            raise InvalidFileTypeException(filename)
        with open(filename, "w") as file:
            json.dump([book.to_dict() for book in books], file)

    @staticmethod
    def load_from_json(filename):
        """Загружает книги из JSON файла."""
        if ".json" not in filename:
            raise InvalidFileTypeException(filename)
        with open(filename, "r") as file:
            books_data = json.load(file)
            return [
                BookFactory.create_book(book["genre"], book["title"], book["author"])
                for book in books_data
            ]