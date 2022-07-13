from peewee import *

from config import get_db


db = get_db()


class Person(Model):
    """
    Пользователь
    """

    first_name = CharField(verbose_name="имя")
    last_name = CharField(verbose_name="фамилия")
    age = IntegerField(verbose_name="возраст")
    is_ill = BooleanField(verbose_name="болен или нет")
    eye = CharField(verbose_name="цвет глаз", default="")

    class Meta:
        database = db


class Book(Model):
    """
    Книга
    """

    title = CharField(verbose_name="название")
    year = IntegerField(verbose_name="год выпуска")
    author = ForeignKeyField(Person, verbose_name="автор", backref="books")

    class Meta:
        database = db


if __name__ == "__main__":
    db.create_tables([Person, Book])

    # user1 = User(first_name="Bob", last_name="DD", age=30, is_ill=True)
    # user1.save()
    #
    # user2 = User.create(first_name="Alan", last_name="DS", age=45, is_ill=False)

    for item in Person.select():
        print(item.first_name, item.last_name)
