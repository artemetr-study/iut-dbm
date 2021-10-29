'''
Вариант 1.
Создать перечень фильмов в mongoDB с названиями, жанром, количеством сыгравших
актеров, рейтингом популярности (по количеству раз аренды фильма) используя SQL запрос
из базы sakila в mysql.
'''

from pprint import pprint

import mysql.connector
from pymongo import MongoClient

# Сделаем документы для переноса данных в mongodb

client = MongoClient('localhost', 27017)
db = client['sakila']
films_collection = db['films']

# Получим все необходимые данные из mysql

with mysql.connector.connect(host='localhost', database='dev', user='root', password='dev') as connection:
    cursor = connection.cursor(dictionary=True)

    # Данные по фильмам
    cursor.execute('''
                SELECT f.film_id, f.title, COUNT(fa.actor_id) as count_actors, r.rating as rating
                FROM film f
                    INNER JOIN film_actor fa on f.film_id = fa.film_id
                    INNER JOIN (
                        SELECT i.film_id, COUNT(r.rental_id) as rating
                        FROM inventory i
                        INNER JOIN rental r on i.inventory_id = r.inventory_id
                        GROUP BY i.film_id
                    ) r on f.film_id = r.film_id
                GROUP BY f.film_id;
            ''')
    films_data = {i['film_id']: i for i in cursor.fetchall()}

    # Данные по жанрам
    cursor.execute('SELECT c.category_id, c.name FROM category c;')
    categories_data = {i['category_id']: i for i in cursor.fetchall()}

    # Данные по связям жанров и фильмов
    cursor.execute('SELECT fc.film_id, fc.category_id FROM film_category fc;')
    category_to_film_relations = cursor.fetchall()

# Соединим фильмы и их категории
for r in category_to_film_relations:
    if films_data.get(r['film_id']) and categories_data.get(r['category_id']):
        if not films_data[r['film_id']].get('categories'):
            films_data[r['film_id']]['categories'] = []
        films_data[r['film_id']]['categories'].append({'name': categories_data.get(r['category_id'])['name']})

# Запишем фильмы
films_collection.drop()
films_collection.insert_many(films_data.values())
del films_data, category_to_film_relations, categories_data

# Обновим название любого фильма средствами MongoDb
film = films_collection.find_one()
pprint(film)
'''
{'_id': ObjectId('617bbd2e07542eda95e3e3d8'),
 'categories': [{'name': 'Documentary'}],
 'count_actors': 10,
 'film_id': 1,
 'rating': 23,
 'title': 'ACADEMY DINOSAUR'}
'''
films_collection.update_one({'title': film['title']}, {'$set': {'title': 'Some title'}})
film = films_collection.find_one({'title': 'Some title'})
pprint(film)
'''
{'_id': ObjectId('617bbd2e07542eda95e3e3d8'),
 'categories': [{'name': 'Documentary'}],
 'count_actors': 10,
 'film_id': 1,
 'rating': 23,
 'title': 'Some title'}
'''

# Удалим несколько фильмов по критерию жанра
horror_films = films_collection.count_documents({'categories': {'$elemMatch': {'name': 'Horror'}}})
pprint(horror_films)  # 53
films_collection.delete_many({'categories': {'$elemMatch': {'name': 'Horror'}}})
horror_films = films_collection.count_documents({'categories': {'$elemMatch': {'name': 'Horror'}}})
pprint(horror_films)  # 0


# Подсчитать количество фильмов в жанре науной фантастики средствами MongoDb
pprint(films_collection.count_documents({'categories': {'$elemMatch': {'name': 'Sci-Fi'}}}))  # 5

# Найти фильмы с рейтингом более 5 средствами MongoDB
pprint(films_collection.count_documents({'rating': {'$gt': 5}}))  # 886
