# 모듈(module) =  함수 + 변수 + 클래스 를 모아놓은 '파이썬 파일(*.py)'

# 한번 만들어 놓으면 다른 파이썬 프로그램에서 불러와서 사용 가능
# 다른 사람들이 만들어 놓은 파이썬 프로그램을 내 프로그램에 불러와 사용 가능

# ------------------------------------
# import

# 모듈 불러오는 구문
#    import 모듈이름

# import는 '현재 디렉터리'에 있는 파일이나
# '파이썬 라이브러리가 저장된 디렉터리'에 있는 모듈만 불러올 수 있다.)

import sys
import pprint
pprint.pprint(sys.path)

import mod0 # 현재 디렉토리의 mod0.py 모듈을 불러옴
# import mod0.py (X)

# import한 모듈명을 사용하여 모듈의 변수, 함수, 클래스를 사용할 수 있다.
print(mod0.myname)

mod0.my_func(10, 20, 30)
my = mod0.MyClass() # MyClass객체 생성
print(my)

# -------------------------------------------
# 모듈의 상대 경로

# import mod1 # 현재 경로 안에서는 mod1.py가 없다.

# 현재 디렉토리 기준으로 Mymodules 디렉토리 밑의 mod1.py 모듈을 불러옴
import Mymodules.mod1
# 모듈명 : Mymodules.mod1

result = Mymodules.mod1.add(10, 20)
print('result = ', result)

# -------------------------------------------
# 패키지란?
# import Mymodules.mod1  <-- 라고 하면..
# 경로에 해당하는 Mymodules 는 '패키지명' 이고, mod1 은 '모듈명' 이다.

# 만약
# import aaa.bbb.dd.kkk  <-- 인 경우
# aaa.bbb.dd. 가 패키지명이고 kkk 가 모듈명이다.
# 즉 상대적인 경로로 aaa/bbb/dd  디렉토리 밑의 kkk.py 파이썬 파일을 불러오는 것이다

# --------------------------------------------------------
# as
#   긴 ~ 이름의 모듈을 as를 사용하여 짧은 별명으로 사용할 수 있다.

import Mymodules.mod1 as my
result = my.add(20, 31)
print('reuslt =', result)

# --------------------------------------------------------
# from 모듈이름 import 모듈함수/변수/클래스

# 모듈이름을 매번 붙이는게 번거롭다면
# 자주 사용하는 함수(변수, 함수, 클래스) 에 대해

#  다음과 같이 불러올수 있다
#  from 모듈이름 import 변수이름 혹은 함수이름 혹은 클래스이름

from Mymodules.mod1 import add
result = add(10, 16) # 모듈명 없이도 add() 사용 가능
print('result =', result)

# 여러개의 이름을 동시에 import 가능.
from mod0 import myname, my_func

from mod0 import * # * 모든 이름을 import 할 수 있다.
print(myname)
my_func(11, 22, 33)

print(__name__)
