from base_when_strategy import *

class ManySmall(BaseWhenStrategy):

    def choose_to_buy(self, last_fill_call, last_trade_call):
        change_since_last_fill= self.get_change_since_last_fill(last_fill_call, last_trade_call)
        short_term_price_change = self.get_short_term_price_change( last_trade_call)#I know first last trade is confusing.  need a better way
        print(change_since_last_fill, "change since last fill")
        if change_since_last_fill < 1:
        #if self.short_term > small amount  and last transaction was a sell:
        #all complicated code lives here
            return True, "buy"
        else:
            print("in else")
            return True
    def choose_to_sell(self):
        #if self.short_term > small amount  and last transaction was a sell:
        #all complicated code lives here
        # if change_since_last_fill > 1:
        #     return True, "sell"
        return False
