from basemodel import *
import datetime

class bot_log(BaseModel):
        id = PrimaryKeyField()
        timestamp = DateTimeField()
        when_strategy = CharField()
        how_much_strategy = CharField()
        buy_or_sell = CharField()
        amt_USD = FloatField()
        amt_crypto = FloatField()
        product_name = CharField()
        #add prices here
