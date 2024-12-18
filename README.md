# 📚 Library Management App

**Приложение для управления библиотекой.**  
Позволяет добавлять, удалять, редактировать и искать книги, а также изменять их статус.  
Данные сохраняются в формате **JSON** для удобного хранения и последующего использования.

---

## 📖 Основной функционал

### 1️⃣ Добавление книги
Позволяет добавить книгу с указанием следующих данных:
- **Название**
- **Автор**
- **Год издания**

Особенности:
- Автоматическое присвоение уникального **ID**.
- Проверка корректности года (число и не отрицательное значение).

### 2️⃣ Удаление книги
- Удаление книги по её **уникальному ID**.
- Данные автоматически обновляются в JSON-файле.

### 3️⃣ Поиск книги
Удобный поиск по библиотеке:
- По **названию**.
- По **автору**.
- По **году издания**.

Особенности:
- Регистронезависимый поиск.
- Результаты отображаются в читаемом формате.

### 4️⃣ Отображение всех книг
- Вывод списка всех книг, отсортированных по их **ID**.
- Уведомление, если библиотека пуста.

### 5️⃣ Изменение статуса книги
Позволяет изменить статус книги на:
- "в наличии".
- "выдана".

Изменение производится по **уникальному ID** книги.

### 6️⃣ Сохранение данных
- Все изменения сохраняются в файл **library.json**.
- При запуске приложения данные загружаются из файла (если он существует).

### 7️⃣ Сортировка книг
- Книги автоматически упорядочиваются по **ID**.

### 8️⃣ Меню управления
Интуитивно понятное меню включает:
- Добавление книги.
- Удаление книги.
- Поиск книги.
- Отображение всех книг.
- Изменение статуса книги.
- Выход из приложения.

---

## ⚠️ Возможные ошибки и защита от них

- **Некорректный ввод года**: Уведомление, если год не число или меньше 0.
- **Некорректный ID**: Уведомление, если книга с указанным ID не найдена.
- **Несуществующий файл JSON**: При отсутствии файла создаётся новый.

---

## 🛠️ Зависимости
- **Python 3.x**
- Стандартная библиотека Python:
  - `json`

---

## 💡 Дополнительно: Будущие улучшения
- Реализация графического интерфейса.
- Введение категорий и тегов для книг.
- Возможность резервирования книг.

---

## 🚀 Запуск приложения

1. Убедитесь, что установлен Python 3.x.
2. Скачайте файлы проекта.
3. Запустите приложение командой:
   ```bash
   python library_app.py
