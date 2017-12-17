from connect_to_gdax import *
from our_bot import *
from bot_log import *

ob = OurBot(api_key, api_secret, passphrase)

print(ob.get_orders())
print
print 
print(ob.get_product_trades(product_id='LTC-USD'))
