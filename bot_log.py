from basemodel import *
import datetime

class bot_log(BaseModel):
        id = PrimaryKeyField()
        timestamp = DateTimeField(default=datetime.datetime.now())
        trade_model = CharField()
        buy0_sell1 = BooleanField()
        amt_USD = FloatField()
        amt_crypto = FloatField()
        crypto_name = CharField()
