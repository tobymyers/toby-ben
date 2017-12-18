from base_when_strategy import *

class ManySmall(BaseWhenStrategy):

    def choose_to_buy(self):
        #if self.short_term > small amount  and last transaction was a sell:
        #all complicated code lives here
        return True, "buy"

    def choose_to_sell(self):
        #if self.short_term > small amount  and last transaction was a sell:
        #all complicated code lives here
        return True, "sell"
