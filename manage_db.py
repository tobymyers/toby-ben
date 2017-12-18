from bot_log import *

db.connect()
print "connected!"

db.create_tables([bot_log])
print "created tables"

bl = bot_log(
        when_strategy = "big_swings",
        how_much_strategy = "risky_business",
        buy_or_sell = "SELL",
        amt_USD = 100.01,
        amt_crypto = 0.004,
        product_name = "LTC-USD"

)

bl.save()

# db.drop_tables([bot_log])
# print "deleted"

db.close()
