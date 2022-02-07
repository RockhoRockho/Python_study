# 가령 다음과 같은 기능을 하는 함수들를 만드려고 한다

#      (입력)        (리턴)
# 1. [1, 2, 3] => [1, 4, 9]        <-- 제곱을 하는 함수

# 2. [-1, 2, -3] => [1, 2, 3]      <--  절대값을 구하는 함수


# 즉, 집합데이터형을 입력 받아서 '각 원소'들에게 '무언가 적용' 한 결과를 만드는 함수!!

def get_square_list(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result


print(get_square_list([3, 4, -6]))


# 도전
def get_absolute_list(numbers):
    result = []
    for number in numbers:
        result.append(number if number >= 0 else -number)
    return result


def get_absolute_list(numbers):
    result = []
    for number in numbers:
        result.append(abs(number))
    return result


print(get_absolute_list([3, 4, -6]))

# '함수' 도 데이터 타입이다!
print(type(get_square_list))

# 함수도! 데이터처럼 주고 받을수 있다?!

a = get_square_list  # 이제 a 는 함수다

print(a([-4, -5, 10]))


# 그렇다면, 함수를 매개변수로 넘겨줄 수도 있는 것이다.

def square(x):
    return x ** 2


def absolute(x):
    return x if x >= 0 else -x


# 함수를 매개변수로 받는 함수
def apply_func_to_list(numbers, func):
    result = []
    for number in numbers:
        result.append(func(number))  # 매개변수로 받는 함수를 내부에서 호출

    return result


result = apply_func_to_list([3, -2, 7], square)
print(result)

result = apply_func_to_list([3, -2, 7], absolute)
print(result)

# 람다 (lambda)
# 이름이 없는 (익명) inline 함수 정의

# 구문: lambda [parameters] : expression(표현식)

print(lambda x: x * 2)  # 표현식이 값인 경우 리턴
print(absolute)
print(square)

(lambda: print('hello'))()
result = (lambda x, y: x + y)(10, 20)
print(result)

double3 = lambda x: x * 3
print(double3(33))

# ★파이썬은 여러문장으로 구성하는 람다는 없다.
# func1 = lambda name, age :
#             print(name)
#             print(age)

result = apply_func_to_list([10, 20, 30], lambda x: x ** 2)
print(result)

result = apply_func_to_list([-3, -21, 7],
                            lambda x: x if x >= 0 else -x)
print(result)

# ----------------------------------------------------------------
# map(), filter(), reduce()와 같은 함수에서도 lambda 활용가능

# map : N -> N
# filter : N -> N' (N' <= N)
# reduce : N -> 1

# ----------------------------------------------------------------
# map() 함수 N개 => N개

# 위와 같이하면, '집합데이터' + '데이터 에 ~~한 동작/연산을 수행하는 함수' 를 세트로 주어
# 일괄 처리 할수 있다
# 파이썬에는 이와 같은 일을 처리하는 함수가 있다.
# 바로 map() 이다

# 구문
#  map(함수, iterable 데이터)     #<-- 이때 data 는 iterable 해야 한다

#  map() 결과는 'map객체' 이고 이 또한 iterable 하다!

m = map(square, [1, 2, 3])
print(m)

print(list(m))

print(list(map(square, [1, 2, 3])))

# print(list(map(upper, "apple")))
print(list(map(str.upper, "apple")))

print(list(map(absolute, [1, -2, -7])))
print(map(int, ["10", "20", "30"]))

# map() 에 lambda 적용

print(list(map(lambda x: -(x ** 2), [1, 4, 9])))

# map() 에 lambda 적용

print(list(map(lambda x: -(x ** 2), [1, 4, 9])))

# map() + lambda 를 여러차례에 걸쳐 적용

print(list(map(
    lambda x: -x,
    map(lambda x: x ** 2, [3, 2, -4])
)))

# [도전]
data = """height,weight,label
140,45,normal
145,72,fat
150,61,fat
137,56,fat
192,48,thin
175,77,fat"""

# 아래와 같은 리스트로 만들기
# [[140.0, 45.0, 'normal'],
#  [145.0, 72.0, 'fat'],
#  [150.0, 61.0, 'fat'],
#  [137.0, 56.0, 'fat'],
#  [192.0, 48.0, 'thin'],
#  [175.0, 77.0, 'fat']]

# 과정
# 1. line 별로 쪼개기
# 2. 각 line 을 ',' 로 쪼개기
# 3. 각 데이터는, '숫자'면 float로 변환, 아니면 그대로

result = []
lines = data.split('\n')[1:]
for line in lines:
    result.append(list(map(
        lambda x: float(x) if x.isdigit() else x,
        line.split(',')
    )))
print(result)

lines = data.split('\n')
f_tonum = lambda n: float(n) if n.isdigit() else n
f_cols = lambda line: list(map(f_tonum, line.strip().split(',')))
csv = list(map(f_cols, lines))
print(csv[1:])

# -----------------------------------------------------------

print()

data2 = "  200 , 400  , 700, hello"
# => [200, 400, 700, "hello"]

print(list(map(
    lambda x: int(x) if x.isdigit() else x,
    map(
        str.strip,
        data2.split(',')
    )
)))

# ------------------------------------------------------------------
# filter : N=> N' (N' <= N)
# 구문 : filter(function, iterable)

# filter에 인자로 사용되는 function은 처리되는 각각의 요소에 대해 bool 값을 반환합니다.
# True를 반환하면 그 요소는 남게 되고, False 를 반환하면 그 요소는 제거 됩니다

# filter() 결과는 filter 객체  (이또한 iterable 하다)

print('-' * 20)


# 주어진 숫자가 3의 배수이면 True, 아니면 False를 리턴하는 함수
def multiple3(x):
    return x % 3 == 0


print(multiple3(8), multiple3(9))

print(list(filter(multiple3, [3, 7, 9])))
print(list(filter(lambda x: x % 3 == 0, [3, 7, 9])))

# map vs. filter
# 동작 비교

data = [1, -2, 3, -4, 5]
                                          # [  1 ,  -2  ,  3  ,  -4,   5  ]
print(list(map(lambda x: x > 0, data)))   # [True, False, True, False, True]

print(list(filter(lambda x: x > 0, data))) # [1,            3,           5]

#-----------------------------------------------------------------------------
# 도전
dataset = [1, -2, 3, -4, 5]

# 양수인 숫자들을 제곱한 결과  => [1, 9, 25]
# 1) 함수로 만들어 보고

def square(n):
    return n ** 2
def filt(n):
    result = []
    for i in n:
        if i > 0: result.append(square(i))
    return result
print(filt(dataset))

# 2) lambda, map, filter 로도 만들어 보자

print(list(map(
    lambda x: x ** 2,
    filter(lambda x: x >0, dataset)
)))

# 3) list comprehension 으로도 도전해보자
print([
    i ** 2
    for i in dataset
    if i > 0
])






