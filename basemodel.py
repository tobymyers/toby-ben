from peewee import *

db = MySQLDatabase('toby_ben', user='root', passwd='root')

class BaseModel(Model):
        class Meta:
            database = db
