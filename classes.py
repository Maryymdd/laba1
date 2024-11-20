# Основные классы
class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author  # Author object
        self.year_published = year_published

    def __str__(self):  # Для пользователя
        return f"'{self.title}' - автор: {self.author.name}, год издания: {self.year_published}"



    def get_info(self, borrow_records):  # Передаем borrow_records для получения статуса книги
        # Проверяем все записи о выдаче
        borrow_status = "свободна"
        for record in borrow_records:
            if record.book == self:  # Если книга найдена среди выданных
                borrow_status = "взята"
                break
        return f"'{self.title}' - автор: {self.author.name}, год: {self.year_published}, статус: {borrow_status}"

class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return self.name


class Genre:
    def __init__(self, genre_name):
        self.genre_name = genre_name

    def __str__(self):
        return self.genre_name


class LibraryUser:
    def __init__(self, name, last_name, address, phone):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.phone = phone

    def __str__(self):
        return self.last_name

    def check_debt(self, borrow_records):
        """Проверка, есть ли задолженность у пользователя."""
        for record in borrow_records:
            if record.library_user == self and record.is_not_returned():
                return True  # Если хотя бы одна книга не возвращена
        return False  # Нет задолженности


class BorrowRecord: #учет возврата
    def __init__(self, book, library_user):
        self.book = book
        self.library_user = library_user
        self.returned = False

    def mark_as_returned(self):
        self.returned = True

    def is_not_returned(self):
        return not self.returned

    def __str__(self):
        return f"{self.book.title} - взята пользователем: {self.library_user.name}."

#аследники книг

class FictionBook(Book):
    
    def __init__(self, title, author, year_published, genre):
        super().__init__(title, author, year_published)
        self.genre = genre
    
    def describe_themes(self):
        return f"Книга '{self.title}' — это бессмертное произведение, которое отражает культурное наследие и глубину человеческой мысли."


class Textbook(Book):
    def __init__(self, title, author, year_published, subject, level):
        super().__init__(title, author, year_published)
        self.subject = subject
        self.level = level

    def describe_subject(self):
        return f"Subject: {self.subject}, Level: {self.level}"

# Наследники авторов
class Poet(Author):
    def __init__(self, name, birth_year, poetry_style):
        super().__init__(name, birth_year)
        self.poetry_style = poetry_style

    def __str__(self):
        return f"{self.name}, поэт, известен своим стилем{self.poetry_style}"


class Writer(Author):
    def __init__(self, name, birth_year, writing_style):
        super().__init__(name, birth_year)
        self.writing_style = writing_style

    def __str__(self):
        return f"{self.name}, писатель, известен своим стилем {self.writing_style}"


# Наследники жанров
class FictionGenre(Genre):
    def __init__(self):
        super().__init__("художественный")


class ScientificGenre(Genre):
    def __init__(self):
        super().__init__("научный")






