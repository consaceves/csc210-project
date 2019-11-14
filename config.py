import os

project_name = 'ebay 2.0'


class Config(object):
    # SQL Alchemy stuff here

    BLUEPRINTS = [
        ('login', {'url_prefix': '/'})
    ]
