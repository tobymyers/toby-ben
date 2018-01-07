from connect_to_gdax import *
from bot_log import *

class OurBot(gdax.AuthenticatedClient): #something similar should inherit from authclient

    def log_in_db(self, when_strategy, how_much_strategy, buy_or_sell, amt_USD, amt_crypto, product_name):
        now = datetime.datetime.now()
        new_log = bot_log.create(timestamp = now, when_strategy = when_strategy, how_much_strategy = how_much_strategy, buy_or_sell = buy_or_sell, amt_USD = amt_USD, amt_crypto = amt_crypto, product_name = product_name)
        new_log.save()


    def implement_strategy(self, strategy_object, last_trade_call, last_fill_call, count):
        self.strategy = strategy_object
        side = ""
        buy_choice = self.strategy.choose_to_buy(last_trade_call, last_fill_call, count )
        sell_choice = self.strategy.choose_to_sell(last_trade_call, last_fill_call, count)
        return buy_choice, sell_choice, side

    def ensure_buy(self, avg_trade_price, product_name, bid_amount):
        status = "pending"
        price_change = -1
        for i in range(10):
            if status != "done":
                price_change += 0.40
                buy_response = self.buy(price= str(avg_trade_price+price_change), #USD, got to make sure it bids a bit higher
                       size= str(bid_amount), #crypto
                       type = "limit",
                       time_in_force = "GTC",
                       product_id = product_name)
                print(buy_response)
                status = self.get_order(buy_response["id"])["status"]
                self.cancel_order(buy_response["id"])
                print(status, "status")
        return buy_response

    def ensure_sell(self, avg_trade_price, product_name, bid_amount):
        status = "pending"
        price_change = 1
        for i in range(10):
            if status != "done":
                price_change -= 0.40
                sell_response = self.sell(price= str(avg_trade_price+price_change), #USD, got to make sure it bids a bit higher
                       size= str(bid_amount), #crypto
                       type = "limit",
                       time_in_force = "GTC",
                       product_id = product_name)
                print(sell_response)
                status = self.get_order(sell_response["id"])["status"]
                self.cancel_order(sell_response["id"])
        return sell_response
