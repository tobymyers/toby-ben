from connect_to_gdax import *
from our_bot import *
from bot_log import *
from many_small_transactions import *
from fixed_coin import *

ob = OurBot(api_key, api_secret, passphrase)

def main(product_name):

    ob = OurBot(api_key, api_secret, passphrase)
    when_strategy = ManySmall()#make a list here
    how_much_strategy = FixedCoin(0.01)
    count = 0

    while True:

        last_trade_call = ob.get_product_trades(product_name)
        last_fill_call = ob.get_fills(product_id=product_name)
        buy_choice, sell_choice, side = ob.implement_strategy(when_strategy, last_fill_call, last_trade_call, count)
        print("buychoice:", buy_choice, "sellchoice:", sell_choice)

        if buy_choice == True:

            avg_trade_price = round(when_strategy.parse_get_product_trades(last_trade_call), 2)
            buy_response = ob.ensure_buy(avg_trade_price, product_name, how_much_strategy.get_bid_amount())
            ob.log_in_db(str(when_strategy), "how_much_strategy", "buy", buy_response["price"], buy_response["size"], product_name)
            #problem here is that I don't know when my orders are filled
        
        if sell_choice == True:
            avg_trade_price = round(when_strategy.parse_get_product_trades(last_trade_call), 2)
            sell_response = ob.ensure_sell(avg_trade_price, product_name, how_much_strategy.get_bid_amount())
            ob.log_in_db(str(when_strategy), "how_much_strategy", "sell", sell_response["price"], sell_response["size"], product_name)

        time.sleep(5)
        count+=1


if __name__ == '__main__':
    main("LTC-USD")



#things that are broken:
#timestamp isn't printing seconds
#implement_strategy isn't working right
