from connect_to_gdax import *
from our_bot import *
from bot_log import *
from many_small_transactions import *

ob = OurBot(api_key, api_secret, passphrase)

def main(product_name):

    ob = OurBot(api_key, api_secret, passphrase)
    when_strategy = ManySmall()#make a list here

    while True:
        last_trade_call = ob.get_product_trades(product_name)
        last_fill_call = ob.get_fills(product_id=product_name)
        buy_choice, sell_choice, side = ob.implement_strategy(when_strategy, last_fill_call, last_trade_call)
        print(buy_choice, "buychoice")
        if buy_choice == True:
            side = "BUY"
            print("in buy choice")
            #calculate amount of money later
            #ob.buy(#buying params from api doc)
            ob.log_in_db(str(when_strategy), "how_much_strategy", side, 00, 00, product_name)

        if sell_choice == True:
            side = "SELL"
            ob.log_in_db(str(when_strategy), "how_much_strategy", side, 00, 00, product_name)
        #     #calculate amount of money later
        #     ob.sell(#selling params from api doc)
        #     ob.log_in_db(trade_model, buy0_sell1, amt_USD, amt_crypto, crypto_name):

        time.sleep(5)

if __name__ == '__main__':
    main("LTC-USD")



#things that are broken:
#timestamp isn't printing seconds
#implement_strategy isn't working right
