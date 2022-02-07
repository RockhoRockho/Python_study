# Magic Method 매직 메소드란?
# 클래스안에 정의할 수 있는 스페셜 메소드이며 클래스를 int, str, list등의 파이썬의 빌트인 타입(built-in type)과 같은 작동을 하게 해준다.
# +, -, >, < 등의 오퍼레이터에 대해서 각각의 데이터 타입에 맞는 메소드로 오버로딩하여 백그라운드에서 연산을 한다.
# __init__이나 __str__과 같이 메소드 이름 앞뒤에 더블 언더스코어("__")를 붙인다.

# special method 라고도 한다 https://docs.python.org/3/reference/datamodel.html#specialnames

"""

연산자     메소드                     설명
─────────────────────────
         <binary operator>

 +      __add__(self, other)         덧셈
 *      __mul__(self, other)         곱셈
 -      __sub__(self, other)         뺄셈
 /      __truediv__(self, other)     나눗셈
 //     __floordiv__(self, other)
 %       __mod__(self, other)             나머지
 **      __pow__(self, other[, modulo])
 >>      __lshift__(self, other)
 <<      __rshift__(self, other)
 &       __and__(self, other)
 ^      __xor__(self, other)
 |      __or__(self, other)


             <Extended operator>
+=         __iadd__(self, other)
-=         __isub__(self, other)
*=         __imul__(self, other)
/=         __idiv__(self, other)
//=        __ifloordiv__(self, other)
%=         __imod__(self, other)
**=        __ipow__(self, other)
<<=        __ilshift__(self, other)
>>=        __irshift__(self, other)
&=         __iand__(self, other)
^=         __ixor__(self, other)
|=         __ior__(self, other)

        <unary operators>
-
+
abs()
~
complex()
int()
long()
float()
oct()
hex()



 <       __lt__(self, other)         작다(미만)
 <=      __le__(self, other)         작거나 같다(이하)
 ==      __eq__(self, other)         같다
 !=      __ne__(self, other)         같지 않다
 >      __gt__(self, other)          크다(초과)
 >=     __ge__(self, other)          크거나 같다(이상)
 [index]   __getitem__(self, index)   인덱스 연산자
 in       __contains__(self, value)   멤버 확인
 len     __len__(self)                요소 길이
 str      __str__(self)                문자열 표현


         __init__
         __del__
         __new__

         __repr__(self)              representative form
 """

s1 = "Hello"
s2 = "Python"


print(s1 + s2)  # '+' 연산자는 실제로 아래 __add__ 메소드가 동작하고 있던 것이다!
print(s1.__add__(s2))

print(s1 * 2)  # str * int
print(s1.__mul__(2))

print("PYTHON" > "Python")
print("PYTHON".__gt__("Python"))

print(s1[0])
print(s1.__getitem__(0))

score = [10, 20, 30, 40, 50]
print(score[2])
print(score.__getitem__(2))

print('e' in s1)
print(s1.__contains__('e'))


# repr, str 차이
# 공통점 : 객체를 문자열 리턴
# 차이점
#    `__repr__` : out 값
#    `__str__` : str(), print() 등에서 문자열(str) 변환시 호출됨,
#                 오버라이딩 안되어 있으면 __repr__ 의 값을 리턴한다

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s1 = Student('김혜원', 4)
print(s1)   # 기본적인 __repr__이 작동한 결과값

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):     # __repr__을 오버라이딩
        return f'이름 {self.name}, 학년 {self.grade}'

    def __str__(self):      # __str__을 오버라이딩
        return f'{self.name} : {self.grade}'
s1 = Student('김혜원', 4)
print(s1)   # __str__이 정의되어 있는 경우 __str__ 결괏값이 리턴됨

# ---------------------------------------------------------------------
# 원래 객체간의 + 연산은 불가능
print('-' * 20)

class Number:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return str(self.number)

f1 = Number(10)
f2 = Number(20)
print(f1, f2)
# print(f1 + f2)  # Number + Number <-- 연산 정의가 안되어 있으므로 불가

# MagicMethod를 오버라이딩 하면 객체간의 연산도 가능해진다.
print()
class Number:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return str(self.number)

    # Number에 대한 + 연산 정의
    def __add__(self, other):
        return self.number + other.number

f1 = Number(10)
f2 = Number(20)
print(f1 + f2)

f3 = Number(30)
print(f2 + f3)
# print(f1 + f2 + f3) # 에러다! 왜?
#  f1 + f2 => 30 (int)
#    30(int) + f3(Number)  는 불가

print()
class Number:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return str(self.number)

    # Number에 대한 + 연산 정의
    def __add__(self, other):
        return Number(self.number + other.number)

f1 = Number(10)
f2 = Number(20)
f3 = Number(30)
print(f1 + f2 + f3)







