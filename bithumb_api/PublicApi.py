from .BithumbMethod import BithumbMethod

def ticker(order_currency, payment_currency="KRW"):
    url = "/public/ticker/{}_{}".format(order_currency, payment_currency)
    return BithumbMethod().get(url)

def orderbook(order_currency, payment_currency="KRW", limit = 5) :
    url = "/public/orderbook/{}_{}?count={}".format(order_currency,payment_currency,limit)
    return BithumbMethod().get(url)

def candlestick(order_currency, payment_currency="KRW", chart_instervals = "24h") :
    url = "/public/candlestick/{}_{}/{}".format(order_currency, payment_currency, chart_instervals)
    return BithumbMethod().get(url)
