""" Module for managing tasks through a simple cli interface. """

import os
from manager import Manager  # manage.py lib

from yoyo import read_migrations, get_backend
from settings import db_settings

from server import app

manager = Manager()


@manager.command
def run(port=8000, dev=False, debug=False):
    """
    Starts Sanic server on port 8000. https://sanic.dev/en/guide/deployment/running.html
    python manage.py run --dev - for development mode
    """
    app.run(port=port, dev=dev, debug=debug)


@manager.command
def migrate(rollback=False, create=''):
    """
    Database raw SQL migrations. yoyo-migrations lib https://ollycope.com/software/yoyo/
    Config file: yoyo.ini
    python manage.py migrate - for apply migrations
    python manage.py migrate --rollback - for rollback
    python manage.py migrate --create 'migration_name' - create new migration
    """
    dsn = "postgres://{user}:{password}@{host}:{port}/{database}".format(
        user=db_settings["DB_USER"], password=db_settings["DB_PASSWORD"], host=db_settings["DB_HOST"],
        port=db_settings["DB_PORT"], database=db_settings["DB_NAME"]
    )

    backend = get_backend(dsn)
    migrations = read_migrations('./migrations')
    if rollback:
        print('Rollback migrations')
        with backend.lock():
            # Rollback all migrations
            backend.rollback_migrations(backend.to_rollback(migrations))
        print('Rollback migrations done')
    elif create:
        print('Create new migration')
        os.system(f'yoyo new ./migrations -m "{create}"')
    else:
        print('Apply migrations')
        with backend.lock():
            # Apply any outstanding migrations
            backend.apply_migrations(backend.to_apply(migrations))
        print('Apply migrations done')


if __name__ == '__main__':
    manager.main()