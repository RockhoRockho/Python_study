# 도전
# 일전에 filter, map으로 했던문제다. reduce 로 도전해보자

# 응용
# CSV 파일 데이터의 형태에서
data = """height,weight,label
140,45,normal
145,72,fat
150,61,fat
137,56,fat
192,48,thin
175,77,fat"""
print(data)


# 아래와 같은 리스트로 만들기
# [[140.0, 45.0, 'normal'],
#  [145.0, 72.0, 'fat'],
#  [150.0, 61.0, 'fat'],
#  [137.0, 56.0, 'fat'],
#  [192.0, 48.0, 'thin'],
#  [175.0, 77.0, 'fat']]

from functools import reduce

data = reduce(
    lambda r1, line: r1.append(
        reduce(
            lambda r2, e: r2.append(float(e) if e.isdigit() else e) or r2,
            line.strip().split(','),
            []
        )) or r1,
    data.split('\n'),
    []
)
print(data[1:])