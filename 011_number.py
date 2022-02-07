# 숫자 (정수, 실수) 데이터
# 소숫점이 없으면 '정수' (int : integer)
# 소숫점이 있으면 '실수' (float)
# 컴퓨터 프로그래밍에서는 실수를 floating point number 라 함

print(10) # 정수 int 10
print(10.0) # 실수 float 10
print(10.)
# 소수점 뒤에 아무 숫자가 없으면 정수가 아니라, 실수로 인식
# (결과가 10 이 아닌 10.0 으로 표시됨에 주목)
print(.1) # 0.1 float
print(10 - 2 * 4) # 연산자 우선순위
print((10 - 2) * 4) # 괄호 연산 우선 실행!
print(4 * 5) # '정수' 와 '정수' 끼리의 연산결과는 '정수'
print(4 * 5.0) # '실수' 와의 연산 결과는 '실수'
print(4 / 2) # ★나눗셈 연산 결과는 언.제.나 실수

print() # 아무것도 출력 안하고 줄바꿈만.

# 나눗셈 후 소수점 이하를 버리는 연산자 :  //
# 정수 끼리 딱 떨어지는 결과에 대해서는 정수로 결과가 나옴
# 나눗셈 후 소숫점 이하 버리는 연산자

print(4 // 2)
print(4 // 2.0)
print(3.4 / 1.1)
print(3.4 // 1.1)

# print(5 / 0)
# print("실행될까요?")

# 나머지 연산자 %
print(13 % 3)
print(12.6 % 4.1)
# 12.6 = 4.1 * 3 + 0.3
# 컴퓨터 실수 계산 결과는
# 오차가 존재한다.

print('--------------------------')
print('-' * 30)
# 제곱연산자 **
print(2 ** 4)
print(-3 ** 3)
print(2 ** -1)
print(2 ** -2)
print(10 ** -2)
print(2 ** (1/2))
print(27 ** (1/3))

# ※ 참고 : 제곱근구하기
import math
print(math.sqrt(2))




































