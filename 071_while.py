# 특정 코드를 일정 회수 반복수행하는 경우 사용하는 구문
# 순환문(loop) 혹은 반복문(iteration) 이라고 한다

# 파이썬에는 while, for 구문이 순환문을 수행합니다

#-------------------------------------------------
# while 순환문

# while 순환문 구조,  조건문이 '참' 인 동안 수행문장을 반복수행

# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
#     ...
# else:
#      순환문 빠져나오기 전에 수행

num = 0
while num < 5:
    print(num)
    num += 1

print('while 종료')

# 순환문에서 중요한 것은
# 1. 몇번 순환을 하는가?
# 2. 순환하는 동안 변수값의 변화 범위는?
# 3. 순환문 종료후 변수값은?

# 위 순환문의 경우
# 1. 총 5번 순환을 했고
# 2. 순환하는 동안 num 변수값은 0 부터 4 까지 변화
# 3. 순환문 종료후 num 값은 5

# 도전
# 10 ~ 20 출력
print('-' * 20)
a = 10
while a < 21:
    print(a, end=' ')
    a += 1

print("\n 종료")

# 구구단 2단을 출력해보자, while  사용
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
print('-' * 20)
print('구구단 2단')

i = 1
while i <= 9:
    print(f'2 x {i} = {2 * i}')
    i += 1

# 연습
# 1 ~ n 까지의 숫자 중에서
# 3과 7의 공배수만 출력
#  => 21 42 63 84
print('-' * 20)
n = 100
i = 1
while i <= n:
    if i % 3 == 0 and i % 7 == 0:
        print(i, end=' ')
    i += 1

print('\n종료')

i = 21
while i <= n:
    print(i, end=' ')
    i += 21
print('\n종료')
