from pykis import PyKis, KisAuth, KisBalance,KisQuote
class private_kis:
  def __init__(self):
    self.token = None
    self.kis = None

  def connect_token(self, token_path):
    self.kis = PyKis(token_path, keep_token = True)
    self.kis = PyKis(KisAuth.load(token_path), keep_token = True)
    token_kis = self.kis
    return token_kis # 연결된 객체를 반환함

class private_account:
  def __init__(self, kis):
    self.account = None
    self.Kis = kis

  def connect_account(self):
    self.account = self.Kis.account()
    balance: KisBalance = self.account.balance()
    return balance

class KIS_stock:
  def __init__ (self, kis):
    self.stock = None
    self.kis = kis # connect_token 에서 반환된 연결된 token임

  def connect_stock(self, name):
    self.stock = self.kis.stock(name) # name 에 해당하는 주식과 객체를 연결함.

  def search_stock(self):
    quote: KisQuote = self.stock.quote() # name으로 저장된 주식을 반환함
    quote: KisQuote = self.stock.quote(extended = True)
    return quote
  
sp100_tickers = [
    "AAPL","MSFT", "AMZN", "TSLA", "NVDA", "META", "JNJ", "GOOGL","V",
    "XOM", "PG", "CVX", "PFE", "KO", "INTC", "WMT", "MCD", "PEP", "HD", "ABBV",
    "VZ",]
    # "ABT", "CRM", "DIS", "NKE", "MRK", "BMY", "TXN", "LMT", "ORCL", "AMGN",
    # "CVS", "HON", "UNH", "GE", "MMM", "GS", "CAT", "MDT", "NKE", "HD", "PFE",
    # "BLK", "MS", "CL", "RTX", "JCI", "GM", "BA", "LLY", "NEE", "D", "TMUS",
    # "AXP", "PM", "COP", "LUMN", "SPGI", "IBM",
    # "SCHW", "MCD", "HSY", "BIIB",
    # "AMD", "TMUS", "BMY", "LLY", "CI", "MS", "HPE", "MAR", "DAL", "AIG",
    # "UPS", "SYY", "CI", "SLB", "CTSH", "CTVA", "MOS", "ILMN", "EXC", "DIS",
    # "ANTM", "BLK", "KR", "LLY", "REGN", "LUMN", "QCOM", "GD", "AZN", "WFC",
    # "C", "LMT", "CB", "ANTM", "AMT", "WM"

json = []
p_kis = private_kis()
p_stock = p_kis.connect_token('secret.json') #json 파일로 저장된 secret key를 통해 api 연결
for name in sp100_tickers:
  kis_stock = KIS_stock(p_stock)
  kis_stock.connect_stock(name)
  stock_data = kis_stock.search_stock()
  dic_data = {
    "CODE":name,
    "NAME":stock_data.name,
    "PER":float(stock_data.indicator.per),
    "PBR":float(stock_data.indicator.pbr),
    "eps":float(stock_data.indicator.eps),
    "bps":float(stock_data.indicator.bps)
  }
  print(dic_data)
  json.append(dic_data)