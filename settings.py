db_settings = {
    'DB_HOST': 'localhost',
    'DB_NAME': 'testdb',
    'DB_USER': 'testuser',
    'DB_PASSWORD': 'testpass',
    'DB_PORT': 5432
}

db_dsn = "postgres://{user}:{password}@{host}:{port}/{database}".format(
        user=db_settings["DB_USER"], password=db_settings["DB_PASSWORD"], host=db_settings["DB_HOST"],
        port=db_settings["DB_PORT"], database=db_settings["DB_NAME"]
    )