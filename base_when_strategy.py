#class

class BaseWhenStrategy:
    """base class to inform extensions for deciding when to buy, you must call parse_get_fills before get_short_term_price_change"""

    def __init__(self):
        self.last_price = 1 #need to fix this

    def get_last_fill_price(self):
        last_fill = last_fill_call[0][0]
        return last_fill["price"]

    # def parse_get_product_trades(self, last_trade_call):
    #     last_trades = 0
    #     trade_data = last_trade_call
    #     for trade in trade_data:
    #         last_trades += float(trade["price"])
    #     avg_trade_price = last_trades / len(trade_data)
    #     print( avg_trade_price ,"avg_trade_price")
    #     return float(avg_trade_price)

    def parse_get_product_trades(self, last_trade_call):
        last_trade_price = float(last_trade_call[0]["price"])
        print(last_trade_price, "last trade price")
        return last_trade_price

    def parse_get_fills(self, last_fill_call):
        self.last_fill = last_fill_call[0][0]
        return self.last_fill["product_id"],float(self.last_fill["price"]), self.last_fill["side"]

    def get_change_since_last_fill(self, last_fill_call, last_trade_call):
        self.current_price = float(self.parse_get_product_trades(last_trade_call))
        product_id, self.last_fill_price, self.side = self.parse_get_fills(last_fill_call)
        change = (self.current_price - self.last_fill_price)/self.last_fill_price
        print(change, "change since last fill")
        print(self.last_fill_price, "self.last_fill_price")
        return change, self.side

    def get_short_term_price_change(self, last_trade_call, count): #this is currently broken
        if count == 0:
            self.last_price = self.parse_get_product_trades(last_trade_call)
        current_price = self.parse_get_product_trades(last_trade_call)
        change = (current_price - float(self.last_price))/float(self.last_price)
        self.last_price = current_price
        print(change, "change since last call")
        print(count, "count")
        return change
#^^the above should take the old price, compare it to the new price, get the percentage change, and set the old_price to be the new price_change_since_last_transactions
