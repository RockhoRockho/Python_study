# 조건식에 사용가능한 비교연산자, 논리연산자
# 비교연산자 : >, >=, <, <=, !=, ==
# 논리연산자 : and, or, not, ^ (xor)
# 위 연산자들의 결과값은 항상 True / False
#      and : 둘다 '참' 일때 '참'
#      or : 둘중 하나만 '참' 이면 '참'
#      not : 참 -> 거짓, 거짓 -> 참
#      ^ : eXclusive OR (XOR, 배타적 논리합)
#          같으면 거짓, 다르면 참

d = 10
result = d > 2
result = d > 10
result = d <= 100   #   주의 =<  (x)
result = d == 100
result = d == 100 / 10  # 10 == 10.0 참으로 판정
result = d != 10

result = d % 2 == 0
result = d % 3 == 0
result = d % 2 == 0 and d % 3 == 0 # F
result = d % 2 == 0 or d % 3 == 0
result = (d % 2 == 0) ^ (d % 3 == 0)
# ↑ 괄호 없으면 ^ 는 논리연산자가 아닌 비트 연산자로 동작함
result = not d % 2 == 0 # F
result = not d % 3 == 0 # T

if result:
    print(result, '참입니다')
else:
    print(result, '거짓입니다')

# ----------------------------------------------
print('-' * 20)

score = 10

if 0 <= score and score <= 100:
    print(score, '는 유효한 점수입니다')
else:
    print(score, '는 유효한 점수가 아닙니다')

# 파이썬에선 a <= x <= b 표현 가능
if 0 <= score <= 100:
    print(score, '는 유효한 점수입니다')
else:
    print(score, '는 유효한 점수가 아닙니다')

# ↑ 파이썬에선 비교연산자가 chaining 된다.
# 0 <= score <= 100
# ↓
# 0 <= score and score <= 100 으로 chaining  된다

print(False == True == False) # True 가 나올줄 알았는데.. False 다!

# 왜? -->  False == True and True == False

print((False == True) == False)

#----------------------------------------
# 조건식의 '참' '거짓' 판정

# 조건식의 참 / 거짓 판정

# 조건문,  순환문 등에 사용되는  '조건식' 은 참, 거짓이 판정되어야 하는데
# 파이썬에서는 bool 타입 외에도 조건식에서 참, 거짓 판정이 된다.

#           │     참     │   거짓
# ───────────────────
# bool 타입 :     True         False
# 숫자 타입 :  0 아닌 숫자      0
# str  타입 :      "abc"        ""   빈문자열
# list 타입 :    [1, 2, 3]      []
# tuple 타입 :   (1, 2, 3)      ()
# dict 타입 :    {"name":"john"}    {}

# None 타입 :   무조건 거짓

print('-' * 20)
result = 0.001  # T
result = -100   # T
result = 0      # F
result = 0.0    # F
result = ""     # F
result = " "    # T
result = not " "    # not의 결과는 bool 타입
result = bool(" ")  # bool() 결과도 bool 타입
result = [1, 2, 3]  # T
result = (1, )      # T
result = ()         # F
result = ("")       # F
result = ("", )     # T tuple
result = {'name': 'hong'}   # T
result = {}
result = None

if result:
    print("참", type(result), result)
else:
    print("거짓", type(result), result)

# ------------------------------------------------------------
print('-' * 20)
# SCE : Short-circuit Evaluation
# 논리연산자 and, or의 결과

#논리 연산자 and, or 표현식과의 관계
#참, 거짓 판정에 이어 논리연산자의 결과는
# expression 값이 된다.
# 이를 short-circuit evalutaiton (SCE) 혹은
# lazy evalutation 이라 한다

# or
# 왼쪽이 참인 경우 '왼쪽' 값 리턴
# 왼쪽이 거짓인 경우 '오른쪽' 값 리턴

# and
# 왼쪽이 참인 경우 '오른쪽' 값 리턴
# 왼쪽이 거짓인 경우 '왼쪽' 값 리턴


result = True or False  # True
result = False or True  # True

result = True and False # False
result = False and True # False

result = 0 or 100       # '참' 인데.. or의 결과각 True가 아니라? 100?

result = "Hello" or "Python"    # "Hello"
result = "Hello" and "Python"   # "Python"
result = [] and "Python"        # []

if result:
    print("참", type(result), result)
else:
    print("거짓", type(result), result)

print()
n = 10
(n % 5 == 0) and print(n, "은 5의 배수입니다")
(n % 5 == 0) or print(n, "은 5의 배수가 아닙니다")

print(print()) # print()의 리턴값은 None

# 과연 아래의 결과는?
print("AAA") and print("BBB")
print()
print("AAA") or print("BBB")

# ^ 은 bool 타입 외에는 아니되오...
# print([10] ^ [20])

# ^ 의 피연산자로 int, bool 타입이 오면 bit 연산 xor 수행

print(23 ^ 9)

# 0001 0111   23
# 0000 1001   9

print(0 ^ 100)

print(True ^ 100)   # True가 int 1으로 형변환 된다!?
print(int(True), int(False))
print(False ^ 100)

#-------------------------------------------
# in, not in 연산자

# item in iterable

#    in               not in
#  x in 문자열    x not in 문자열
#  x in 리스트    x not in 리스트
#  x in 튜플      x not in 튜플
#  x in 세트      x not in 세트
#  x in 딕셔너리  x not in 딕셔너리      <-- key 값의 존재 유무
print('-' * 20)
x, data = "a", "abc"
x, data = "A", "abc"
x, data = "", "abc" # 무조건 참이 된다!

x, data = 10, [10, 20, 30]
x, data = 11, [10, 20, 30]

x, data = 10, (10, 20, 30)
x, data = 11, (10, 20, 30)

x, data = 10, {10, 20, 30}
x, data = 11, {10, 20, 30}

# dict에서 in 연산자를 사용하는 key에서 찾는 것임
x, data = "name", {"name" : "john", "age" : 12}

if x in data:
    print(x, "in", data, " <- 참")
else:
    print(x, "in", data, " <- 거짓")

if x not in data:
    print(x, "not in", data, " <- 참")
else:
    print(x, "not in", data, " <- 거짓")

# 타입확인 is
a = 10
a = "10"
a = 10.0

print(type(a))

print(type(a) is float)
print(type(a) is int)