class Book:    # базовый класс книги
    def __init__(self, genre, title, autor) -> None: # конструктор
        self.genre = genre
        self.title = title
        self.autor = autor
        self.availability = True

    def info(self):
        print(f"'{self.title}' - автор: {self.autor}, категория: {self.genre}")

    def to_dict(self):
        return {
            "type": self.__class__.__name__,  # тип класса
            "genre": self.genre,
            "title": self.title,
            "author": self.autor,
            #"availability": self.availability
        }

class FictionBook(Book): #художетсвенная
    def genre_description(self) -> None:
        print(f"Книга '{self.title}' предлагает захватывающий вымысел, который погрузит вас в фантастический мир.")

class ScienceBook(Book): #
    def genre_description(self) -> None:
        print(f"Книга '{self.title}' объясняет научные теории и открытия в доступной форме.")

class FantasyBook(Book):
    def genre_description(self) -> None:
        print(f"Книга '{self.title}' полна магии, приключений и сказочных существ.")

class MysteryBook(Book):
    def genre_description(self) -> None:
        print(f"Книга '{self.title}' увлечёт вас загадками и неожиданными поворотами сюжета.")

class RomanceBook(Book):
    def genre_description(self) -> None:
        print(f"Книга '{self.title}' рассказывает историю любви, которая согреет ваше сердце.")

class HistoricalBook(Book):
    def genre_description(self) -> None:
        print(f"Книга '{self.title}' переносит вас в прошлое, чтобы изучить важные исторические события.")

class HorrorBook(Book):
    def genre_description(self) -> None:
        print(f"Книга '{self.title}' наполнена страшными историями, которые заставят ваше сердце замирать.")

class BiographyBook(Book):
    def genre_description(self) -> None:
        print(f"Книга '{self.title}' рассказывает историю жизни выдающейся личности.")

class AdventureBook(Book):
    def genre_description(self) -> None:
        print(f"Книга '{self.title}' увлечёт вас в захватывающие путешествия и приключения.")

class PoetryBook(Book):
    def genre_description(self) -> None:
        print(f"Книга '{self.title}' наполняет душу прекрасными стихами.")
