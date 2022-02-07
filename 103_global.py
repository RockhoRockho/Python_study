# global variable, global scope
# 함수 바깥에서 선언한 변수.
# 스크립트 전체에서 접근할 수 있는 변수를 전역 변수(global variable)라고 부릅니다.
# 특히 전역 변수에 접근할 수 있는 범위를 전역 범위(global scope)라고 합니다

x = 10 # 전역 변수 (global variable)

def foo():
    print(x) # 함수 안에서는 전역변수 '사용' 가능. : '읽기동작'은 가능!

foo()
print('x =', x)

# local variable, local scope
def foo():
    y = 10      # foo의 지역변수
    print(y)    # foo의 지역변수 y를 출력
foo()
# print('y =', y) # 에러! foo의 지역변수는 함수 바깥에서 출력할 수 없음

# foo의 지역 변수(local variable)입니다.
# 따라서 지역 변수는 변수를 만든 함수 안에서만 접근할 수 있고,
# 함수 바깥에서는 접근할 수 없습니다. 지역 변수가 접근할 수 있는 범위를 지역 범위(local scope)라 한다

z = 10 # 전역변수
def foo():
    z = 20 # '쓰기' 동작. 이는 foo()의 지역변수 z로 선언되고 초기화 됨.
    print('foo() z =', z)
foo()
print('전역 z =', z)  # 전역변수 z는 수정되지 않았다.

# ------------------------------------------------------------------------

a = 1   # 전역변수

def vartest(a):     # a는 vartest()안에서 사용하는 지역변수 a
    a = a + 1       # 지역변수 a 수정
    print('vartest() a =', a)   # 지역변수 a 출력
    # 함수 종료되면 지역변수 a는 소멸

vartest(a)
print('전역 a=', a)


# --------------------------------------------------------------
print('-' * 20)

#  함수를 통해 전역변수 값을 '변경'하고 싶다면!
#   방법1 : return 값 활용 (추천)
#   방법2 : global 키워드 사용 (비추)

# 방법1
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)  # 리턴된 값으로 전역변수 a값을 변경한다.
print('전역 a =', a)

# 방법2
a = 1
def vartest():  # 매개변수 없다
    global a    # 이 함수 안에서 전역변수 a를 사용하겠다고 선언
    a = a + 1
    print('vartest() a =', a)   # 전역변수 a
vartest()
print('전역 a =', a)  # 변경되어 있다!

# 전역변수가 없는 상태에서 global 을 사용하면??
def foo():
    global q  # q 라는 전역변수가 없으면, 새로이 전역변수를 만듦.
    q = 20    # q 는 전역변수
    print('foo() q =', q)

foo()
print('전역 q =', q)  # 없었던 전역변수 q 가 foo() 를 통해 생김.


# global 로 선언할 name 은 반드시 그 name 이 사용하기 '전' 에 global 선언되어야 함.
k = 10
def foo():
    k = 20
    print('foo() k =', k)
    # global k  # SyntaxError: name 'k' is used prior to global declaration

foo()
print('전역 k =', k)

# ---------------------------------------------------------
print('-' * 20)

# 네임스페이스 (name space)
#   특정 이름들이 사용되는 프로그래밍 영역
import pprint

x = 10
pprint.pprint(locals())         # 전역 네임스페이스


def foo():
    x = 20
    print('foo() x =', x)
    c = 10
    b = 20
    d = 40
    pprint.pprint(locals())     # 로컬 네임스페이스

foo()


























