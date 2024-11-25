import unittest
from library_app import Library, Book  #Импортируем классы

class TestLibrary(unittest.TestCase):

    #Инициализация перед каждым тестом
    def setUp(self):
        self.library = Library(file_name="test_library.json")  #Используем тестовый файл
        self.library.books = []  #Очищаем библиотеку перед тестами
        self.library.next_id = 1

    #Очистка после тестов
    def tearDown(self):
        self.library.save_data()  #Сохраняем пустые данные

    #Тест добавления книги
    def test_add_book(self):
        self.library.add_book("Книга 1", "Автор 1", 2020)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Книга 1")

    #Тест удаления книги
    def test_delete_book(self):
        self.library.add_book("Книга 1", "Автор 1", 2020)
        self.library.delete_book(1)
        self.assertEqual(len(self.library.books), 0)

    #Тест поиска книги по ID
    def test_find_book_by_id(self):
        self.library.add_book("Книга 1", "Автор 1", 2020)
        book = self.library.find_book_by_id(1)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Книга 1")

    #Тест изменения статуса книги
    def test_change_status(self):
        self.library.add_book("Книга 1", "Автор 1", 2020)
        self.library.change_status(1, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

    #Тест поиска книги по запросу
    def test_search_books(self):
        self.library.add_book("Книга 1", "Автор 1", 2020)
        self.library.add_book("Книга 2", "Автор 2", 2021)
        results = self.library.search_books("Автор 1")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Книга 1")
