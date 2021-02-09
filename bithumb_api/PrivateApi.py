def __init__(self, conkey, seckey) :
    self.req = BithumbMethod(conkey, seckey)
    
def balance(self, **kwargs) :
    return self.req.post('/info/balance', **kwargs)

def place(self, **kwargs) :
    return self.req.post('/trade/place', **kwargs)

def orders(self, **kwargs) :
    return self.req.post('/info/orders', **kwargs)

def order_detail(self, **kwargs) :
    return self.req.post('/info/order_detail', **kwargs)

def market_buy(self, **kwargs) :
    return self.req.post('/trade/market_buy', **kwargs)

def market_sell(self, **kwargs) :
    return self.req.post('/trade/market_sell', **kwargs)

def cancel(self, **kwargs) :
    return self.req.post('/trade/cancel', **kwargs)
