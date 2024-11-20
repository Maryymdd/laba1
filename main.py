import json
from exceptions import InvalidGenreException, InvalidFileTypeException, BookNotFoundException
from BookFactory import BookFactory, UserFactory
from classes import Author, Genre, LibraryUser, BorrowRecord


def menu():
    print("1. Добавить книгу")
    print("2. Добавить пользователя")
    print("3. Выдать книгу пользователю")
    print("4. Вернуть книгу")
    print("5. Загрузить информацию из файла")
    print("6. Выгрузить информацию в файл")
    print("7. Вывести на экран текущую информацию")
    print("0. Выйти")

def info_menu():
    print("1. Вывести подробную информацию о всех книгах")
    print("2. Вывести информацию о доступных книгах")
    print("3. Вывести информацию о читателях")


books = []
users = []
borrow_records = []

while True:
    menu()
    choice = input("Выберите действие: ")
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "0"]:
        print("Ошибка: неверный выбор")
        continue

    if choice == "1":  # Добавить книгу
        valid_genres = ["художественный", "учебный"]
        while True:
            genre = input("Введите жанр книги (художественный или учебный): ").lower()
            try:
                if genre not in valid_genres:
                    raise InvalidGenreException(genre)
                break
            except InvalidGenreException as e:
                print(f"Ошибка: {e}")
                continue
        title = input("Введите название книги: ")
        author_name = input("Введите ФИО автора: ")
        birth = input("Введите дату рождения автора: ")
        year_published = input("Введите дату издания книги: ")
        genre = Genre(genre)

        if genre.genre_name == "учебный":
            subject = input("Введите предмет учебника: ")
            level = input("Введите уровень учебника (например, школьный, университетский): ")
            book = BookFactory.create_book(genre, title, Author(author_name, birth), year_published, subject=subject,
                                           level=level)
        else:
            book = BookFactory.create_book(genre, title, Author(author_name, birth), year_published)

        books.append(book)
        print(f"Книга '{title}' успешно добавлена!")

    elif choice == "2":  # Добавить пользователя
        name = input("Введите имя пользователя: ").capitalize()
        last_name = input("Введите фамилию пользователя: ").capitalize()
        address = input("Введите адрес пользователя: ")
        phone = input("Введите мобильный номер пользователя: ")

        #добавить проверку неверных данных
        user = LibraryUser(name, last_name, address, phone)
        users.append(user)
        print(f"Пользователь {user.last_name} {user.name} успешно добавлен!")

    elif choice == "3":  # Выдать книгу пользователю
        user_name = input("Введите имя пользователя: ")
        book_title = input("Введите название книги: ")

        user = None
        for u in users:
            if u.name == user_name:
                user = u
                break

        book = None
        for b in books:
            if b.title == book_title:
                book = b
                break

        if user and book:
            borrow_record = BorrowRecord(book, user)
            borrow_records.append(borrow_record)
            print(f"Книга '{book_title}' выдана пользователю '{user_name}'!")
        else:
            if not user:
                print("Ошибка: пользователь не найдены.")
            else:
                print("Ошибка: книга не найдены.")


    elif choice == "4":  # Вернуть книгу
        user_name = input("Введите имя пользователя: ").capitalize()
        book_title = input("Введите название книги: ")
        # вынести в отдельную ошибку
        user = None # Поиск пользователя
        for u in users:
            if u.name == user_name:
                user = u
                break
        if not user:
            print("Пользователь не найден")
            continue

        record = None # Поиск записи о выдаче
        for r in borrow_records:
            if r.book == book_title and r.library_user == user_name:
                record = r
                break
        if not record:
            raise BookNotFoundException(book_title)
        else:
            borrow_records.remove(record)
            print(f"Книга '{book_title}' успешно возвращена пользователем {user_name}.")

    elif choice == "5":  # Загрузить данные из файла
        book_filename = input("Введите имя файла для загрузки книг: ")
        user_filename = input("Введите имя файла для загрузки пользователей: ")
        try:

            books = BookFactory.load_from_json(book_filename)
            users = UserFactory.load_users_from_json(user_filename)
            print(f"Информация о книгах и пользователях успешно загружена!")
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")

    elif choice == "6":  # Сохранить данные в файл
        book_filename = input("Введите имя файла для сохранения книг (например, books.json): ")
        user_filename = input("Введите имя файла для сохранения пользователей (например, users.json): ")
        try:
            BookFactory.save_to_json(books, book_filename)
            UserFactory.save_users_to_json(users,borrow_records, user_filename)
            print(f"Информация о книгах сохранена в файл {book_filename}.")
            print(f"Информация о пользователях сохранена в файл {user_filename}.")
        except InvalidFileTypeException as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

    elif choice == "7":  # Вывод информации
        info_menu()
        choise_info = input()
        if choise_info == "1":
            # Подробная информация о всех книгах
            if books:
                print("Список всех книг:")
                for book in books:
                    print(book.get_info(borrow_records))  #borrow_records для проверки статуса
            else:
                print("Нет доступных книг.")

        elif choise_info == "2":
            # Информация о доступных книгах
            borrowed_books = []
            for record in borrow_records:
                borrowed_books.append(record.book)

            available_books = []
            for book in books:
                if book not in borrowed_books:
                    available_books.append(book)

            if available_books:
                print("Доступные книги:")
                for book in available_books:
                    print(book.get_info(borrow_records))
            else:
                print("Нет доступных книг.")

        elif choise_info == "3":
            # Информация о читателях
            if not users:
                print("Нет зарегистрированных читателей.")
            else:
                for user in users:
                    debt_status = "Задолженность" if getattr(user, "has_debt", False) else "Нет задолженности"
                    # Выводим информацию о пользователе с задолженностью
                    print(
                        f"Пользователь: {user.last_name} {user.name}, Адрес: {user.address}, Телефон: {user.phone}, Статус: {debt_status}")

    elif choice == "0":  # Выход
        print("Спасибо за работу! До скорых встреч :)")
        break
