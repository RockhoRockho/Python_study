class Foo:
    def func1():
        print('function1')
    def func2(self):
        print('function2')

f1 = Foo()

f1.func2()
Foo.func2(f1) # 클래스 이름으로 호출
# Foo.func2() # 에러

Foo.func1()   # 클래스 이름으로 호출가능

f = Foo() # 인스턴스 만들어서 func1() 호출하면
# f.func1() # ?? ==> 어떻게 호출됨? Foo.func1(f)

# ------------------------------------------
# id 값
# 인스턴스의 주소

print('-' * 20)

class Foo:
    def __init__(self, name='noname'):
        self.name = name

    def set_name(self, name):
        print('이름 변경:', self.name, '->', name)
        self.name = name

    def func1():
        print('function1')

    def func2(self):
        print(id(self))
        print('function2')

f1 = Foo()
f2 = Foo()

print(id(f1), id(f2))       # 다른 인스턴스다
print(type(f1) == type(f2)) # 타입만 같을뿐

print(f1.name, f2.name)
f1.set_name('John')     # Foo.set_name(f1, 'John')  f1이 self로 전달
f2.set_name('Susan')
print(f1.name, f2.name)


f1.func2()
f2.func2()

# -------------------------------------
# namespace

# 클래스와 인스턴스의 차이를 정확히 이해하는 것은 매우 중요합니다.
# 이를 위해서는 먼저 네임스페이스라는 개념을 알아야 합니다

# 네임스페이스라는 것은 변수가 객체를 바인딩할 때 그 둘 사이의 관계를 저장하고 있는 공간을 의미
# 예를 들어,'a = 2'라고 했을 때  a 라는 변수가 '2 라는 객체'가 저장된 주소를 가지고 있는데
# 그러한 연결 관계가 저장된 공간이 바로 네임스페이스

# 파이썬의 클래스는 새로운 타입(객체)을 정의하기 위해 사용되며,
# 모듈과 마찬가지로 하나의 네임스페이스를 가집니다

class Stock:
    market = 'kospi'

print('-' * 20)

# 현재 스코프의 name들의 str list로 리턴
print(dir())
print(Stock)    # 에러 안난다. 왜? Stock이라는 name이 있기 때문
# print(xxx)    # namespace에 없는 이름

# 클래스를 정의하면 독립적인 네임스페이스 생성됨

# 클래스 내에 정의된 변수나 메소드는 해당 네임스페이스 안에 dict 형태로 저장

# Stock
# ┗ {'market':'kospi'}

import pprint
pprint.pprint(Stock.__dict__)

# 따라서, 해당 '클래스의 네임'으로 클래스 변수나 클래스 메소드 접근 가능]
print(Stock.market)

# -----------------------------------------------------------
# 인스턴스를 생성하면 인스턴스별로 별도의 네임스페이스 생성유지
s1 = Stock()
s2 = Stock()
print(id(s1), id(s2))

pprint.pprint(dir())

print(s1.__dict__, s2.__dict__) # 비어있다!!

print(s1.market)    # 그런데 s1으로 market 사용이 가능하다!?

# 현재 네임스페이스

# Stock
# ┗ {'market':'kospi'}

# s1 (instance)     <-- s1 라는 네임스페이스
# ┗ {}

# s2 (instance)     <-- s2 라는 네임스페이스
#  ┗ {}


# s1으로 market이라는 이름을 접근하면
#   우선 인스턴스의 네임스페이스에서 찾으려 하고
#   없었으면 클래스의 네임스페이스에서 찾는다.


s1.market = 'nasdaq'
print(s1.__dict__)

# 현재 네임스페이스

# Stock
# ┗ {'market':'kospi'}

# s1 (instance)     <-- s1 라는 네임스페이스
# ┗ {'market':'kosdaq'}

# s2 (instance)     <-- s2 라는 네임스페이스
#  ┗ {}

print('s1.market:', s1.market)
print('s2.market:', s2.market)

# 파이썬 오브젝트 이름 찾는 순서
# 우선 인스턴스의 네임스페이스 검색
# ★ 인스턴스의 네임스페이스에 해당 이름이 없으면 클래스의 네임스페이스로 이동.
#  클레스 네임스페이스에도 없으면 super (부모) 네임스페이스 를 찾는다

# 위와 같이 다 뒤지고 이름이 없으면 AtrributeError 발생
# print(Stock.volume)
# print(s2.volume)
























