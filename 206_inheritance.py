# 상속과 생성자 고찰

class Vehicle:
    def __init__(self, speed):
        print(f'Vehicle({speed}) 생성')
        self.speed = speed

# v1 = Vehicle() # 에러
v1 = Vehicle(100)

class Car(Vehicle):
    pass

# car1 = Car() # 에러

import pprint
pprint.pprint(Vehicle.__dict__)
pprint.pprint(Car.__dict__)

# -------------------------------------------
print('-' * 20)

class Vehicle:

    def __init__(self, speed = 0):
        print(f'Vehicle({speed}) 생성')
        self.speed = speed

class Car(Vehicle):
    pass

car1 = Car()
car1 = Car(10)

# ---------------------------------------------
print('-' * 20)

class Vehicle:

    def __init__(self, speed = 0):
        print(f'Vehicle({speed}) 생성')
        self.speed = speed

class Car(Vehicle):
    def __init__(self, oil = 0):
        # 파이썬은 부모생성자가 자동으로 호출되지 않는다.
        print(f'Car({oil}) 생성')
        self.oil = oil

car1 = Car()
print(car1.oil)
# print(car1.speed)   # 에러!  부모쪽의 생성자가 호출안되었으니..

# -------------------------------------------------------------
print('-' * 20)
# 상속받은 자식쪽에서 생성자를 제공하는 경우 (오버라이딩)
# 부모쪽의 생성자를 명시적으로 호출해줄 필요가 있다.

class Vehicle:

    def __init__(self, speed = 0):
        print(f'Vehicle({speed}) 생성')
        self.speed = speed

class Car(Vehicle):
    def __init__(self, oil = 0):
        super().__init__(20)   # 명시적으로 호출
        print(f'Car({oil}) 생성')
        self.oil = oil

car1 = Car(10)


# ---------------------------------------------------------
print('-' * 20)

class Vehicle:

    def __init__(self, speed = 0):
        print(f'Vehicle({speed}) 생성')
        self.speed = speed

class Car(Vehicle):
    def __init__(self, speed = 0, oil = 0):
        super().__init__(speed)   # 명시적으로 호출
        print(f'Car(speed={speed}, oil={oil}) 생성')
        self.oil = oil

car1 = Car(5, 9)

# ----------------------------------------------------

class HybridCar(Car):
    def __init__(self, electricity = 0, speed = 0, oil = 0):
        super().__init__(speed, oil)
        print(f'HybridCar(electricity ={electricity}, speed={speed}, oil={oil}) 생성')
        self.electricity = electricity

car1 = HybridCar(10, 5, 4)

# --------------------------------------------------------------
# 언제 상속관계로 만들것인가?

# IS-A 관계 => 상속관계로 만든다.
# HAS-A 관계?

# Vehicle
#  └─ Car
#      └─ HybridCar

#  Vehicle IS-A Car ?
#  Car IS-A Vehicle ?

# 반면에
# Car, Tire

# Car IS-A Tire ?  X
# Tire IS-A Car ?  X
#  따라서 위 둘은 상속관계로 만들면 안된다.

# Car HAS-A Tire ? O
# Tire HAS-A Car ? X
#  따라서 위 경우는 객체의 변수(필드)로 만들어 준다

class Tire:
    pass

class Car:

    def __init__(self):
        self.tire1 = Tire()
        self.tire2 = Tire()
        self.tire3 = Tire()
        self.tire4 = Tire()

