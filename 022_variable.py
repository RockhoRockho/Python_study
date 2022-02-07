#변수명규칙
# 알파벳, 숫자, _  등 사용 가능
# 숫자로는 시작할수 없다
# 변수명에 띄어쓰기 불가
# 특수문자 불가
# 파이썬의 예약어(reserved word)는 변수명으로 사용불가
#      and,  as,  assert,  break,  class,  continue,  def,  del,  elif,  else,  except,  is,
#      finally,  for, from,  global,  if,  import,  in,  lambda,  nonlocal,
#      not,  or,  pass,  raise,  return,  try,  while,  with, yield


# 가능한 변수명
lapTime = 10.2
abc2022 = 10
myName = "John"
my_Name = "John"
_value23 = 3.14

# 불가능한 변수명
# 55num = 33
# $%@#^^ = 33
# %aaa% = 200
# $abc = 10  # Java, JS 는 $ 도 변수명 사용가능하나 Python 은 안됨!
# my-name = "hello"
# aaa diff = 333
# return = 100


# 변수 없애기 del()
name = "John"
print(name, type(name))

del(name)   # name 이라는 변수 삭제

# print(name)

#---------------------------------------------
print('-' * 20)

# 여러 변수를 한줄에 선언

a = 10
b = 20
c = 30
print(a, b, c)

a = 10; b = 20; c = 30
print(a, b, c)

# 그러나, 파이썬에서는 여러변수를 한번에 선언할때
# 아래와 같은 표현을 더 많이 사용함
a, b, c = 100, 200, 300
print(a, b, c)
# ↑ 좀더 파이썬다운(pythonic) 방법

#-----------------------------------------------------
# 변수의 값 증가, 감소
print('-' * 20)

a = 10
print(a)
a = a + 1
print(a)
a = a * 2
print(a)
a = a - 1
print(a)
a = a / 7
print(a)

# 복합 대입 연산자
a, b, c = 100, 10, 7

a += 10   # ↔ a = a + 10
b /= 2    #   b = b / 2
c %= 2    #   c = c % 2
print(a, b, c)

# ++, -- 연산자는 파이썬에는 없다.

#----------------------------------------------------
# 변수값 바꾸기
print('-' * 20)

a = 11
b = 33
print('a =', a, ' b =', b)

temp = a
a = b
b = temp
print('a =', a, ' b =', b)

# pythonic한 방법
a, b = 11, 33
a, b = b, a # ?!
print('a =', a, ' b =', b)

#--------------------------------------------------
# 복소수 타입(complex)
# a + bj

a = 10 + 2j
print(a)
print(type(a))

b = 1j
print(b * b)










