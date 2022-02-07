# 정규표현식 regular expression

# 문자열 검색, 치환  등의 동작에 있어서
# 단순한 '문자열 비교' 를 하는 것이 아니라 
# 특정 '패턴'과 비교하고자 할때 이를 단 몇줄의 코드로 구현 가능!
# 주어진 문자열에서 패턴을 찾아내는 것을 '패턴 매칭(pattern matching)' 이라 함

# 사용자가 입력한 문자열 패턴 유효성 체크 등에 많이 사용
#  		ex) 주민등록번호, URL, email, 비밀번호, 
#  			날짜포맷(yyyy-mm-dd) 
#  			전화번호(010-xxxx-xxxx) ... 

# 장점: 코딩량 저감, 거의 대부분의 언어에서 공용으로 사용.
# 단점: 처음에 배우기 어렵고, 코드 가독성 떨어뜨림.

import re

# 정규표현식 패턴문자열 -> re.compile 객체 생성
# compile 객체의 메소드를 사용하여 패턴 매칭(검색, 치환)

#  정규표현식		설명
#  ^			문자열 시작
#  $			문자열 종료
#  .			임의의 문자 [단 ‘'는 넣을 수 없습니다.]
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
#  (?i)			대소문자를 구분하지 않습니다.

import re

regex = 'My....'; # My로 시작하고 임의의 문자 4개의 매칭
pat = re.compile(regex)
print(pat, type(pat))

# 위 패턴객체를 사용하여 문자열 검색 가능

# match()  문자열의 처음부터 정규식과 매치되는지 조사한다.
# search()  문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
# findall()  정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다
# finditer()  정규식과 매치되는 모든 문자열(substring)을 iterator 객체로 리턴한다
# sub()  정규식과 매칭되는 문자열 치환

mat = pat.match("My1234") # 문자열 전체가 패턴에 매칭되면 Match 객체 리턴
print(mat)
print(mat.span()) # (0, 6) 매칭된 범위
print(mat.group()) # 매칭된 문자열

mat = pat.match("My12345")
print(mat)
print(mat.span())
print(mat.group())

mat = pat.match("-My12345") # 매칭이 안되면 None을 리턴
print(mat)

mat = pat.search("-My12345")
print(mat)

# search()는 여러개의 매칭이 발생되더라도 최초 매칭된 것 하나만 리턴
mat = pat.search("aaaMy000   My1111---- My33 3 --")
print(mat)

# findall() 매칭된 문자열들을 list로 리턴
result = pat.findall("aaaMy000   My1111---- My33 3 --") # 맨 처음 발견된 것만 찾음
print(result)

# fint
result = pat.finditer("aaaMy000   My1111---- My33 3 --")
print(result)

for mat in result:
    print(mat)

# ---------------------------------------------------------
# Match 객체의 메소드들

# 어떤 문자열이 매치되었는가?
# 매치된 문자열의 인덱스는 어디서부터 어디까지인가?

# group()	매치된 문자열을 리턴한다.
# start()	매치된 문자열의 시작 위치를 리턴한다.
# end()	매치된 문자열의 끝 위치를 리턴한다.
# span()	매치된 문자열의 (시작, 끝) 에 해당되는 튜플을 리턴한다.
print('-' * 20)
mat = pat.match("MyHistory")
print(mat)
print(mat.group())
print(mat.span())
print(mat.start())
print(mat.end())

# -----------------------------------------------------
# 패턴안의 그룹 (group)
# 정규표현식 패턴 안에서 ( ) (괄호) 로 묶으면 '그룹' 이 된다

print('-' * 20)
pat = re.compile("My(..)(..)")
mat = pat.match('My1234')
print(mat)
print(mat.groups()) # 매치에서의 그룹들

# 매개변수 없으면 매칭된 문자열 '전체'에 대한 결과
print(mat.group())
print(mat.span())
print(mat.start())
print(mat.end())

# 매개변수 1부터가 그룹
# 첫번째 그룹이 1번 그룹
print('그룹 1')
print(mat.group(1))
print(mat.span(1))
print(mat.start(1))
print(mat.end(1))

print('그룹 2')
print(mat.group(2))
print(mat.span(2))
print(mat.start(2))
print(mat.end(2))

p = re.compile('^([\\d]{1,2}):([\\d]{1,2}):([\\d]{1,2})$')
m = p.match("14:05:23")
print(m.groups())

# ---------------------------------------------------------------
# re.match()
# re.compile() + match()의 축약형

mat = re.match('My....', "My1234")
print(mat)

# re.search() : re.compile() + search()
# re.findall() : re.compile() + findall()
# re.finditer() : re.compile() + finditer()

# ----------------------------------------------------
# 정규표현식 문자열 사용할때는 가급적 raw string을 사용하자

print("a\n\da")
print("a\\n\da")
print(r"a\n\da")

p = re.compile('^([\\d]{1,2}):([\\d]{1,2}):([\\d]{1,2})$')
            # ↑ 위의 문자열처럼 보기 힘들게 만들지 말고
            # ↓ 가급적 raw string 사용하자.
p = re.compile(r'^([\d]{1,2}):([\d]{1,2}):([\d]{1,2})$')

# -------------------------------------------------------
# 치환
# re.compile() + sub()
# re.sub()

a = "123456-123456"
print(re.sub(r'\d', '*', a))
