# 변수(variable) 은 데이터를 담아두는 공간
# '이름'을 정해서 담아둔다.  이 이름을 변수이름 (variable name) 이라한다
# 변수의 데이터는 언제든지 변경할수 있다. (변할수 있다!)

# 변수 사용법
#    변수명 = 값

# 이와 같이 = 연산자를 사용하여 변수에 값을 저장하는 것을 대입(assign 한다 라고 하며
# = 을 대입연산자 (assignment operator) 라고 한다

# ★★프로그래머는 변수에 어떠한 타입의 어떠한 값이 담겨 있는지 놓치면 안된다!   타입! 값!

# 변수명은 대소문자 구분한다

a = 10 # a 라는 변수에 int 값 10을 대입

print('a =', a)
print(type(a))

b = 5 # b라는 변수에 정수 5를 대입

print(a + b)

# NameError : 선언한적 없는 변수 사용 불가
# print(c)

# print(A) # a 와 A 는 다르다. 변수명은 대소문자 구분한다.

print('-' * 20)

# 형변환 함수
# int(), float(), str(), bool() ...

myName = "김만수" # myName은 "Hello" 라는 str 문자열 대입됨.

print('제 이름은', myName, "입니다")
print('제 이름은' + myName + " 입니다")

age = 10

print("네 나이는", age, "살 입니다")
# print("네 나이는" + age + " 살 입니다")

# 형변환 함수 사용. 숫자->문자, 문자->숫자 타입으로 변환 가능
# print("제 나이는" + age + "살 입니다") # 형변환 함수 str() 을 사용하여 문자열로 변환된 결과값 사용

num5 = "100"
# print(num + 2)
print(int(num5) + 2)

# int('hello') # 형변환 불가능하면 ValueError

# -------------------------------------------------
# 진법

# 진법에 대해서 형변환 함수에 매개변수 줄 수 있다.
print(int("110")) # 디폴트, 10진수(base 10)으로 인식하여 정수 변환
print(int("110", 8)) # "110"을 8진수로 인식하여 정수 변환
print(int("110", 2))

# 실수 -> 정수 변환
print()
print(int(3.14)) # 소수점 이하 제거

# 정수 -> 실수 변환
print(float(10))

# 변수의 size (byte)
import sys
x = 2 # int
print(sys.getsizeof(x), 'byte') # 변수나 값의 용량(byte)

x = 2.0 # float
print(sys.getsizeof(x), 'byte')