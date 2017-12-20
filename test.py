from connect_to_gdax import *
from our_bot import *
from bot_log import *
import json
import time
# ob = OurBot(api_key, api_secret, passphrase)
#
# print(ob.get_fills(product_id = "LTC-USD"))
#
#
# def log_in_db(self, when_strategy, how_much_strategy, buy_or_sell, amt_USD, amt_crypto, product_name):
#     new_log = bot_log.create(when_strategy = when_strategy, how_much_strategy = how_much_strategy, buy_or_sell = buy_or_sell, amt_USD = amt_USD, amt_crypto = amt_crypto, product_name = product_name)
#     new_log.save()
# for i in range(10):
#      ob.log_in_db("when", "how much", 0, 0, 0, "product_name")
#      time.sleep(1)
#

for i in range(10):
     default=datetime.datetime.now()
     new_log = bot_log.create(timestamp = default, when_strategy = "when_strategy", how_much_strategy = "how_much_strategy", buy_or_sell = 0, amt_USD = 0, amt_crypto = 0, product_name = "product_name")
     time.sleep(1)

# def parse_get_product_trades(api_response):
#     last_trades = 0
#     trade_data = api_response
#     for trade in trade_data:
#         last_trades += float(trade["price"])
#     avg_trade_price = last_trades / len(trade_data)
#     return avg_trade_price
#
# print ob.get_fills()
#
# #
# #
# #
# #
# #
# #
# # parse_get_product_trades(api_response)
# # print
# # print
# #     when_strategy = "big_swings",
#     how_much_strategy = "risky_business",
#     buy_or_sell = "SELL",
#     amt_USD = 100.01,
#     amt_crypto = 0.004,
#     product_name = "LTC-USD"
#
#
#
# def parse_get_fills(api_response):
#     last_order = api_response[0][0]
#     return last_order["product_id"], last_order["price"]
#
# api_response = [[{u'fee': u'0.0000000000000000', u'user_id': u'5a21e2ec8c2f93020d945e51', u'product_id': u'LTC-USD', u'order_id': u'8f1de547-031a-40d3-8ef5-470b854f1fff', u'created_at': u'2017-12-15T15:21:21.583Z', u'profile_id': u'579a3628-7428-4389-a908-904f425109ad', u'side': u'sell', u'price': u'311.02000000', u'trade_id': 18057076, u'settled': True, u'liquidity': u'M', u'size': u'5.00000000'}, {u'fee': u'0.0000000000000000', u'user_id': u'5a21e2ec8c2f93020d945e51', u'product_id': u'LTC-USD', u'order_id': u'67efda48-3121-4ac5-bc86-83055868ba10', u'created_at': u'2017-12-14T14:51:52.582Z', u'profile_id': u'579a3628-7428-4389-a908-904f425109ad', u'side': u'buy', u'price': u'280.00000000', u'trade_id': 17677234, u'settled': True, u'liquidity': u'M', u'size': u'4.00000000'}, {u'fee': u'0.0000000000000000', u'user_id': u'5a21e2ec8c2f93020d945e51', u'product_id': u'LTC-USD', u'order_id': u'509e3ca3-aadb-4b66-b9c3-1f4cadd0e8fa', u'created_at': u'2017-12-13T22:26:15.108Z', u'profile_id': u'579a3628-7428-4389-a908-904f425109ad', u'side': u'sell', u'price': u'317.77000000', u'trade_id': 17438969, u'settled': True, u'liquidity': u'M', u'size': u'2.03038619'}]]
#
# parse_get_fills(api_response)
