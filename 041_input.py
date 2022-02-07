# 파이썬 기본입력 함수 input()
# 기본적으로 input() 함수는 키보드로 부터 입력받아
# 문자열(str) 으로 리턴합니다

# a = input()
# print('입력하신 값은', a)
# print(a + 8)  # input() 의 결과값은 str.  산술연산 불가

# a = int(input())  # input() 으로 입력한 결과(str) 를 정수(int) 로 변환하여 a 에 대입
# print(a, type(a))
# print(a + 8)

# print("키를 입력하세요(cm)", end=" ")
# height = float(input())
# print(height, type(height))

# prompt 를 사용한 input 입력
# height = float(input("키를 입력하세요(cm) "))
# print('height =', height)

#--------------------------------------------------
# 연습
# 1야드(yd)는 91.44cm이고 1인치(in)는 2.54cm이다.
# 처음에는 야드를 입력받고, 두번째는 인치를 입력받아
# 각각 cm로 변환하여 다음 형식에 맞추어 소수 둘째자리까지 출력하시오.​

# [실행예]
# yard 입력: 23.45
# inch 입력: 41.273
# 23.45 yard 는 2144.27cm
# 41.27 inch 는 104.83cm

yard, inch = 91.44, 2.54
a = float(input())
b = float(input())
print('{:4.2f} yard는 {:5.2f}cm'.format(a, yard*a))
print('{:4.2f} inch는 {:5.2f}cm'.format(b, inch*b))
