import json
from pymongo import MongoClient

# Функція для завантаження даних з JSON файлу
def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Підключення до MongoDB Atlas
client = MongoClient('mongodb+srv://goitlearn:Asd852654@cluster0.szweo9j.mongodb.net/')
db = client.quotes_db

# Завантаження даних з JSON файлів
authors = load_json('authors.json')
quotes = load_json('quotes.json')

# Колекції в базі даних
authors_collection = db.authors
quotes_collection = db.quotes

# Очистка колекцій, якщо потрібно
authors_collection.delete_many({})
quotes_collection.delete_many({})

# Імпорт даних в колекції
authors_collection.insert_many(authors)
quotes_collection.insert_many(quotes)

print("Дані успішно імпортовані в MongoDB.")
