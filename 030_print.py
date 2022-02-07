# print() 기본 출력함수

# 파이썬의 가장 기본적인 출력 함수 print()

# print( 출력내용1, 출력내용2, 출력내용3, ...)
#  위와 같이 print() 함수의 parameter 로 출력할 내용들을 기입하면 된다

# print() 함수는 출력한후 자동적으로 "줄바꿈" 됩니다 (디폴트)

print(10, 20, 30)
print("I'm", 30, "year's old")

print()

a = 4 * 2
b = 3

print(a, "x", b, "=", a * b)  # 매개변수는 5개
print(str(a) + " x " + str(b) + " = " + str(a * b))  # 매개변수는 1개

# end
print(10, end = "")   # end = 출력하고 나서 마지막에 출력하는 문자열
print("hello", end = "")
print(3.14)

print()

print(2022, end="-")
print(10, end="-")
print(23)

# sep (separator)

print(10, 20, 30)  # sep=" "
print(10, 20, 30, sep="***")


print()
# 이스케이프 문자 (escape character)
# '문자열' 내에서 특수한 문자 출력할때 사용
# \와 조합하여 출력

# 많이 사용되는 이스케이프 코드
#    \n : 줄바꿈
#    \t : 탭
#    \\ : 역슬래시
#    \' : 홀따옴표
#    \" : 쌍따옴표

# He says "I'm fine" <-- 출력하려면
print("He says \"I'm fine\" ")
print('He says "I\'m fine"')

# Raw String
# 문자열 내부의 모~든 특수기능(?) 제거

path = "D:\DevRoot\Dropbox\Py00\21_Python"
print(path)

path = r"D:\DevRoot\Dropbox\Py00\21_Python"
print(path)


#------------------------------------------------
#  indent
# 파이썬은 들여쓰기(indentation) 에 대해 엄격한 규칙 적용
print(10)
 # print(100)
print(300)

#-------------------------------------------------






