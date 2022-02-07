# 문자열 포맷팅 (formatting)
# 데이터 포맷을 위해 사용
# 방법1 : % 연산자 사용
# 방법2 : .foramt() 사용
# 방법3 : f-string 사용 (파이썬 3.6 이상)

#--------------------------------------------------

# 1. % 연산자 사용

# 서식지정자(format specifier) 를 포함한 문자열과, 각 '서식문자'에 대응하는 데이터들을 연결하여 문자열 완선

# 구문)
#    "서식문자포함문자열" % ( 데이터 튜플 )

a = "Hello %s"
print(a)

b = "Hello %s" % ("파이썬")
print(b)

print(a % ("파이썬"))
print(a % ("자바"))
print(a % ("인공지능"))

# 서식지정자 문자는 여러개 있을 수 있다.
a = "My name is %s, I'm %d years old" % ("박수진", 10)
print(a)

# format specifier
#  https://docs.python.org/2/library/string.html

# %d   십진수 정수
# %f   실수
# %s   문자열.  어떤값도 문자열로 변환하여 표현
# %%   %  문자 자체

print("%d %x %X" % (13, 13, 13))

import math
pi = math.pi
print(pi)

fmt = "원주율은 %f 입니다"
print(fmt % (pi))  # %f 는 소숫점 6자리까지 출력

print("원주율은 %.2f 입니다" % (pi)) # %.2f  소숫점 2자리까지 출력

print("원주율은 %.4f 입니다" % (pi))
print("원주율은 %.4f 입니다" % (100))

print("I have %s apples" % (3))
print("I have %s apples" % ("many"))

print()
# %d : 자리수 명시 가능
a, b, c, d = 10, 100, 1000, 1000
print("%d:%d:%d:%d" % (a, b, c, d))
print("%5d:%5d:%5d:%5d" % (a, b, c, d))  # 5칸, 오른쪽 정렬
print("%-5d:%-5d:%-5d:%-5d" % (a, b, c, d))  #5칸, 왼쪽 정렬

print()

print("***%f***" % 0.12345)
print("***%4.2f***" % 0.12345)  # %4.2f  전체적으로 4자리. 소숫점 이하 2자리
print("***%5.1f***" % 0.12345)

#------------------------------------------------------------------
# 방법2 : format() 함수 사용
print("My name is {}, I'm {} years old".format("박수진", 10))


print("My name is {name}, I'm {age} years old".format(name = "박수진", age = 10))
print("My name is {name}, I'm {age} years old".format(age = 10, name = "박수진"))

print("[A{:<30}]".format("Left"))
print("[A{:>30}]".format("Right"))
print("[A{:^30}]".format("Center"))

print("PI = {:.3f}".format(math.pi))
print("PI = {:+.3f}".format(math.pi))
print("PI = {:+.3f}".format(-math.pi))

print("{:,}".format(1234567890))

#-----------------------------------------------------------------------
# 방법3 : f-string

lang = "Python"
author = "Guido van Rossum"

print("Language: {}, Author: {}".format(lang, author))

print(f'Languege: {lang}, Author: {author}')

print(f'원주율은 {math.pi} 입니다')
print(f'원주율은 {math.pi:.2f} 입니다')


#----------------------------------
# 연습
#           Seoul     10,312,545        +91,375
#           Pusan      3,567,910         +5,868
#         Incheon      2,758,296        +64,888
#           Daegu      2,511,676        +17,230
#         Gwangju      1,454,636        +29,774

# 3가지 방법으로 출력
print()
area, pop, inc = "Seoul", "10,312,545", "+91,375"
print("%15s%15s%15s" % (area, pop, inc))
area, pop, inc = "Pusan", "3,567,910", "+5,868"
print("%15s%15s%15s" % (area, pop, inc))
area, pop, inc = "Incheon", "2,758,296", "+64,888"
print("%15s%15s%15s" % (area, pop, inc))
area, pop, inc = "Daegu", "2,511,676", "+17,230"
print("%15s%15s%15s" % (area, pop, inc))
area, pop, inc = "Gwangju", "1,454,636", "+29,774"
print("%15s%15s%15s" % (area, pop, inc))

print()
area, pop, inc = "Seoul", 10312545, 91375
print("{:>15}{:>15,}{:>+15,}".format(area, pop, inc))
area, pop, inc = "Pusan", 3567910, 5868
print("{:>15}{:>15,}{:>+15,}".format(area, pop, inc))
area, pop, inc = "Incheon", 2758296, 64888
print("{:>15}{:>15,}{:>+15,}".format(area, pop, inc))
area, pop, inc = "Daegu", 2511676, 17230
print("{:>15}{:>15,}{:>+15,}".format(area, pop, inc))
area, pop, inc = "Gwangju", 1454636, 29774
print("{:>15}{:>15,}{:>+15,}".format(area, pop, inc))

print()
area, pop, inc = "Seoul", 10312545, 91375
print(f"{area:>15}{pop:>15,}{inc:>+15,}")
area, pop, inc = "Pusan", 3567910, 5868
print(f"{area:>15}{pop:>15,}{inc:>+15,}")
area, pop, inc = "Incheon", 2758296, 64888
print(f"{area:>15}{pop:>15,}{inc:>+15,}")
area, pop, inc = "Daegu", 2511676, 17230
print(f"{area:>15}{pop:>15,}{inc:>+15,}")
area, pop, inc = "Gwangju", 1454636, 29774
print(f"{area:>15}{pop:>15,}{inc:>+15,}")









































