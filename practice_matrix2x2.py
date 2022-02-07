# 연습 : 2차원 행렬 객체 정의
# magic method 활용
"""
mt1 = Matrix2x2([10, 20], [30, 40])
mt2 = Matrix2x2([1, 2], [3, 4])

print(mt1) 실행 결과
    [10, 20]
    [30, 40] 

print(mt2) 실행 결과
    [1, 2]
    [3, 4]
    
print(mt1 + mt2) 실행결과
    [11, 22]
    [33, 44]
    
print(mt1 + mt2 + mt2 + mt2) 실행결과
    [13, 26]
    [39, 52]
"""
class Matrix2x2:
    def __init__(self, list1, list2):
        self.matrix = [list1, list2]

    def __repr__(self):
        return str(f'{self.matrix[0]}\n{self.matrix[1]}')

    def __add__(self, other):
        return Matrix2x2([self.matrix[0][0] + other.matrix[0][0], self.matrix[0][1] + other.matrix[0][1]],
                         [self.matrix[1][0] + other.matrix[1][0], self.matrix[1][1] + other.matrix[1][1]])

from functools import reduce

class Matrix2x2:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __repr__(self):
        return str(f'{self.list1}\n{self.list2}')

    def __add__(self, other):
        a = reduce(lambda x, y: x.append(self.list1[y] + other.list1[y]) or x, range(len(self.list1)), [])
        b = reduce(lambda x, y: x.append(self.list2[y] + other.list2[y]) or x, range(len(self.list2)), [])
        return Matrix2x2(a, b)


mt1 = Matrix2x2([10, 20], [30, 40])
mt2 = Matrix2x2([1, 2], [3, 4])

print(mt1)
print(mt2)
print(mt1 + mt2)
print(mt1 + mt2 + mt2 + mt2)