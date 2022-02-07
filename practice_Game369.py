# 369게임
# 1~100 까지의 자연수를 나열하되,
# 10개 단위로 줄바꿈을 하고
# 숫자에 3,6,9 중 하나라도 있으면 * 표시를 하기

# 1번문제
num = 1
while num <= 100:
    if '3' in list(str(num)):
        print(f'{"*":<4}', end='')
    elif '6' in list(str(num)):
        print(f'{"*":<4}', end='')
    elif '9' in list(str(num)):
        print(f'{"*":<4}', end='')
    else:
        print(f'{num:<4}', end='')
    if num % 10 == 0: print()
    num += 1

# 2번문제
num1 = 1
num2 = int(input())
while num1 <= num2:
    if '3' in list(str(num1)):
        print(f'{"*":<4}', end='')
    elif '6' in list(str(num1)):
        print(f'{"*":<4}', end='')
    elif '9' in list(str(num1)):
        print(f'{"*":<4}', end='')
    else:
        print(f'{num1:<4}', end='')
    if num1 % 10 == 0: print()
    num1 += 1