# break
# 순환문 (while, for) 안 에서 순환문을 강제로 종료시키는 키워드

# break 는 감싸고 있는 가장 가까운 순환문을 종료합니다

n = 1
while True:
    print(n, end=' ')
    if n == 100:
        break
    n += 1

print('\nwhile 종료')

# 연습
# a 와 b의 최소 공배수 구하기
# - a, b 는 임의의 자연수
# - 순환문 + break 사용

print('-' * 20)
a, b = 2, 7
num = a if a > b else b
while True:
    if num % a == 0 and num % b == 0:
        print(f'{a}와 {b}의 최소공배수는 {num}')
        break
    num += 1

print('-' * 20)
# 구구단 출력시
# 2단은 x 2까지 출력
# 3단은 x 3까지 출력

dan = 2
while dan <= 9:  # 2단 ~ 9단

    print(dan, '단')
    mul = 1
    while mul <= 9:  # x1 ~ x9
        print(dan, 'x', mul, '=', dan * mul)
        if dan == mul: break
        mul += 10
    print()
    dan += 1

print('-' * 20)
# -------------------------------------------------------

# continue
# 순환문 처음으로 돌아가기
# 순환문은 종료하지 않되, 특정 조건만 skip 하는 경우 사용

num = 1
while num <= 10:
    num = num + 1

    if num % 2 == 1:
        continue

    print(num)

# 정수를 계속해서 입력받다가, 0 이 입력되면
# 그때까지의 정수의 '합' 과 '평균' 을 출력

"""
[입력예]
10
20
30
0

[출력예]
합: 60
평균: 20.0

"""
print('-' * 20)
total = 0
cnt = 0
while True:
    n = int(input())
    if n == 0: break
    total += n  # 합계 누적 합산
    cnt += 1  # 개수 +1 증가
print('합:', total)
print('평균:%.1f' % (total / cnt))
