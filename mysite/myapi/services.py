from contextlib import closing
from django.db import connection
from collections import OrderedDict


def get_author(author_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" select * from myapi_author where id=%s""", [author_id])
        author = dict_fetchone(cursor)
        return author


def get_authors():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" select * from myapi_author""")
        authors = dict_fetchall(cursor)
        return authors


def get_genre(genre_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" select * from myapi_genre where id=%s""", [genre_id])
        genre = dict_fetchone(cursor)
        return genre


def get_genres():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" select * from myapi_genre""")
        genres = dict_fetchall(cursor)
        return genres


def get_book(book_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select myapi_book.*, myapi_author.id as author_id, myapi_author.name as author_name, 
            myapi_genre.id as genre_id, myapi_genre.name as genre_name from myapi_book left join myapi_author on myapi_book.author_id = myapi_author.id
            left join myapi_genre on myapi_book.genre_id = myapi_genre.id 
            where myapi_book.id = %s""", [book_id])
        book = dict_fetchone(cursor)
        return OrderedDict(
            [
                ('id', book['id']),
                ('name', book['name']),
                ('author', OrderedDict(
                    [
                        ('id', book['author_id']),
                        ('name', book['author_name']),
                    ]
                )),
                ('genre', OrderedDict(
                    [
                        ('id', book['genre_id']),
                        ('name', book['genre_name']),
                    ]
                ))
            ]
        )


def get_books():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select myapi_book.*, myapi_author.id as author_id, myapi_author.name as author_name, 
            myapi_genre.id as genre_id, myapi_genre.name as genre_name from myapi_book left join myapi_author on myapi_book.author_id = myapi_author.id
            left join myapi_genre on myapi_book.genre_id = myapi_genre.id 
            """)
        books = dict_fetchall(cursor)
        return [OrderedDict(
            [
                ('id', book['id']),
                ('name', book['name']),
                ('author', OrderedDict(
                    [
                        ('id', book['author_id']),
                        ('name', book['author_name']),

                    ]
                )),
                ('genre', OrderedDict(
                    [
                        ('id', book['genre_id']),
                        ('name', book['genre_name'])
                    ]
                ))
            ]
        ) for book in books]


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
