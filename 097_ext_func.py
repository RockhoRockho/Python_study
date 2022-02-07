# 1. built-in : import 없이 사용가능
# 2. import 를 사용하여 가져온뒤 사용가능한 함수
# 3. 추가 설치 후에 import 하여 사용 가능한 함수들
#      pip, conda ...

# 파이썬 설치시 '기본적'으로 설치된 라이브러리로부터 사용 가능한 함수들

# 라이브러리(library) 란 파이썬 프로그래밍에 사용가능한 프로그램을을 모아놓은 것.

# https://docs.python.org/3/library/index.html    <-- Python Standard Library

# --------------------------------------------------------------------
# time 모듈

import time

# 1970.1.1 00:00:00 초 기준으로 경과한 시간 (초)   타임스탬프(time stamp) 라고도 한다
print(time.time())

# 현재시간 연도 , 월, 일  시, 분, 초, 요일... 의 형태로 변환
print(time.localtime())

# 특정 타임스탬프 값을 매개변수로 받을수 있다.
print(time.localtime(time.time()))
print(time.localtime(0))

# 현재 날짜, 시간값 추출
t = time.localtime()
print(t.tm_year)
print(t.tm_mon)
print(t.tm_mday)

# timestamp 를 str 으로 변환
now = time.localtime()

print(time.strftime('%x', now))
print(time.strftime('%c', now))
print(time.strftime('%c'))  # 현재시간에 대한 문자열 변환시 굳이 두번째 매개변수 필요없슴.
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y년 %m월 %d일 %H시%M분%S초'))

# str -> timestamp 변환
from datetime import datetime

dt = datetime(year=2020, month=9, day=13)
print(dt)
print(type(dt))

date_string = '2018-07-23 18:59:09'
timestamp = time.mktime(datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S').timetuple())
print(timestamp)

# datetime -> timestamp 변환
print(datetime.today())
print(datetime.today().timetuple())
timestamp = time.mktime(datetime.today().timetuple())
print(timestamp)

# str -> datetime 변환
dt = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
print(dt, type(dt))

# timestamp -> datetime 변환
d = datetime.fromtimestamp(1532339949.0)
print(d, type(d))

# -----------------------------------------------------------
# 경과시간 측정 (elapsed time)
start_time = time.time()

for i in range(5):
    print(i)
    # time.sleep(2) # 2 sec 딜레이 주기


end_time = time.time()
elapsed_time = end_time - start_time # 경과시간
print(f'---- {elapsed_time} sec ----')

# 경과시간을 시:분:초  로 나타내려면?

# 물론 일일히 계산 할수도 있다.. 3600 나눈몫이 경과 시간이고..
# 다시 나머지로... 분, 초 계산하고

# 그러나, 파이썬에서는 이를 위한 timedelta 함수가 있다
# 활용할수 있으면 활용하자

from datetime import timedelta

print(timedelta(seconds=36542.23))

# -------------------------------------
# random 모듈
print('-' * 20)
import random

for i in range(10):
    print(random.random()) # 0.0 <= <1.0 사이의 난수값 리턴

print()

for i in range(10):
    print(random.randint(1, 10)) # 1 <= <= 10 정수난수값 리턴

data =[1, 2, 3, 4, 5]
print('data =', data)
v = data.pop() # 리스트에서 데이터 추출(제거된 값이 리턴됨)
print('pop data =', v)
print('data =', data)   # 원본 변화된다.
v = data.pop()
print('pop data =', v)
print('data =', data)   # 원본 변화된다.

data = [1, 2, 3, 4, 5]

def random_pop(d):
    idx = random.randint(0, len(d) -1)
    return d.pop(idx)

while data: print(random_pop(data))

# 연습
# 로또 번호 추출
#  1 ~ 45까지의 숫자중 6개 랜덤 추출
#  (중복 발생하면 안됨!)

data = [i for i in range(1, 46)]
for _ in range(6):
    print(random_pop(data), end=' ')

print()

print()

data = ['dog', 'cat', 'bird', 'fish']
random.shuffle(data) # data가 변화됨
print(data)

print(random.choice(data))
print(random.choice(data))

# 로또 번호 추출(shuffle 사용)
data = [i for i in range(1, 46)]
random.shuffle(data)
print(data[:6])

# ----------------------------------------
# math 모듈
print('-' * 20)
import math
print(math.pi)
print(math.e) # 자연로그

# degree -> radian
print(math.radians(180))
print(math.radians(90))
math.sin(math.radians(30)) # sin 30도

# ----------------------------------------------------------
# sys 모듈
print('-' * 20)
import sys
print(sys.version)
print(sys.maxsize)
print(sys.copyright)
print(sys.path)

# ----------------------------------------------------------
import this

