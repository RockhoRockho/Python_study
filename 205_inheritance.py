# 2차원 원 Circle
#  └─ 3차원 구 Sphere

import math

# 2차원 원 Circle 객체 정의
class Circle:
    def __init__(self, radius = 0):
        self.radius = radius

    # 면적
    def get_area(self):
        return math.pi * self.radius ** 2

    # 둘레
    def get_perimeter(self):
        return math.pi * self.radius * 2

c1 = Circle()
c1.radius = 10
print(c1.get_area())
print(c1.get_perimeter())


# Circle을 상속받아서 Sphere(구) 객체를 만들기

class Sphere(Circle):

    # 부피 (새로 추가되는 기능)
    def get_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

s2 = Sphere(4)
print('s2의 부피:', s2.get_volume())

s3 = Sphere(10)
print('s4 의 넓이: ', s3.get_area())
print('s3 의 둘레: ', s3.get_perimeter())
print('s3 의 부피: ', s3.get_volume())

# 메소드 오버라이딩(overriding)
# 클래스가 상속관계에 있을때,
# 클래스의 메소드와 동일한 이름으로 자식 클래스 쪽에서 재작성 하는 것을
# 메소드 오버라이딩 이라 한다

import pprint
pprint.pprint(Circle.__dict__)

pprint.pprint(Sphere.__dict__)

# '구' 와 '원'은 다르다
# 기존의 Circle 의 getArea() 를 재정의 (오버라이딩) 해주어야 한다

# 구의 겉넓이 공식  :  4 x pi x r ** 2

class Sphere(Circle):
    # 부피 (새로 추가되는 기능)
    def get_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    # 넓이 (오버라이딩)
    def get_area(self):
        return 4 * math.pi * self.radius ** 2

s4 = Sphere(10)
print('s4 의 넓이: ', s4.get_area())
print('s4 의 둘레: ', s4.get_perimeter())
print('s4 의 부피: ', s4.get_volume())


import pprint
pprint.pprint(Circle.__dict__)

pprint.pprint(Sphere.__dict__)