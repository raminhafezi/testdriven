#services/users/project/config.py

import os

class BaseConfig:
	""" Base Configuration"""
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
	""" Development Configuration"""
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class TestingConfig(BaseConfig):
<<<<<<< HEAD
=======
	""" Testing Configuration """
>>>>>>> 59a433577b98b7f6b4e03b9c92d92cb391d2c20e
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
	""" Production Configuration """
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
