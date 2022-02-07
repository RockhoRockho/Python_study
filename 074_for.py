# for 순환문
# 기존의 다른 프로그래밍 언어의 for 문에 비해 파이썬은 매우 직관적이고 사용하기 편리

# 구문]
# for 변수 in iterable객체:
#     수행할 문장1
#     수행할 문장2
#     ....
# else:
#      순환문 빠져나오기 전에 수행

# iterable한 객체들 => range(숫자), str, list, set, tuple, dict ...

print(range(3))  # 0, 1, 2 의 숫자가 담긴 iterable 객체 생성

for i in range(3):
    print('hello world')

print()

for i in range(4):  # 0, 1, 2, 3
    print('hello python', i)

# range(5, 8)  => 5, 6, 7
print()
for i in range(5, 8):
    print('hello world', i)

# range(4, 15, 3)     # step 값   3  : 4, 7, 10, 13
print()
for i in range(4, 15, 3):
    print('hello monday', i)

print()
for i in range(10, 0):
    print(i)  # 한번도 순환 안함

for i in range(10, 0, -2):  # 10, 8, 6, 4, 2
    print(i, end=' ')

# 구구단 2단을 출력해보자, for  사용
"""
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
"""
for i in range(1, 10):
    print(f'2 x {i} = {2 * i}')

# 구구단
# 1단 ~ 9단
for dan in range(2, 10):  # 2 ~ 9 단
    print(dan, '단')
    for mul in range(1, 10):  # x 1 ~ x 9
        print(f'{dan} x {mul} = {dan * mul}')
    print()

#----------------------------------------------------------
# for문 + list

animals = ['dog', 'cat', 'bird', 'puppy', 'kitty']

print()
# index 를 사용한다면
for i in range(len(animals)):  # 0 ~ 4
    print(animals[i])

# iterable 안에서 데이터 직접 순환
print()
for animal in animals:
    print(f'I love {animal}')

# 다양한 iterable에서 가능

for ch in "Hello":
    print(ch, end = ', ')
print()

# list(iterable), tuple(iterable)..
print(list("hello"))

print()

result = []
for ch in "Hello":
    result.append(ch)
print(result)

print()
for item in (10, 20, 30, 40):
    print('tuple', item)

# dict 는 for문에서 key 값이 순환한다.
print()
myDict = {'name': 'hong', 'age': 24, 'grade': 4}
for key in myDict:
    print(key, ':', myDict[key])

# -------------------------------------------------
# iterable안의 데이터가 tuple인 경우
a, b, c = 10, 20, 30
print(a, b, c)
a, b, c = [10, 20, 30]
print(a, b, c)
a, b, c = "XYZ"
print(a, b, c)

a = [(1, 2), (3, 4), (5, 6)]
# len(a) -> 3

print('-' * 20)
for x in a: # x는 tuple이다
    print(x[0], x[1])

# 파이썬 다운 표현
print()
for x, y in a: # x는 int다
    print(x, y)

#------------------------------------------------
print('-' * 20)

# break, continue + for문
for x in range(10):
    print(x)
    if x == 5: break

print()

for x in range(10):
    if x % 2 == 0: continue
    print(x)

# 예제 연습
# 학생들의 점수가 아래와 같이 주어졌다고 하자
# 총점과 평균을 출력해보세요

total = 0
avg = 0.0
scores = [88, 34, 98, 74, 33]

# 결과예
# 학생수: 5 명
# 총점: 327 점
# 평균: 65.4 점

for i in scores:
    total += i
avg = total / len(scores)
print(f'학생수: {len(scores)} 명')
print(f'총점: {total} 점')
print(f'평균: {avg:.1f} 점')









