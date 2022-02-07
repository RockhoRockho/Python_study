# 등급별 생존률 계산하기
# titanic.csv

# 컬럼 의미
# survival - Survival (0 = No; 1 = Yes)
# class - Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
# name - Name
# sex - Sex
# age - Age
# sibsp - Number of Siblings/Spouses Aboard
# parch - Number of Parents/Children Aboard
# ticket - Ticket Number
# fare - Passenger Fare
# cabin - Cabin
# embarked - Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
# boat - Lifeboat (if survived)
# body - Body number (if did not survive and body was recovered)


"""
3등급] 총 491 명, 생존 119 명, 생존률 24.2%
1등급] 총 216 명, 생존 136 명, 생존률 63.0%
2등급] 총 184 명, 생존 87 명, 생존률 47.3%
"""

# ------------------------------------------------------------------------
# 생노가다 방법

# with open('D:/DevRoot/dataset/titanic.csv', 'r') as f:
#     total = []
#     while True:
#         line = f.readline()
#         if not line: break
#         total.append(line.split(',')[1:3])
#
#     total = total[1:]
#     total_result = [0, 0, 0]
#     survived_result = [0, 0, 0]
#
#     for i in total:
#         if i[1] == '3':
#             total_result[2] += 1
#             if i[0] == '1':
#                 survived_result[2] += 1
#         elif i[1] == '2':
#             total_result[1] += 1
#             if i[0] == '1':
#                 survived_result[1] += 1
#         else:
#             total_result[0] += 1
#             if i[0] == '1':
#                 survived_result[0] += 1
#
#     for i in range(3):
#         print(f'{i+1}등급] 총 {total_result[i]} 명, 생존 {survived_result[i]} 명, 생존률 {(survived_result[i] / total_result[i]) * 100:.1f}%')


# ※ pandas 등 데이터 라이브러리는 사용하지 마세요

# reduce 활용
from functools import reduce

with open(r"D:\DevRoot\dataset\titanic.csv", "r", encoding="utf8") as f:
    S = reduce(lambda a, b: a.append(b.split(",")[1:3]) or a, f.read().split('\n')[1:], [])[:-1]
    Total = reduce(lambda a, b: a.update({int(b[1]) : a.get(int(b[1]), 0) + 1}) or a, S, {})
    Survival = reduce(lambda a, b: a.update({int(b[1]) : a.get(int(b[1]), 0) + 1 if b[0] != '0' else a.get(int(b[1]), 0)}) or a, S, {})
    for i in Total: print(f'{i}등급] 총 {Total[i]} 명, 생존 {Survival[i]} 명, 생존률 {Survival[i] / Total[i] * 100:.1f}%')