import json
#from curses.ascii import isdigit
from exceptions import InvalidGenreException, InvalidFileTypeException
from BookFactory import BookFactory


def menu():
    print("1. Добавить книгу")
    print("2. Загрузить информацию из файла")
    print("3. Выгрузить информацию в файл")
    print("4. Вывести на экран текущую информацию")
    print("0. Выйти")


books = []
while True:
    menu()
    choise = input("Выберите действие: ")
    if choise not in ["1", "2", "3", "4", "0"] :
        print("Error")
        continue
    if choise == "1":
        valid_genres = ["классика", "научная", "фантастика", "мистика", "романтика",
                        "история", "ужасы", "биография","приключения", "поэма"]
        while True:
            genre = input(
                "Выберите категорию книги (классика, научная, фантастика, мистика, романтика,"
                " \nистория, ужасы, биография, приключения, поэма): ")
            try:
                if genre not in valid_genres:
                    raise InvalidGenreException(genre)
                break

            except InvalidGenreException as e:
                print(f"Ошибка: {e}")
                continue

        title = input("Введите название книги: ")
        author = input("Введите ФИО автора: ")

        try:
            # Создание книги
            book = BookFactory.create_book(genre, title, author)
            books.append(book)
            print(f"Книга '{title}' успешно добавлена!")
        except InvalidGenreException as e:
            print(f"Ошибка при создании книги: {e}")

    elif choise == "2":
        filename = input("Введите имя файла для загрузки данных: ")
        try:
            # Загрузка книг из файла
            books = BookFactory.load_from_json(filename)
            print(f"Информация о книгах успешно загружена из файла {filename}.")
        except InvalidFileTypeException as e:
            print(f"Ошибка: {e}")
        except FileNotFoundError:
            print(f"Ошибка: Файл {filename} не найден.")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

    elif choise == "3":
        filename = input("Введите имя файла для сохранения данных: ")
        try:
            # Сохранение книг в файл
            BookFactory.save_to_json(books, filename)
            print(f"Информация о книгах успешно сохранена в файл {filename}.")
        except InvalidFileTypeException as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

    elif choise == "4":
        if books:
            print("Список книг:")
            for book in books:
                book.info()  # Вывод информации о книге
                book.genre_description()
                print()

        else:
            print("Список книг пуст.")


    elif choise == "0":
        print("Спасибо за работу! \nДо скорых встреч :)")
        break











