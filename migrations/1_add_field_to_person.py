from playhouse.migrate import *
from environs import Env

environment = Env()
environment.read_env()

DB_NAME = environment("DB_NAME")
DB_URI = environment("DB_URI")


db = PostgresqlDatabase(
    database=DB_NAME,
    dsn=DB_URI,
)
db.connect()
migrator = PostgresqlMigrator(db)

if __name__ == "__main__":
    migrate(
        migrator.add_column('person', 'eye', CharField(verbose_name="цвет глаз", default="")),
    )


