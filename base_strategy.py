#class

class BaseWhenStrategy:
    """base class to inform extensions for deciding when to buy"""

    def __init__(self, short_term_price_change, price_change_since_last_transaction):
        self.short_term = short_term_price_change
        self.since_last = price_change_since_last_transaction

    def parse_get_product_trades(self, api_response):
        #parse the stuff
        return price, #all the other things I care about from the call

    def parse_get_orders(self, api_response):
        #parse the stuff
        return price, #all the other things I care about from the call

    def get_change_since_last_order(self, parsed_order):
        self.last_order = #last order price, sell or buy, currency, etc in list
        change = (current_price - last_order_price)/last_order_price
        return change

    def get_short_term_price_change(self, new_price #all the parsed call stuff parsed_call):
        self.last_price = last_order_price #should be a dummy value that's not going to screw things up
        change = (current_price - last_order_price)/last_order_price
        self.last_price = new_price
        return change
#^^the above should take the old price, compare it to the new price, get the percentage change, and set the old_price to be the new price_change_since_last_transactions
