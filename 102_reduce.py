# reduce()  N => 1개

from functools import reduce

# 구문
# functools.reduce(function, iterable[, initializer])


# function 을 사용해서 iterable을 '하나의 값'으로 줄여서 '값'을 리턴한다.
# initializer 는 주어지면 첫 번째 인자로서 추가됩니다

dataset = [1, 2, 3, 4]


# 기존 for문
def total(numbers):
    result = 0
    for number in numbers:
        result = result + number
        print('r:', result)
    return result


print(total(dataset))


# 0 | 1, 2, 3, 4
#     1
#        3
#           6
#              10

# reduce()에 적용되는 함수는 : '두개'의 입력 -> '하나'의 결과
def add(x, y):
    return x + y


print(reduce(add, dataset))

# [   1, 2,   3,   4,   5]
#     ↓  ↓
# add(1, 2)
#     ↓
# [   3,    3,   4,   5]
#     ↓     ↓
# add(3,    3)
#     ↓
# [   6,       4,   5]
#     ↓        ↓
# add(6,       4)
#     ↓
# [   10,         5]
#      ↓          ↓
# add(10,         5)
#     ↓
#    15   # 결국 하나의 값으로 reduce 된다


# reduce + lambda
print(reduce(lambda x, y: x + y, dataset))

sum_all = lambda numbers: reduce(lambda a, b: a + b, numbers)
print(sum_all([10, 11, 12, 13, 14, 15, 16]))
print(sum_all([-1, -2, -3, -4, -5]))


# initializer(초기값)
# [1, 2, 3] ==> [1, 4, 9]

def func(a, b):
    a.append(b ** 2)
    return a


print(reduce(func, [1, 2, 3], []))

#   []   | [1,   2,   3]
#     ↓    ↓
# func([], 1)
#       ↓
#      [1]    2     3
#         ↓   ↓
#    func([1], 2)
#           ↓
#        [1, 4]    3
#            ↓     ↓
#      func([1, 4], 3)
#                ↓
#            [1, 4, 9]

# lambda 로 가능할까?
# print(reduce(lambda a, b: a.append(b ** 2), [1, 2, 3], []))  # 에러, append() 리턴값은 None

print(reduce(lambda a, b: a + [b ** 2], [1, 2, 3], []))  # 가능은 하다. 성능 나쁨. 비추.

# SCE 사용!

print(reduce(lambda a, b: a.append(b ** 2) or a, [1, 2, 3], []))

# ------------------------------------
# [도전]

dataset = [1, 4, 3, 5, 2]
# reduce + lambda 를 사용하여 최댓값을 찾아보세요

print(reduce(lambda a, b: a if a >= b else b, dataset))

# --------------------------------------------------------
# 아이템 별 개수 구하기
dataset = ["dog", "dog", "dog", "cat", "cat", "bird"]

# 개수구하기 결과 =>  {'dog': 3, 'cat': 2, 'bird': 1}

# 1. for loop 를 이용한 방법
# 2. reduce 를 이용한 방법   ... 초깃값을 어떻게 할까?
#    2-1 reduce + 함수
#    2-2 reduce + lambda

print('-' * 20)
# 1. for 사용
student = {'name':'Susan'}

print(student['name'])
print(student.get('name'))

# print(student['age']) # 에러
print(student.get('age')) # key 값이 없으면 None 리턴
print(student.get('age', 20)) # key 값이 없으면 20 리턴

def count_element(elements):
    result = {}
    for element in elements:
        result[element] = result.get(element, 0) + 1
    return result

print(count_element(dataset))

# 2-1. reduce + 함수 사용

def func(result, element):
    result[element] = result.get(element, 0) + 1
    return result

print(reduce(func, dataset, {}))

# 2-2. reduce + lambda

# dict 의 수정
student['name'] = 'john'
student.update({'name': 'Kelly'})
print(student)

# dict.update : 있으면 업데이트하고, 없으면 추가하고  , None 리턴
# dict.get    : 있으면 가져오고, 없으면 None 리턴 (default 값이 있으면 default 값 리턴)

# dict에 key value를 추가하고, 추가된 dict를 리턴받기
# SCE 사용
student.update({"email": "uuu@mail.com"})

print(reduce(
    lambda r, e: r.update({e : r.get(e, 0) + 1}) or r,
    dataset,
    {}
))


#----------------------------------------------------------------
# [도전] 알파벳 사용 빈도
print('-' * 20)
fp = open(r'D:\DevRoot\dataset\sample.txt', encoding='utf8')
data = fp.read()

print(data)

# 대소문자 구분없이 알파벳 계수
# 결과
"""
{'a': 245, 'b': 32, 'c': 82, 'd': 129, 
 'e': 365, 'f': 61, 'g': 56, 'h': 170, 
 'i': 231, 'j': 5, 'k': 37, 'l': 112, 
 'm': 93, 'n': 257, 'o': 288, 'p': 81,
 'q': 2, 'r': 223, 's': 201, 't': 297,
 'u': 91, 'v': 24, 'w': 56, 'x': 1, 'y': 50}
 ※ dict는 순서 무관!!
"""

# 알파벳 사용 빈도 > map, filter, reduce
# 전처리
# 알파벳만 filter한 list 만들기

data = list(filter(str.isalpha, data))
print(data)
# 모두 소문자로 변환하기
data = list(map(str.lower, data))
data = sorted(data)
print(data)

# 1. reduce + 함수

def func(r, e):
    r[e] = r.get(e, 0) + 1
    return r
print(reduce(func, data, {}))

# 2. reduce + lambda
result = reduce(
    lambda r, e: r.update({e : r.get(e, 0) + 1}) or r,
    data,
    {}
)

print()

# 정렬해주세요~
sorted_key = sorted(result)
for key in sorted_key:
    print(key, result[key])

# value에 대해 정렬
sorted_key = sorted(result, key=result.get, reverse=True)
for key in sorted_key:
    print(key, result[key])

print(sorted(result.items(), key=lambda x: x[1], reverse=True))


# ----------------------------------------------------------------
# map(), filter() 동작도 reduce()로 가능
# 어지간한 데이터 처리 동작 -> reduce()로 가능!
# 제곱하기
# [1, 2, 3] => [1, 4, 9]    map() 동작이지만 reduce() 로 가능
print(reduce(
    lambda r, e: r.append(e ** 2) or r,
    [1, 2, 3],
    []
))

# 양수만 골라내기
# [1, -2, 3] => [1, 3]  filter() 동작이지만, reduce() 로도 가능
print(reduce(
    lambda r, e : (r.append(e) or r) if e >= 0 else r,
    [1, -2, 3],
    []
))
