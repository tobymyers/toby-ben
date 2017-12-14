from basemodel import *
import datetime

class bot_log(BaseModel):
        id = PrimaryKeyField()
        type = BooleanField()
        amount = IntegerField()
        timestamp = DateTimeField(default=datetime.datetime.now())
