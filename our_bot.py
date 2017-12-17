from connect_to_gdax import *
from bot_log import *

class OurBot(gdax.AuthenticatedClient): #something similar should inherit from authclient

    def log_in_db(self, trade_model, buy0_sell1, amt_USD, amt_crypto, crypto_name):
        new_log = bot_log(trade_model, buy0_sell1, amt_USD, amt_crypto, crypto_name)
        new_log.save()


    def implement_strategy(self, strategy_object, last_trade, last_order):
        self.strategy = strategy_object
        buy_choice = self.strategy.choose_to_buy()
        sell_choice = self.strategy.choose_to_sell()
        return buy_choice, sell_choice

    #get_product_ticker()
