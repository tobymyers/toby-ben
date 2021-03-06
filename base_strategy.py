#class

class BaseWhenStrategy:
    """base class to inform extensions for deciding when to buy"""

    def __init__(self, current_price):
        self.current_price = current_price

    def parse_get_product_trades(self, api_response):
        last_trades = 0
        trade_data = api_response
        for trade in trade_data:
            last_trades += float(trade["price"])
        avg_trade_price = last_trades / len(trade_data)
        return avg_trade_price

    def parse_get_fills(api_response):
        last_order = api_response[0][0]
        return last_order["product_id"], last_order["price"]

    def get_change_since_last_fill(self, last_fill_price):
        change = (self.current_price - last_fill_price)/last_fill_price
        return change

    def get_short_term_price_change(self, new_price #all the parsed call stuff parsed_call):
        self.last_price = last_order_price #should be a dummy value that's not going to screw things up
        change = (current_price - last_order_price)/last_order_price
        self.last_price = new_price
        return change
#^^the above should take the old price, compare it to the new price, get the percentage change, and set the old_price to be the new price_change_since_last_transactions
