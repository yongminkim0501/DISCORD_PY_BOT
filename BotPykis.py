from pykis import PyKis, KisAuth, KisBalance, KisQuote

class get_set_connect_pykis:
    def __init__(self):
        self.kis = None
        self.stock = None

    def set_real_pykis(self, token_path):
        self.kis = PyKis(token_path, keep_token = True)
        self.kis = PyKis(KisAuth.load(token_path), keep_token = True)

    def get_pykis(self):
        return self.kis
    
    def search_stock_name(self, stock_name):
        self.stock = self.kis.stock(stock_name)
        quote: KisQuote = self.stock.quote()
        quote: KisQuote = self.stock.quote(extended = True)
        return quote