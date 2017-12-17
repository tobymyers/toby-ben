from bot_log import *

db.connect()
print "connected!"

db.create_tables([bot_log])
print "created tables"

bl = bot_log(
        trade_model = "model1"
        buy0_sell1 = False
        amt_USD = 100.345
        amt_crypto = 0.000345
        crypto_name = "ETH"
)
bl.save()

# db.drop_tables([bot_log])
# print "deleted"

db.close()
