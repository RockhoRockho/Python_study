# 상속 연습

# 정사각형(Square)
#   └─ 정육면체 (Cube)

#  1. '정사각형' 객체 정의
#  클래스 이름 : Square
#  생성자 : '한 면의 길이(side)'를 받아서 초기화
#  면적을 계산하여 리턴하는 메소드 : getArea()

# 2. '정육면체' 객체 정의 <-- Square 상속받아 정의
#  클래스 이름 : Cube
#  getArea() : 정육면체의 총 면적
#  getVolume() : 정육면체의 부피 계산

class Square:
    def __init__(self, side):
        self.side = side

    def getArea(self):
        return self.side ** 2

class Cube(Square):
    def getArea(self):
        return self.side ** 2 * 6
    def get_volume(self):
        return self.side ** 3

sq1 = Square(2)
sq2 = Square(1)
print(sq1.getArea())
cub1 = Cube(2)
print(cub1.getArea())
print(cub1.get_volume())

# cub1으로 부모의 getArea()를 호출할 수 있을까?
print(Square.getArea(cub1))

# super(하위클래스 이름, 하위클래스 객체)
print(super(Cube, cub1))
print(super(Cube, cub1).getArea())