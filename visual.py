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
  json.append(dic_data)

dic_data = [{'CODE': 'AAPL', 'NAME': '애플', 'PER': 36.92, 'PBR': 52.41, 'eps': 6.3, 'bps': 4.44}
            , {'CODE': 'MSFT', 'NAME': '마이크로소프트', 'PER': 33.14, 'PBR': 10.11, 'eps': 12.42, 'bps': 40.71}
            , {'CODE': 'AMZN', 'NAME': '아마존닷컴', 'PER': 42.15, 'PBR': 8.62, 'eps': 5.52, 'bps': 27.0}
            , {'CODE': 'TSLA', 'NAME': '테슬라', 'PER': 161.16, 'PBR': 14.49, 'eps': 2.04, 'bps': 22.67}
            , {'CODE': 'NVDA', 'NAME': '엔비디아', 'PER': 52.31, 'PBR': 49.39, 'eps': 2.54, 'bps': 2.69}
            , {'CODE': 'META', 'NAME': '메타 플랫폼스(페이스북)', 'PER': 30.09, 'PBR': 9.99, 'eps': 23.92, 'bps': 72.07}
            , {'CODE': 'JNJ', 'NAME': '존슨 앤드 존슨', 'PER': 26.93, 'PBR': 5.36, 'eps': 5.8, 'bps': 29.14}
            , {'CODE': 'GOOGL', 'NAME': '알파벳 A', 'PER': 23.03, 'PBR': 6.96, 'eps': 8.05, 'bps': 26.62}
            , {'CODE': 'V', 'NAME': '비자', 'PER': 35.83, 'PBR': 18.34, 'eps': 9.79, 'bps': 19.13}
            , {'CODE': 'XOM', 'NAME': '엑슨 모빌', 'PER': 14.23, 'PBR': 1.84, 'eps': 7.85, 'bps': 60.58}
            , {'CODE': 'PG', 'NAME': '프록터 앤드 갬블', 'PER': 26.99, 'PBR': 7.89, 'eps': 6.28, 'bps': 21.49}
            , {'CODE': 'CVX', 'NAME': '셰브론', 'PER': 16.23, 'PBR': 1.81, 'eps': 9.7, 'bps': 86.92}
            , {'CODE': 'PFE', 'NAME': '화이자', 'PER': 18.13, 'PBR': 1.57, 'eps': 1.41, 'bps': 16.29}
            , {'CODE': 'KO', 'NAME': '코카콜라', 'PER': 28.08, 'PBR': 10.99, 'eps': 2.41, 'bps': 6.15}
            , {'CODE': 'INTC', 'NAME': '인텔', 'PER': 4.8, 'PBR': 0.91, 'eps': 4.37, 'bps': 22.93}
            , {'CODE': 'WMT', 'NAME': '월마트', 'PER': 42.08, 'PBR': 9.34, 'eps': 2.44, 'bps': 10.97}
            , {'CODE': 'MCD', 'NAME': '맥도날드', 'PER': 27.23, 'PBR': 0.0, 'eps': 11.39, 'bps': 0.0}
            , {'CODE': 'PEP', 'NAME': '펩시코', 'PER': 20.96, 'PBR': 11.08, 'eps': 6.95, 'bps': 13.15}
            , {'CODE': 'HD', 'NAME': '홈 디포', 'PER': 28.29, 'PBR': 71.46, 'eps': 14.72, 'bps': 5.83}
            , {'CODE': 'ABBV', 'NAME': '애브비', 'PER': 80.02, 'PBR': 56.2, 'eps': 2.4, 'bps': 3.41}
            , {'CODE': 'VZ', 'NAME': '버라이존 커뮤니케이션스', 'PER': 9.78, 'PBR': 1.72, 'eps': 4.14, 'bps': 23.57}]

