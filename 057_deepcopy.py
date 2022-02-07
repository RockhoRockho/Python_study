# Assignment VS. Shallow Copy VS. DeepCopy
# 대입연산 vs. 얕은복사 vs. 깊은복사

# --------------------------------------
# 대입연산
#  ★ 대입연산은 '객체복사' 가 아니다
# 생각해보기
a = 10
b = a
print(f'a={a}, b={b}')
print(id(a), id(b)) # id() 변수의 주소값

a += 1
print(f'a={a}, b={b}')
print(id(a), id(b))
#--------------------------------
print('-' * 20)

A = [1, 2, 3]
B = A
print(f'A={A}, B={B}')
print(id(A), id(A[0]), id(A[1]), id(A[2]))
print(id(B), id(B[0]), id(B[1]), id(B[2]))

A[1] = 20
print(f'A={A}, B={B}')

#-------------------------------------------------------

# 중복된 literal, 중복된 immutable 객체는 만들지 않는다.
print('-' * 20)
num1 = 10
num2 = num1

print(num1 is num2)

num1 = num1 + 2 # 새로운 int 객체가 생긴다 (immutable)

print(num1 is num2)

print(f'num1={num1}, num2={num2}')
print(f'id(num1)={id(num1)},\nid(num2)={id(num2)}')

num3 = 6
print(f'num3={num3}')
print(f'id(num3)={id(num3)}')

num3 *= 2 # 새로운 int 객체가 생성된다.
print(f'num3={num3}')
print(f'id(num3)={id(num3)}')
# 이제 num3와 num1의 주소가 같아졌다!!!!

#----------------------------------------------------
# is 연산자 vs. == 연산자
print('-' * 20)

a = 10
b = 10
print(f'a={a}, b={b}')
print(f'id(a)={id(a)}, id(b)={id(b)}')

print(f'a == b : {a == b}') # == 각 '값'들을 비교
print(f'a is b : {a is b}') # is 동일 객체인지 비교

a = [10, 20, 30]
b = [10, 20, 30]    # a와는 다른 list 객체가 생성된다.
print(f'a={a}, b={b}')
print(f'id(a)={id(a)}, id(b)={id(b)}')

print(f'a == b : {a == b}') # == 각 '값'들을 비교
print(f'a is b : {a is b}') # is 동일 객체인지 비교

#------------------------------------------------------------------
# 얕은복사 (shallow copy)
# 새로운 인스턴스를 만들고 인스턴스의 '값'만 복사

# list 의 얕은복사 방법들

# 방법1  copy() 함수 사용
# 방법2  범위지정 [:]  사용
# 방법3  list() 함수 사용
# 방법4  copy.copy() 사용

#--------------------------------------------------------------------
# 방법1 copy() 함수
x = [10, 20, 30]
y1 = x # 대입연산
y2 = x.copy() # 얕은복사

print('-' * 20)
print(f'x={x}, y1={y1}, y2={y2}')
print(f'id(x)={id(x)}, id(y1)={id(y1)}, id(y2)={id(y2)}')
print(f'x == y1 : {x == y1}, x == y2 : {x == y2}, y1 == y2 : {y1 == y2}')
print(f'x is y1 : {x is y1}, x is y2 : {x is y2}, y1 is y2 : {y1 is y2}')

x[1] = 200
print('-' * 20)
print('x[1] = 200 수행 후')
print()
print(f'x={x}, y1={y1}, y2={y2}')
print(f'id(x)={id(x)}, id(y1)={id(y1)}, id(y2)={id(y2)}')
print(f'x == y1 : {x == y1}, x == y2 : {x == y2}, y1 == y2 : {y1 == y2}')
print(f'x is y1 : {x is y1}, x is y2 : {x is y2}, y1 is y2 : {y1 is y2}')

#--------------------------------------------------------------------
# 방법2 [:]
print('-' * 20)
x = [10, 20, 30]
y1 = x
y2 = x[:]
print(f'x is y1 : {x is y1}, x is y2 : {x is y2}, y1 is y2 : {y1 is y2}')

#--------------------------------------------------------------------
# 방법3 list() 사용
print('-' * 20)
x = [10, 20, 30]
y1 = x
y2 = list(x)
print(f'x is y1 : {x is y1}, x is y2 : {x is y2}, y1 is y2 : {y1 is y2}')

#--------------------------------------------------------------------
# 방법4 copy.copy() 사용
import copy

print('-' * 20)
x = [10, 20, 30]
y1 = x
y2 = copy.copy(x)
print(f'x is y1 : {x is y1}, x is y2 : {x is y2}, y1 is y2 : {y1 is y2}')

#-------------------------------------------------------------------------
# 얕은 복사의 한계

print('-' * 20)
print('얕은복사의 한계')

x = [1, 2, ['A', 'B', 'C']]
y = x.copy()    # 얕은복사

print(f'x={x}\ny={y}')
print(f'x == y : {x == y}\nx is y : {x is y}')

x[0] = 'python'
print(f'x={x}\ny={y}')
print(f'x == y : {x == y}\nx is y : {x is y}')

y[-1][-1] = 'F'
print(f'x={x}\n y={y}')

#----------------------------------------------------------
print('-' * 20)
print('깊은 복사 (DeepCopy)')

x = [1, 2, ['A', 'B', 'C']]
y = copy.deepcopy(x) # 깊은 복사 발생
print(f'x={x}\n y={y}')
print(f'x == y : {x == y}\nx is y : {x is y}')

x[0] = 'python'
print(f'x={x}\ny={y}')

y[-1][-1] = 'F'
print(f'x={x}\ny={y}')