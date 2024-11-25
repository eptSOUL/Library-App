import json

#Класс для представления книги
class Book:
    
    def __init__(self, book_id, title, author, year, status="в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"

    #Преобразование объекта "книги" в словарь
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    #Создание объекта "книги" из словаря
    @staticmethod
    def from_dict(data):  
        return Book(data["id"], data["title"], data["author"], data["year"], data["status"])

#Класс для управления библиотекой
class Library:

    def __init__(self, file_name="library.json"):
        self.file_name = file_name
        self.books = self.load_data()
        self.next_id = self.find_next_id()

    #Чтение данных из файла
    def load_data(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    #Сохранение данных в файл
    def save_data(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4, ensure_ascii=False)

    #Вычисление следующего ID при добавлении книги
    def find_next_id(self):
        if not self.books:
            return 1 
        existing_ids = {book.id for book in self.books}  #Множество всех существующих ID
        next_id = 1
        while next_id in existing_ids:  #Находим первый свободный ID
            next_id += 1
        return next_id


    #Добавление книги с проверкой корректности года
    def add_book(self, title, author, year):
        try:
            #Проверка, что год является целым числом
            year = int(year)
            if year < 0:
                print("\nОшибка: Год не может быть отрицательным.")
                return
        except ValueError:
            print("\nОшибка: Год издания должен быть числом.")
            return
        
        #Создание книги, если год корректен
        book = Book(self.next_id, title, author, str(year))  # Преобразуем год в строку для хранения
        self.books.append(book)
        self.sort_books_by_id()
        self.next_id = self.find_next_id()
        self.save_data()
        print(f"\nКнига '{title}' добавлена с ID {book.id}.")


    #Удаление книги по ID
    def delete_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_data()
            print(f"\nКнига с ID {book_id} удалена.")
        else:
            print("\nКнига с указанным ID не найдена.")

    #Поиск книги по ID
    def find_book_by_id(self, book_id):
        return next((book for book in self.books if book.id == book_id), None)

    #Изменение статуса книги
    def change_status(self, book_id, new_status):
        book = self.find_book_by_id(book_id)
        if not book:
            print("\nКнига с указанным ID не найдена.")
            return

        if new_status not in ["в наличии", "выдана"]:
            print("\nНекорректный статус.")
            return

        book.status = new_status
        self.save_data()
        print(f"\nСтатус книги с ID {book_id} изменён на '{new_status}'.")

    #Отображение всех книг
    def display_books(self):
        self.sort_books_by_id()
        if self.books:
            print("\nСписок книг в библиотеке:")
            for book in self.books:
                print(book)
        else:
            print("\nБиблиотека пуста.")

    #Поиск книг по названию, автору или году
    def search_books(self, query):
        query = query.lower()
        results = [
            book for book in self.books
            if query in book.title.lower() or query in book.author.lower() or query in book.year
            ]
        return results

    #Сортировка книг по ID
    def sort_books_by_id(self):
        self.books.sort(key=lambda book: book.id)


#Приложение для управления библиотекой
class LibraryApp:

    def __init__(self):
        self.library = Library()

    #Запуск приложения
    def run(self):
        while True:
            print("\nМеню:")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Поиск книги")
            print("4. Отобразить все книги")
            print("5. Изменить статус книги")
            print("6. Выйти")

            choice = input("Выберите действие (1-6): ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":
                self.search_books()
            elif choice == "4":
                self.library.display_books()
            elif choice == "5":
                self.change_status()
            elif choice == "6":
                self.library.save_data()
                print("\nДанные сохранены. До свидания!")
                break
            else:
                print("\nНекорректный выбор. Попробуйте снова.")

    #Добавление книги
    def add_book(self):
        title = input("\nВведите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания: ")
        self.library.add_book(title, author, year)

    #Удаление книги
    def delete_book(self):
        try:
            book_id = int(input("\nВведите ID книги для удаления: "))
            self.library.delete_book(book_id)
        except ValueError:
            print("Некорректный ввод ID.")

    #Поиск книг
    def search_books(self):
        query = input("\nВведите название, автора или год издания для поиска: ")
        results = self.library.search_books(query)
        if results:
            print("\nНайденные книги:")
            for book in results:
                print(book)
        else:
            print("\nКниги по вашему запросу не найдены.")

    #Изменение статуса книги
    def change_status(self):
        try:
            book_id = int(input("\nВведите ID книги для изменения статуса: "))
            new_status = input("\nВведите новый статус ('в наличии' или 'выдана'): ").strip().lower()
            self.library.change_status(book_id, new_status)
        except ValueError:
            print("Некорректный ввод ID.")


if __name__ == "__main__":
    app = LibraryApp()
    app.run()
