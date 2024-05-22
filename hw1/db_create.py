from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://goitlearn:qwerty1@cluster0.szweo9j.mongodb.net/",
    server_api=ServerApi('1')
)

db = client['cats_db']
collection = db['cats_collection']


def create_cat(name, age, features):
    """Створення нового запису про кота."""
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    return collection.insert_one(cat).inserted_id

def read_all_cats():
    """Читання всіх записів із колекції."""
    return list(collection.find({}))

def read_cat_by_name(name):
    """Читання запису про кота за іменем."""
    return collection.find_one({"name": name})

def update_cat_age(name, new_age):
    """Оновлення віку кота за іменем."""
    return collection.update_one({"name": name}, {"$set": {"age": new_age}})

def add_feature_to_cat(name, feature):
    """Додавання нової характеристики до списку features кота за іменем."""
    return collection.update_one({"name": name}, {"$push": {"features": feature}})

def delete_cat_by_name(name):
    """Видалення запису про кота за іменем."""
    return collection.delete_one({"name": name})

def delete_all_cats():
    """Видалення всіх записів із колекції."""
    return collection.delete_many({})

# Приклади використання функцій
cat_id = create_cat("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
print(f"Створено кота з ID: {cat_id}")

all_cats = read_all_cats()
print(f"Усі коти: {all_cats}")

cat_info = read_cat_by_name("barsik")
print(f"Інформація про кота barsik: {cat_info}")

update_cat_age("barsik", 4)
print(f"Вік кота barsik оновлено на 4 роки.")

add_feature_to_cat("barsik", "любить іграшки")
print(f"Додано нову характеристику до кота barsik.")

delete_cat_by_name("barsik")
print(f"Кота barsik видалено.")

delete_all_cats()
print(f"Усі коти видалені.")

