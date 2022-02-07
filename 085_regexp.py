"""
  대표적인 정규 표현식 
  구글링 하면 대표적인 정규표현식들이 많이 구할수 있습니다.
  각 정규표현식들을 작성해보고
  매칭되는 문자열과 그렇지 않은 것들을 출력해봅시다.   
"""
import re


title = "URL"
regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$\-@\.&+:/?=]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
input_list = [
    'http://www.naver.com'
]

title = "email"
regex =  '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
input_list = [
    'dkssusaos123@naver.com'
]

title = "주민등록번호"
regex = r"(\d{6})[-]\d{7}"
input_list = [
    '921231-1234213'
]

title = "날짜 YYYY-MM-DD"
regex = '((\d{4})|\d{2})?(-|/|.)?(?P<month>[1-9]|0[1-9]|1[0-2])(-|/|.|월 )(?P<date>([1-9]|0[1-9]|[1-2][0-9]|3[01]))일?$'
input_list = [
    '2020-12-30'
]

title = "자연수"
regex = r'[^-]+[1-9]\d*'
input_list = [
    '23',
    '-23'
]

# title = "정수"
# regex = r'^[^0]\d*'
# input_list = [
#     '01234',
#     '23',
#     '-23'
# ]

# title = "소수"
# regex = r'^[+-]?\d*(\.?\d*)$'
# input_list = [
#     '231.23',
#     '23154.23234'
# ]

# title = "소수점 둘째자리까지"
# regex = r'\d+(\.\d{1,2})?'
# input_list = [
#     '231.23',
#     '23154.23234'
# ]

# title = "1000 단위 콤마 자연수"
# regex = '^[+]?[\d,]*$'
# input_list = [
#     '123,234',
#     '234,213,123'
# ]


for s in input_list:
    print("[정규표현식 매칭 테스트]-----------------")
    print("정규표현식: " + regex)
    print("입력문자열: " + s)

    match_count = 0

    for match in re.finditer(regex, s):
        match_count += 1
        print(f'   매치{match_count}: {match.group()} ({match.start()} - {match.end()})')

        # 그룹이 있다면 그룹별로 출력
        group_size = len(match.groups())
        for i in range(1, group_size + 1):
            print(f'\t   group{i}: {match.group(i)} ({match.start(i)} - {match.end(i)})')


    if match_count == 0: print('    X매치 없슴X')
    print()