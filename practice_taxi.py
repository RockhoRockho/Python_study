# Taxi 클래스 설계하기
# '택시'에는 승객들에게 공통적으로 적용되는 자료 - 클래스네임
# - 택시 요율 (거리당 요금)  : 700 ( 거리 1km 당 요금 )
# - 기본 요금 : 3000
# - 최초 기본 주행 거리 : 2km 

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성 - 인스턴스 네임

# 거리에 따른 요금 계산 메소드 정의 (동작)
# 거리에 따른 잔돈 계산 메소드 정의 (동작)


# 기본요금 : 3000
# 기본주행거리 : 2 km
# 거리당 요율 : 700  (거리 1km당 요금)

"""
passenger1 = Taxi(20000, 1)   # 20000원을 가지고 거리 1km 이동하는 경우

#passenger1 의 비용은 ? → 3000
#passenger1 의 잔돈은 ? → 17000

passenger1.calc_cost(), passenger1.get_change()


passenger2 = Taxi(30000, 10)   # 30000원을 가지고 거리 10km 이동하는 경우
# passenger2 의 비용은 ? → 8600
# passenger2 의 잔돈은 ? → 21400
passenger2.calc_cost(), passenger2.get_change()

"""

class Taxi:
    b_rate = 3000
    b_dist = 2
    per_dist = 700

    def __init__(self, money, dist):
        self.money = money
        self.dist = dist

    def calc_cost(self):
        self.cost = Taxi.b_rate
        if self.dist > Taxi.b_dist:
            self.cost = (self.dist - Taxi.b_dist) * Taxi.per_dist + Taxi.b_rate
        return self.cost

    def get_changes(self):
        return self.money - self.cost

passenger1 = Taxi(20000, 1)
print(passenger1.calc_cost(), passenger1.get_changes())

passenger2 = Taxi(30000, 10)
print(passenger2.calc_cost(), passenger2.get_changes())















