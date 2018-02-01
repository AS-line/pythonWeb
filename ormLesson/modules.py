from peewee import *

db = SqliteDatabase("people.db")


class Person(Model):
    name = CharField(max_length=50)
    age = SmallIntegerField()
    male = BooleanField()

    class Meta:
        database = db


def create_table():
    with db:
        db.create_tables([Person]) #передаём список таблиц