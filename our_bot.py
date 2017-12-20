from connect_to_gdax import *
from bot_log import *

class OurBot(gdax.AuthenticatedClient): #something similar should inherit from authclient

    def log_in_db(self, when_strategy, how_much_strategy, buy_or_sell, amt_USD, amt_crypto, product_name):
        now = datetime.datetime.now()
        new_log = bot_log.create(timestamp = now, when_strategy = when_strategy, how_much_strategy = how_much_strategy, buy_or_sell = buy_or_sell, amt_USD = amt_USD, amt_crypto = amt_crypto, product_name = product_name)
        new_log.save()


    def implement_strategy(self, strategy_object, last_trade_call, last_fill_call):
        self.strategy = strategy_object
        side = "dummy"
        buy_choice = self.strategy.choose_to_buy(last_trade_call, last_fill_call )
        sell_choice = self.strategy.choose_to_sell()
        return buy_choice, sell_choice, side

    #get_product_ticker()
