#  정규표현식		설명
#  ^			문자열 시작
#  $			문자열 종료
#  .			임의의 문자
#  *			앞 문자가 0개 이상의 개수가 존재할 수 있습니다.
#  +			앞 문자가 1개 이상의 개수가 존재할 수 있습니다.
#  ?			앞 문자가 없거나 하나 있을 수 있습니다.
#  []			문자의 집합이나 범위를 표현합니다. -기호를 통해 범위를 나타낼 수 있습니다. ^가 존재하면 not을 나타냅니다.
#  {}			횟수 또는 범위를 나타냅니다.
#  ()			괄호안의 문자를 하나의 문자로 인식합니다. (그룹)
#  |			패턴을 OR 연산을 수행할 때 사용합니다.
#  \s			공백 문자
#  \S			공백 문자가 아닌 나머지 문자
#  \w			알파벳이나 숫자
#  \W			알파벳이나 숫자를 제외한 문자
#  \d			[0-9] 숫자
#  \D			숫자를 제외한 모든 문자

import re

title = " . : 어떤 문자든지 임의의 '한개의 문자' 에 매칭"
regex = r'x.z'
input_list = [
    "xyz",  # xyz
    "xxzdfdk",  # xxz
    "aa10x9zbxbz",  # x9z, xbz
    "xz",  # X
    "90x zxx_zdf",  # x z, x_z
    "xbz",  # xbz
    "xyyz"  # X
]

title = " () : () 안에 있는 글자들을 그룹화"
regex = r'(..).(..)'
input_list = [
    "abc",
    "abcbdbbacd",
    "abccabcabad"
]

title = "^ : 바로 뒤의 문자열로 시작됨"
regex = r'^The'
input_list = [
    "The Things",       # OK
    "On The Things",    # X
    " The The The",     # X
    "The The The",      # OK
]

title = "$ : 문자열의 마지막이 해당 문자열로 마무리"
regex = r'Man$'     # Man으로 끝나는 문자열
input_list = [
    "SuperMan",     # OK
    "AquaMan",      # OK
    "WonderWoman",  # X
    "WonderWoMan",  # X
    "PostMan "      # OK
]

title = "^표현식& : 정확하게 전체패턴 매칭되는 문자열"
regex = r'^SuperMan&'
input_list = [
    "SuperMan",
    "Super Man",
    " SuperMan",
    "SuperMan "
]

title = " * : 바로앞의 문자가 없거나 한개 이상에 매칭"
regex = r'ab*'
input_list = [
    "a",  # 1       a
    "abc",  # 2     ab
    "ab",  # 3      ab
    "abbbaaaabababbab",  # 4    abbb a a a ab ab abb ab
    "bbba",  # 5    a
    "cdef"  # 6     X
]

title = " + : 바로 앞의 문자가 꼭 한개 이상에 매칭"
regex = r'ab+'
input_list = [
    "a",  # 1       X
    "abc",  # 2     ab
    "ab",  # 3      ab
    "abbbaaaabababbab",  # 4    abbb ab ab abb ab
    "bbba",  # 5    X
    "cdef"  # 6     X
]

title = " ? : 바로 앞의 문자가 한개 있거나 없는 것에 매칭"
regex = r'ab?'
input_list = [
    "a",  # 1       a
    "abc",  # 2     ab
    "kkabcc",  # 3  ab
    "abbbaaaabababbab",  # 4    ab
    "bbba"  # 5     a
]

title = " [] : 안에 존재하는 문자들 중 한 문자만 매칭"
regex = r'[abc]'    # a또는 b또는 c중에 한 문자에 매칭
input_list = [
    "able",  # 1        a, b
    "bible",  # 2       b, b
    "cable",  # 3       c, a, b
    "xenosys",  # 4		X
]

regex = r'[abc]+'
# 1 ab
# 2 b b
# 3 cab
# 4 X

regex = r'[a-z]+'
input_list = [
    "abc100",
    "abcDefGHIUJ-KLM123opQrstuz"    # abc ef op rstuz
]

regex = r'[a-zA-Z]+'
regex = r'[a-zA-Z0-9]+'
regex = r'[0-9]+'

regex = r'[^a-zA-Z]+'   # []안에서 ^는 안의 문자들을 제외

title = " {} : 앞의 문자나 문자열의 등장횟수"
regex = r'ab{2}'    # a로 시작하고 b가 두 번 등장하는 패턴
input_list = [
    "abb",  # abb
    "abbb", # abb
    "abbbabbbbbbbbabaabab", # abb abb
]

regex = r'ab{2,}'    # b의 개수가 2개 이상
# 1 abb
# 2 abbb
# 3 abbb abbbbbbbb

regex = r'ab{3,5}'  # b의 개수가 3개에서 5개까지
# 1 X
# 2 abbb
# 3 abbb abbbbb

title = " | : OR 연산자 역할"
regex = r'a|b'  # a 또는 b 둘중 하나
input_list = [
    "a",    # a
    "b",    # b
    "ab",   # a b
    "xyz"   # X
]

title = r" \s : 공백, \S : 공백이 아닌 문자"
regex = r'\s+'
input_list = [
    "Hello My World",
    "He \tllo My World",
    "\n\t Hello My World\n\n",
]

regex = r'\S+'
# 1 3개
# 2 4개
# 3 3개

title = r" \w : 알파벳이나 숫자, \W ㅇ: 알파벳이나 숫자를 제외한 문자"
regex = r'\w+'
input_list = [
    'This is 2022-01-25 !!'
]

regex = r'\W+'

title = r" \d : [0-9] 숫자, \D : 숫자를 제외한 문자"
regex = r'\d+'
input_list = [
    'This is 2022-01-25 !!'
]

regex = r'\D+'

title = "escaped character 매칭시키기"
# regex = r'.+'   # 이렇게 하면 전체 문자열이 매칭된다
regex = r'[.]+'
regex = r'\.+'
input_list = [
    "My name is .."
]

# title = ""
# regex = r''
# input_list = [
# ]

for s in input_list:
    print("[정규표현식 매칭 테스트]-----------------")
    print("정규표현식: " + regex)
    print("입력문자열: " + s)

    match_count = 0

    for match in re.finditer(regex, s):
        match_count += 1
        print(f'    매치{match_count}: {match.group()} ({match.start()} - {match.end()})')

        # 그룹이 있다면 그룹별로 출력
        group_size = len(match.groups())
        for i in range(1, group_size + 1):
            print(f'\t    group{i}{match_count}: {match.group(i)} ({match.start(i)} - {match.end(i)})')


    if match_count == 0: print('     x매치 없음')
    print()





