from connect_to_gdax import *
from our_bot import *
from bot_log import *
from many_small_transactions import *

ob = OurBot(api_key, api_secret, passphrase)


def main(product_name):

    ob = OurBot(api_key, api_secret, passphrase)

    while True:
        last_trade = ob.get_product_trades(product_name)
        last_fill = ob.get_fills(product_name)
        when_strategy = ManySmall()
        buy_choice, sell_choice, side = ob.implement_strategy(when_strategy, last_fill, last_trade)
        buy_choice = True
        if buy_choice == True:
            print("in buy choice")
            #calculate amount of money later
            #ob.buy(#buying params from api doc)
            ob.log_in_db(str(when_strategy), "dummy", side, 00, 00, product_name)

        # if sell_choice == True:
        #     #calculate amount of money later
        #     ob.sell(#selling params from api doc)
        #     ob.log_in_db(trade_model, buy0_sell1, amt_USD, amt_crypto, crypto_name):

        time.sleep(5)

if __name__ == '__main__':
    main( "LTC-USD")



#things that are broken:
#timestamp isn't printing seconds
#implement_strategy isn't working right
