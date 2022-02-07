# 지금까지의 프로그래밍은 '함수 중심'

# ex) 아래와 같이 goto() 함수 안에 필요한 인자를 넘겨준다

# goto("이길자", "집(논현동 188)")
# goto("김해성", "집(서초동 333)")

# 함수 중심이라는 것은 곧 '동작' 중심이라는 거다.

# 그러나 이는 '실세계'를 표현하는데는 한계가 있다.

# 사람이 인지하는 세상은 '객체 중심' 이기 때문이다

# 사람이 인지하는 세상은 '객체 중심' 이기 때문이다

# '객체 중심' 프로그래밍은 다음과 같다.

# 예시]
# Person 클래스(class) 안에 다음의 '틀' 을 정의
#     - 이름 : 이름 정보 담는 '속성'
#     - 집주소 : 주소 정보 담는 '속성'
#     - goHome() : 집으로 가는 '동작' 수행

# 사람객체(object)들 생성
# lee = Person("이길자", "논현동 188") <- 이름, 집주소 등에 대한 정보가 객체에 담김
# kim = Person("김해성", "서초동 333") <- 이름, 집수소 등에 대한 정보가 객체에 담김

# lee.goHome()
# kim.goHome()

# 프로그래밍의 중심이 '함수' 중심이 아니라, 각각의 객체 중심( lee, kim )..


# 객체는 클래스로 정의를 하고
# 클래스를 통하여 객체를 생성한다   생성된 객체를 인스턴스(instance) 라 한다

# 흔히 클래스(Class ) 를 '붕어빵 틀'이라 하고
# 객체(object) 를 Class 로 찍어낸 '붕어빵'에 비유하곤 한다

# 파이썬에선 다음 순서대로 클래스를 사용한 객체중심 프로그래밍을 한다
#     ① 클래스 정의, class 키워드 사용
#     ② 객체 생성 (생성자 사용),생성된 객체를 '인스턴스(instance)' 라 한다
#     ③ 객체 사용 (객체의 변수, 메소드)

# 클래스 이름은
# 변수나 함수 이름 정의하는 규칙과 거의 동일하나
# 관례적으로 첫글자는 대문자로 한다

# 1. 클래스 정의 , (붕어빵틀)
class Cookie:
    pass

# 2. 객체 생성,   붕어빵 찍어내기


a = Cookie()  # Cookie 객체 생성.  변수 a 는 Cookie 의 인스턴스
b = Cookie()
c = Cookie()

print(type(a))
print(type(b))
print(type(c))

# == , is
print(type(a) is Cookie)
print(a == b)  # 타입만 같을 뿐 다른 인스턴스다.


# 클래스를 통해 만들어진 객체를 인스턴스(instance)라고도 한다
# 객체와 인스턴스는 다소 혼용되어 표현되기도 한다.
# "a 는 Cookie 의 객체" 다
# "a 는 Cookie 의 인스턴스" 다

# 객체의 '속성' --> 객체변수로 정의
# 객체의 '동작' --> 객체함수(메소드)로 정의

# 클래스 가 가져야 하는 변수를 '객체변수(instance variable)',
# 혹은 속성값 (attribute value) 혹은 멤버변수(member variable) 이라고도 함
# 혹은 필드 (field) 라고도 함
# 어떠한 메소드에서도 self. 키워드를 사용하여 정의 가능하고
# 인스턴스를 통해 생성도 가능.


# 객체변수 사용구문   . 사용
#   객체.객체변수

# 생성자 (Constructor)  __init__()
# 객체가 생성될때 자동으로 호출되는 특별한 메소드
# 주로 객체변수를 정의하고 초기화 하는 역할 수행

# 클래스 안에서 정의된 함수를 메소드(method) 라 함
# 메소드 호출 구문    . 사용
#    객체.메소드()
# 메소드가 호출될때는 해당 '객체' 에 대해서 동작하게 됨

# 모든 메소드는 기본적으로 첫번째 매개변수가 self 이다.

# ----------------------------------------------------------------

# 사각형 이란 객체에 대해 설계해보자
# 사각형 class 정의

# 사각형의 속성은 ? -> 가로(width),  세로(height)
# 사각형의 동작은 ? ->
#                   사각형의 넓이 구하기
#                   사각형의 둘레 구하기

# Rectangle 객체 정의
class Rectangle:
    def __init__(self):  # 생성자
        print('Rectangle() 생성자 호출')
        # 객체변수들 (속성)
        self.width = 0  # 객체변수 width 선언, 초깃값 0
        self.height = 0  # 객체변수 height 선언, 초깃값 0

    # 사각형의 넒이 구하기
    def get_area(self):
        area = self.width * self.height
        return area

    # 사각형의 둘레 구하기
    def get_perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter

    # 매개변수 있는 메소드
    def set_data(self, width, height):
        self.width = width
        self.height = height


