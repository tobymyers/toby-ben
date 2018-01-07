from base_when_strategy import *

class ManySmall(BaseWhenStrategy):

    def choose_to_buy(self, last_fill_call, last_trade_call, count):
        change_since_last_fill, side = self.get_change_since_last_fill(last_fill_call, last_trade_call)
        short_term_price_change = self.get_short_term_price_change( last_trade_call, count)#I know first last trade is confusing.  need a better way

        if change_since_last_fill < -0.03 and str(side) == "sell": #if it goes down 3%
            return True
        else:
            return False


    def choose_to_sell(self,last_fill_call, last_trade_call, count):

        change_since_last_fill, side = self.get_change_since_last_fill(last_fill_call, last_trade_call)
        short_term_price_change = self.get_short_term_price_change( last_trade_call, count)#I know first last trade is confusing.  need a better way

        if change_since_last_fill > 0.03 and str(side) == "buy": #if it goes dow 3%
            return True
        else:
            return False
