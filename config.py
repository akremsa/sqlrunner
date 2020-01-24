import os

class Development(object):
        """
        Development environment configuration
        """

        DEBUG = True
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_USERNAME = os.getenv("DB_USERNAME")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_NAME = os.getenv("DB_NAME")

class Production(object):
        """
        Production environment configuration
        """

        DEBUG = False
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT")
        DB_USERNAME = os.getenv("DB_USERNAME")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_NAME = os.getenv("DB_NAME")

app_config = {
        'development': Development,
        'production': Production,
}