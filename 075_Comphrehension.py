# 주어진 리스트의 원소 데이터 들을 * 3 하여 새로운 리스트 작성하기
# ex) [1, 2, 3, 4] ==> [3, 6, 9, 12]

a = [1, 2, 3, 4]
print(a * 3)   # 원하는 결과 아님.

result = []
for num in a:
    result.append(num * 3)
print(result)

# List Comprehension  -->  list 안에 포함된 for문  --> list 생성
# Dict Comprehension  -->  dict 안에 포함된 for문 --> dict 생성
# Set Comprehension -->  set 안에 포함된 for문 --> set 생성

# List Comprehension 구문
# [표현식 for 항목 in 반복가능객체 (if 조건)]

result = [num * 3 for num in a ]
print(result)

# 1 ~ 10 까지 담긴 리스트
print([i + 1 for i in range(10)])

#  짝수에만 3을 곱하여 담고 싶다면 다음과 같이 "if 조건"을 사용할 수 있다
# [1, 2, 3, 4] --> [6, 12]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# 도전
# 아래와 같이 짝수에만 적용되게 하려면? 홀수는 그대로.
# [1, 2, 3, 4]
#  ↓  ↓  ↓  ↓
# [1, 6, 3, 12]   <- 2, 4 에만 x3 적용

# TODO
result = [
    num * 3 if num % 2 == 0 else num
    for num in a
]
print(result)

result = []
for num in a:
    result.append(num * 3 if num % 2 == 0 else num)
print(result)

# ------------------------------------------------
# for문 2개 이상 사용도 가능

# [표현식 for 항목1 in 반복가능객체1 if 조건1
#         for 항목2 in 반복가능객체2 if 조건2
#         ...
#         for 항목n in 반복가능객체n if 조건n]

result = [
    f'{i}-{j}'
    for i in range(2, 10, 2)   # 2, 4, 6, 8
    for j in range(1, 10, 2)   # 1, 3, 5, 7, 9
]
print()
print(result)

print()
result = [
    ch + str(num)
    for ch in "ABC"
    for num in range(1, 3)  # 1, 2
]
print(result)

# 도전
# 구구단의 모든 결과를 담는 리스트
"""
['2 x 1 = 2',
 '2 x 2 = 4',
 ...
 '9 x 7 = 63',
 '9 x 8 = 72',
 '9 x 9 = 81']

"""
print()
result = [
    f'{dan} x {mul} = {dan * mul}'
    for dan in range(2, 10)
    for mul in range(1, 10)
]
print(result)

# 위에서 짝수 단만 출력하려면?
result = [
    f'{dan} x {mul} = {dan * mul}'
    for dan in range(2, 10, 2)
    for mul in range(1, 10)
]
print(result)

result = [
    f'{dan} x {mul} = {dan * mul}'
    for dan in range(2, 10) if dan % 2 == 0
    for mul in range(1, 10)
]
print(result)
print('\n'.join(result))

# 단순히 0 으로 n 개 초기화 가능
result = [0 for n in range(0, 26)]
print(result)


# 주어진 dataset 에서 제곱의 결과가 10보다 큰 결과만 담은 list 작성
# [1, -2, 3, -4, 5]
#  ↓ ↓
# [16, 25]
dataset = [1, -2, 3, -4, 5]

result = [
    x ** 2
    for x in dataset
    if x ** 2 > 10
]
print(result)

result = [
    y
    for y
    in [
        x ** 2
        for x
        in dataset
    ]
    if y > 10
]
print(result)

# -----------------------------------------------------------
# set comprehension
# 기본 구문은 list comprehension 과 동일
print('-' * 20)
result = [  # list
    num % 3
    for num in range(10)
]
print(result)
result = {   # set
    num % 3
    for num in range(10)
}
print(result)

# ----------------------------------------------------------
# dict comprehension
# {10, 20, 30}  # <-- set {값, .. }
# {1:10, 2:20, 3:30}  # <-- dict  {key:value, ..}

result = {
    n: n ** 2
    for n in range(5)
}
print(result)

# list(iterable)
print(list(range(5)))

result = {
    x: list(range(x))
    for x in [1, 2, 3, 4, 5]
}
print(result)

# -------------------------------------------------------
# dict + for

print('-' * 20)
student = {"name" : "홍반장", "email": "hong@mail.com", "address": "강남역"}

for key in student:
    print(key, ':', student[key])

# dict 의 items() 사용
print(student.items())  # (key, value) tuple 의 iterable

for key, value in student.items():
    print(key, ':', value)

result = [
    (k, v)
    for k, v in student.items()
]
print(result)

