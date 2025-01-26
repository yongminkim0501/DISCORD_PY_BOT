import math as math
from scipy.stats import norm
'''r = 0 # t-bill risk free interest rate
v = 0 # option price
s = 0 # 기초자산가격
k = 0 # 행사 가격
T = 0 # 만기 시점
t = 0 # 현재 시점
T-t # 잔존 만기
sigma = 0 # 기초 자산 변동성'''
# r = risk free interest rate => t - bill (United States Treasury securitie)
# 미국의 재무부 증권 - 어떤 금리를 고를 지는 만기일자에 맞게 고르면 될 것으로 예상됨.
def black_shores_call(s,d_1,k,r,T,t,d_2):
  call = s * norm.cdf(d_1) - k * math.exp(-r * (T-t)) * norm.cdf(d_2)
  return call

def black_shores_put(k,r,T,t,d_2,d_1,s):
  put = k * math.exp(-r * (T-t)) * norm.cdf(-d_2) - s * norm.cdf(-d_1)
  return put

def get_d1(s,k,r,sigma, T):
  d1 = (math.log(s/k) + (r + (sigma ** 2) / 2) * T) / sigma * math.sqrt(T-t)
  return d1

def get_d2(d_1, sigma, T, t):
  d2 = d_1 - sigma * math.sqrt(T-t)
  return d2

def get_delta(d1):
  # delta가 0.5라면, 기초자산이 1% 움직일 때, 옵션의 가격은 0.5% 변동한다는 의미
  # 콜 옵션 매수 포지션의 경우 0 ~ 1 사이의 값으로 나타냄, 내가격 (ITM)일수록 1에 가깝고
  # 외가격 (OTM)일수록 0에 가까운 델타값을 가지게 된다.
  # 내가격이란, 시장가격 > 행사가격 -> 권리 포기
  # 외가격이란, 시장가격 < 행사가격 -> 권리 사용
  # 행사 가능성이 높을수록 기초 자산 가격변동에 옵션 가격이 민감하게 움직이고
  # 행사 가능성이 낮을수록 기초 자산과 옵션 가격의 correlation이 낮다는 말이 됨
  return norm.cdf(d1) / (norm.cdf(d1) - 1)

def get_gamma(s,d_1,sigma,T,t):
  # 기초 자산 가격의 변동 대비 델타의 변동을 나타냄
  # 기초 자산의 가격과 델타와의 상관관계를 나타냄
  return (norm.pdf(d_1) / (s * sigma * math.sqrt(T-t)))

def get_setta_call(s,d_1,sigma,T,t,r,k,d_2):
  # 시간에 따른 옵션가격의 변동률을 나타냄
  # 블랙 숄즈 방정식을 t(시간)으로 편미분하여 세타 구함
  # t가 0에 가까울수록, 만기가 가까워질수록 세타는 가파르게 떨어짐
  setta_call = -(s * norm.pdf(d_1) * sigma) / (2 * math.sqrt(T-t)) - r * k * math.exp(-r*(T-t)*norm.cdf(d_2))
  return setta_call

def get_setta_put(s, d_1, sigma, T, t, r, k, d_2):
  setta_put = -(s * norm.pdf(d_1) * sigma) / (2 * math.sqrt(T-t)) + r * k * math.exp(-r*(T-t))*(norm.cdf(-d_2))
  return setta_put

def get_vega(s,T,t,d_1):
  # 기초 자산의 변동성의 변화 대비 옵션가격의 변동률을 나타냄
  # 베가는 변동성이 낮을수록 옵션가격의 민감도가 높음
  vega = s*math.sqrt(T-t)*(norm.pdf(d_1))
  return vega

def get_rho_call(k,T,r,t,d_2):
  # 이자율의 변동 대비 옵션 가격의 변동률을 나타내줌
  rho_call = k*T*math.exp(-r*(T-t))*norm.cdf(d_2)
  return rho_call

def get_rho_put(k,T,r,t,d_2):
  # 이자율의 변동은 자주 일어나는 일은 아니어서 실제 트레이딩에서는 거의 사용 x이지만,
  # 알아두는 것 중요
  rho_put = -k * T * math.exp(-r*(T-t))*norm.cdf(-d_2)
  return rho_put