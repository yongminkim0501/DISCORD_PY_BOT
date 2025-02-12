from BotPykis import *
from bot import *
import discord, json
from option_function.black_shores_option import *

def kis():
    connect_pykis = get_set_connect_pykis()
    connect_pykis.set_real_pykis("secret.json")

    token = connect_discord("config.json")
    discord_bot = set_discord()
    discord_bot.set_discord_bot(connect_pykis)
    discord_bot.start_client(token)

def black_shores_option():
    # 예시 데이터 1: AAPL(애플) 주식 콜옵션 가정
    r = 0.05    # 연간 무위험 이자율 5% (T-bill 기준)
    s = 180     # 현재 주식 가격 $180
    k = 185     # 행사가격 $185 (약간의 외가격 옵션)
    T = 0.5     # 만기 6개월
    t = 0       # 현재 시점
    sigma = 0.25 # 연간 변동성 25%
    d_1 = get_d1(s, k, r, sigma, T, t)
    d_2 = get_d2(d_1, sigma, T, t)

    call_price = black_shores_call(s, d_1, k, r, T, t, d_2)
    put_price = black_shores_put(k, r, T, t, d_2, d_1, s)
    print(f"d_1, d_2, call_price, put_price : {d_1, d_2, call_price, put_price}")

    # 그리스 지표들도 계산해볼 수 있는 예시 데이터 2: TSLA(테슬라) 주식 풋옵션 가정
    r = 0.05     # 연간 무위험 이자율 5%
    s = 250      # 현재 주식 가격 $250
    k = 245      # 행사가격 $245 (약간의 내가격 옵션)
    T = 0.25     # 만기 3개월
    t = 0        # 현재 시점
    sigma = 0.40 # 연간 변동성 40% (테슬라는 변동성이 더 큼)
    d_1 = get_d1(s, k, r, sigma, T, t)
    d_2 = get_d2(d_1, sigma, T, t)

    call_price = black_shores_call(s, d_1, k, r, T, t, d_2)
    put_price = black_shores_put(k, r, T, t, d_2, d_1, s)
    print(f"d_1, d_2, call_price, put_price : {d_1, d_2, call_price, put_price}")

#black_shores_option()
kis()

'''
d_1, d_2, call_price, put_price : (0.03740885015893052, -0.13936784513770636, np.float64(12.469128506987616), np.float64(12.901462232229136))
d_1, d_2, call_price, put_price : (0.06587838414689934, -0.13412161585310067, np.float64(23.494995588438655), np.float64(15.451556709439615))

d_1, d_2가 0에 가깝다는 것 : 옵션이 등가격(ATM) 근처에 있다는 의미
    -> 현재 주가 (s)가 행사가격 (k) 근처에 있음

콜 옵션 가격이 두 번째 케이스에서 크게 상승했는데:
    - 기초 자산 가격이 더 높거나
    - 변동성이 더 크거나
    - 만기가 더 길 수 있음을 시사

풋옵션 가격도 상승했지만 콜옵션 만큼 크게 오르지는 않음
    - 이는 기초자산 가격이 상승했을 가능성을 시사
'''