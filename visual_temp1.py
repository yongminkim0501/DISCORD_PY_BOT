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

import matplotlib.pyplot as plt
import numpy as np

name = []
per = []

for stock in dic_data:
    name.append(stock["CODE"])
    per.append(stock["PER"])

plt.plot(name, per)
plt.show()

plt.bar(name,per) 
plt.show()

plt.scatter(name,per) 
plt.show()

plt.barh(name,per) 
plt.show()

plt.fill_between(name,per) 
plt.show()