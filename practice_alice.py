## 실습] 파일의 단어 빈도수 구하기 
## alice30.txt

# 오로지 알파벳만. 계수하기
# 대소문자 구문없이 비교 : The, the
# 글자수 2개 이상인 단어만 카운트 하기 : a, I <-- 제외
# 빈도수 100회 이상인 단어만 카운트

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""

# 파일 읽기 “alice30.txt"

# 알파벳 대/소문자 변환 : lower(), upper()

# 알파벳 아닌거 제거 (알파벳 아닌 글자는 공백으로 치환)

# 단어 추출 (2글자 이상인 단어만) : split()

# 등장 빈도 계수 --> { } 로 만들기

# 100번이상 등장한것만 출력


from functools import reduce
import re

with open(r'D:\DevRoot\dataset\alice30.txt', 'r') as f:
    lines = f.read().lower()
    lines = re.sub(r'\W|\d', ' ', lines)
    lines = re.findall(r'\w\w+', lines)
    lines = reduce(lambda x, y: x.update({y: x.get(y, 0) + 1}) or x, lines, {})
    lines = filter(lambda x: x[1] >= 100, lines.items())
    lines = sorted(lines, key=lambda x: x[1], reverse=True)
    print(lines)