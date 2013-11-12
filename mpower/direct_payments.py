"""MPower Payments DirectCard"""
from .core import Payment

class DirectCard(Payment):
    """DirectCard processing class
    
    This class handle billing of clients using their credit card information
    Card info format:
       '{ "card_name" : "Alfred Robert Rowe", 
          "card_number" : "4242424242424242", "card_cvc" : "123", 
          "exp_month" : "06", "exp_year" : "2010", "amount" : "300" 
        }'
    """
    def __init__(self, card_info={}, configs={}):
        self.card_info = card_info
        super(DirectCard, self).__init__(configs)
    
    def process(self, card_info=None):
        """proces the direct card billing transaction"""
        return self._process('direct-card/processcard', card_info or self.card_info)


class DirectPay(Payment):
    """Directpay processing class
    
    Receipient account_info format:
    '{ "account_alias" : "0244124660", "amount" : 30.50 }'
    """
    def __init__(self, account_alias=None, amount=None, configs={}):
        self.transaction = {'account_alias': account_alias, 'amount': amount}
        super(DirectPay, self).__init__(configs)

    def process(self, transaction):
        """Process the transaction"""
        return self._process('direct-pay/credit-account', transaction or  self.transaction)
