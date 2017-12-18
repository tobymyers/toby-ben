from basemodel import *
import datetime

class bot_log(BaseModel):
        id = PrimaryKeyField()
        timestamp = DateTimeField(default=datetime.datetime.now())
        when_strategy = CharField()
        how_much_strategy = CharField()
        buy_or_sell = CharField()
        amt_USD = FloatField()
        amt_crypto = FloatField()
        product_name = CharField()
