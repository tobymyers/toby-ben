from connect_to_gdax import *
from our_bot import *
from bot_log import *

ob = OurBot(api_key, api_secret, passphrase)


def main():

    ob = OurBot(api_key, api_secret, passphrase)

    while True:
        last_trade = ob.get_product_trades()
        last_order = ob.get_orders("done")
        buy_choice, sell_choice = ob.implement_strategy(strategy_name, last_order, last_trade)
        if buy_choice == True:
            #calculate amount of money later
            ob.buy(#buying params from api doc)
            ob.log_in_db(trade_model, buy0_sell1, amt_USD, amt_crypto, crypto_name):
              #whatever)
        if sell_choice == True:
            #calculate amount of money later
            ob.sell(#selling params from api doc)
            ob.log_in_db(trade_model, buy0_sell1, amt_USD, amt_crypto, crypto_name):

        time.sleep(5)

if __name__ == '__main__':
    main()
