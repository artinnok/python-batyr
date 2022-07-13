from playhouse.migrate import *

from config import get_db


db = get_db()
migrator = PostgresqlMigrator(db)

if __name__ == "__main__":
    migrate(
        migrator.add_column('person', 'eye', CharField(verbose_name="цвет глаз", default="")),
    )


