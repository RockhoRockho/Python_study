# 삼황연산자 (ternary operator)
# 파이썬에선 ==>  Conditional Expressions

"""
덧셈 연산 (operation)
연산자 (operator)
피연산자 (operand)

피연산자 개수에 따른 연산자 분류
피연산자 1개 => 단항연산자 (unary operator)  -, not,
피연산자 2개 => 이항연산자 (binary operator)  + - * /
피연산자 3개 => 삼항연산자 (ternary operator)
"""

# 파이썬의 Conditional Expr.
# ( 참일때의 값 ) if (조건식) else (거짓일때의 값)
print('-' * 20)
n = 3
result = "짝수" if n % 2 == 0 else "홀수"
print(result)

# 두 수간의 차 (difference)

a = 54
b = 72

diff = (a - b) if a > b else (b - a)
print('diff =', diff)