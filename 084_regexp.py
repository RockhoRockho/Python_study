# 문자열에서 숫자만 추출하기

import re

string = '정가 14,500원'
# TODO
# 정규표현식 사용하여 int값 14500을 추출하기
# hint : sub() 사용하기
print(int(re.sub('\D+', '', string)))
regex = '\d'
print(''.join(re.findall(regex, string)))

