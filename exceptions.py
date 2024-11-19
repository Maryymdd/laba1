class InvalidGenreException(Exception):

    def __init__(self, genre):
        super().__init__(f"Неверный жанр книги: {genre}. Попробуйте снова!")


class InvalidFileTypeException(Exception):
    def __init__(self, file_type):
        super().__init__(f"Неверный тип файла: {file_type}. Допустимые типы: json.")
