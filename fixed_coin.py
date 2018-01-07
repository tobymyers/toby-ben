class FixedCoin:
    def __init__(self, number_of_coins):
        self.number_of_coins = number_of_coins

    def get_bid_amount(self):
        return self.number_of_coins