r1 = Rectangle()

print('r1.width =', r1.width)
print('r1.height =', r1.height)

r2 = Rectangle()

print('r2.width =', r2.width)
print('r2.height =', r2.height)

r1.width, r1.height = 100, 200
r2.width, r2.height = 50, 30

print(r1.width, r1.height)
print(r2.width, r2.height)

r1.area = 19  # 파이썬에선 class 에선 정의되어 있지 않았던 변수들을 객체에 추가 가능.
print(r1.area)

area = r1.get_area()
perimeter = r1.get_perimeter()

print(f'r1 의 넓이 = {area}')
print(f'r1 의 둘레 = {perimeter}')

area = r2.get_area()
perimeter = r2.get_perimeter()

print(f'r2 의 넓이 = {area}')
print(f'r2 의 둘레 = {perimeter}')

# 메소드에서 첫번째 매개변수 self.

# 다음 두가지는 완전히 동일
r2.set_data(55, 120)

Rectangle.set_data(r2, 55, 120)  # <-- 잘 사용하지는 않지만 이과 같이도 호출 가능하다는

name = "Mike"

print(name.isalnum())
print(str.isalnum(name))
print(str.isalnum)


# ---------------------------------------------------
# 생성자 매개변수
#   객체변수 초기화에 사용된다.
#   디폴트 매개변수 사용 가능!

class Rectangle:
    def __init__(self, width, height=0):  # 생성자 매개변수
        print(f'Rectangle({width}, {height}) 생성자 호출')
        # 객체변수들 (속성)
        self.width = width  # 생성자 매개변수로 객체변수 초기화
        self.height = height

    # 사각형의 넒이 구하기
    def get_area(self):
        area = self.width * self.height
        return area

    # 사각형의 둘레 구하기
    def get_perimeter(self):
        perimeter = (self.width + self.height) * 2
        return perimeter

    # 매개변수 있는 메소드
    def set_data(self, width, height):
        self.width = width
        self.height = height


# r1 = Rectangle()
r1 = Rectangle(30, 20)

print('r1의 넓이 =', r1.get_area())
print(r1.width, r1.height)

r2 = Rectangle(100)
print(r2.width, r2.height)

# 오버로딩(overloading) ??
#   동일 이름의 메소드를 중복해서 여러개 정의하는 것.
#   매개변수 리스트 등을 달리하여 중복 정의 가능.
#   객체지향 기술에서 메소드의 다형성중 하나


# 파이썬에선 함수의 오버로딩이 존재한진 않지만
#   디폴트 파라미터, 가변매개변수 (*args, **kwargs) 들을 사용하면
#   동일한 효과를 볼수 있다.

# ----------------------------------------------------------------
# 객체 생성 연습 : Circle

# 연습 : 원에 대한 객체 정의

#  클래스 정의 Circle
#  객체변수는 반지름  (radius)
#  생성자
#  원의 반지름 설정하는 메소드 set_radius(radius)
#  원의 반지름을 리턴하는 메소드 get_radius()
#  원의 넓이 계산하여 리턴하는 메소드  get_area()
#  원의 둘레 계산하여 리턴하는 메소드  get_perimeter()

# 원주율은 3.141592 로 하자  (후에 math 모듈을 배우면 math.pi 로 사용하면 된다)

# class 정의, 인스턴스들 생성. 동작 시켜 보기

import math


class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


c1 = Circle()
c1.set_radius(10)
area = c1.get_area()
perimeter = c1.get_perimeter()

print('c1 의 넓이:', area)
print('c1 의 둘레:', perimeter)



# --------------------------------------------------
#  클래스 정의 Point2D

#  객체변수는 x, y
#  생성자 : x, y 초기화
#  좌표 설정 메소드 set_point(..)
#  좌표 리턴하는 메소드 get_point()
#  원점에서 부터 거리 계산 get_distance()
#  두 점 사이의 거리 계산 get_distance_from(other)

# 파이썬에서 root 구하는 함수는
# import math 후
# math.sqrt(x) 사용   혹은   x ** 0.5

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y

    def get_distance(self):  # 원점으로부터의 거리
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # 다른 Point2D 객체(other) 와의 거리
    def get_distance_from(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

print('-' * 20)
p1 = Point2D(1, 2)
print(p1.get_point())
print(p1.get_distance())

p2 = Point2D(0, 2)
print(p2.get_distance())

p3 = Point2D(0, -1)
print(p2.get_distance_from(p3))
print(p3.get_distance_from(p2))


# --------------------------------------------------------------------
# dict 속성

# 인스턴스의 __dict__ 속성
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)

print(p1.__dict__['x'])


# 클래스의 __dict__ 속성
import pprint
pprint.pprint(Point2D.__dict__)

# 클래스의 맴버 (속성, 메소드) 추가 삭제 가능
p1.color = 'RED'
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)

print()

del(p2.y)
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)















