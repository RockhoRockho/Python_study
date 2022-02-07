# 재귀호출 (recursive call)
#- 함수가 자기 자신을 다시 호출하는 구조
#- 장점: 프로그램을 구조적으로 작성, 복잡한 문제를 단순화! 추상화!
#- 단점; 메모리 부담 발생

def recursive(n):
    print(n, end=' ')
    recursive(n + 1)
    print('종료')

#

# recursive(1)
#       -> recursive(2)
#           -> recursive(3)
#               -> ...
#           RecursionError:

# -------------------------------------------
# n! factorial
# 4! 4 x 3 x 2 x 1
# n! n x (n-1) x (n-2) x ... x 1
#   = n x(n-1)! <-- 재귀적인 정의.

# 0! = 1 <-- 재귀호출 종료조건

def factorial(n):
    if n == 0: return 1 # 종료조건, 재귀호출 리턴하기 시작

    return n * factorial(n - 1)

for i in range(1, 11):
    print(f'{i}! =', factorial(i))

# factorial(4)
#       4 x factorial(3)
#           3 x factorial(2)
#               2 x factorial(1)
#                   1 x factorial(0)

# 도전
# power(base, exp) # <-- base(2, 4) => 16

def power(base, exp):
    if exp == 0: return 1
    return base * power(base, exp-1)

base = 2
for exp in range(0, 9):
    print(f'{base}^{exp} = {power(base, exp)}')