from peewee import *

database = MySQLDatabase('pablodb', **{'passwd': '18349276150', 'user': 'pablo'})

class UnknownFieldType(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Tweets(BaseModel):
    created_at = DateTimeField()
    entities = TextField()
    geo_lat = DecimalField(null=True)
    geo_long = DecimalField(null=True)
    name = CharField(max_length=40, null=True)
    profile_image_url = CharField(max_length=200, null=True)
    screen_name = CharField(max_length=20)
    id = BigIntegerField(primary_key = True, db_column='tweet_id')
    tweet_text = CharField(max_length=160)
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'tweets'

