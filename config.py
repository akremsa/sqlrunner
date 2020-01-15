import os

class Development(object):
        """
        Development environment configuration
        """

        DEBUG = True
        DB_HOST = os.getenv("DB_HOST")

class Production(object):
        """
        Production environment configuration
        """

        DEBUG = True
        DB_HOST = os.getenv("DB_HOST")

app_config = {
        'development': Development,
        'production': Production,
}