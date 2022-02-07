# 문자열 함수들
# 대표적으로 문자열(str)은 많은 함수(메소드)들을 갖고 있습니다.
# str 의 대표적인 함수들  ==>  split, join, replace, format

# https://docs.python.org/3/library/stdtypes.html#textseq

# str.  <-- 그리고 TAB 을 눌러보자
# "Hello".  <-- TAB 눌러보자

# 참고로
# https://docs.python.org/3/
# https://docs.python.org/2/

# 에서 찾고자 하는 함수의 기능에 대한 메뉴얼 확인 가능
# 좌상단 언어에서 korean 선택하면 한글번역 본도 제공됨 (일부만)

# 대부분의 문자열 메소드는 chaining 된다.

#-----------------------------------------------------
# upper() : 문자열을 전부 대문자로 만드는 함수
#  lower() : 문자열을 전부 소문자로 만드는 함수

str1 = "Apple"
print(str1, str1.upper(), str1.lower())

str2 = "APPLE"
print(str1 == str2)
print(str1.upper() == str2.upper())

# id: <-- 대소문자 구분 안하는 경우도 있다.
# pw: <-- 대소문자 구분

#----------------------------------------------
# strip()
# 문자열의 좌우 공백 제거

a = "   Hello, World!     "
print('[%s]' % a)
print('[%s]' % a.strip())

# 사용자 입력, 추출된 텍스트 데이터 정제 등의 과정에서 필수.

#------------------------------------------------------
# replace(a, b) 문자열 치환
# 주어진 문자열에서 a를 찾아 b로 치환
a = "Hello, World!"
print(a.replace("H", "J"))

# str은 immutable --> str 메소드의 결과로 원본이 변화되진 않는다.
# str의 메소드 결과(리턴값)은 새로운 str인 경우가 많다.
# 즉 뒤이어 계속 str 메소드 사용 가능. --> 메소드 체이닝(method chaining)

# 도전
# "  21,300원 "  --> 정수 21300 으로 바꾸기
a = "  21,300원 "
print(int(a.strip().replace("원", "").replace(",", "")))

#-------------------------------------------------------
# split(separator)
# str을 separator문자열로 구분하여 쪼갠뒤 list로 만들어서 리턴

# 사용예: 엑셀(csv)을 파이썬으로 읽어 왔을때 다음과 같이 콤마 로 데이터들이 구분되어 있을 것이다
data = "사과,바나나,파인애플,포도,복숭아"
print(data.split())
print(data.split(',', maxsplit=2)) # maxsplit: 몇개까지 쪼갤건지 지정

# split에 매개변수 없으면 '공백' 기준으로 쪼갬
# '공백' : ' ', '\n', '\t', '\r', ...
print("강아지 고양이 종달새".split())

# str.join() 함수
# split 과 반대로 list -> 하나의 str으로 묶어주는 함수
data = (["A", "B", "C", "d", "e"])
result = ",".join(data)
print(result)

data = ['2022', '01', '24']
print('-'.join(data))

# 도전
# "사과,바나나,파인애플,포도,복숭아"
#
# "사과-바나나-파인애플-포도-복숭아"
data = "사과,바나나,파인애플,포도,복숭아"
# TODO
print(data.replace(",", "-"))
print('-'.join(data.split(',')))

data= "데이터 분석을 위한 파이썬 프로그래밍"
# "파이썬" 을 => "Python" 으로 바꾸려면?
print(data.replace('파이썬', 'Python'))
print('Python'.join(data.split('파이썬')))

# --------------------------------------------------------------
# index(), find()함수
# 문자열 안에서 문자열 찾기
print('-' * 20)
str3 = 'hello python'
print(str3.index('lo')) # 찾았으면 0이상의 값 리턴
# print(str3.index('x')) # 발견하지 못하면 ValueError

print(str3.find('lo'))
print(str3.find('x')) # 발견하지 못하면 -1 리턴

# 파이썬 함수등에선, 예외 상황을 어떻게 처리하느냐에 따라
# 여러개의 함수/연산자들이 제공되는 경우가 많다.

# ----------------------------------------------------------
print('-' * 20)
# count()
str4 = 'aabababababbbababab'
print(str4.count('ba'))

# --------------------------------------------------------
# isdigit(), isnumeric(), isdecimal()
a = '12345678' # str 타입
print(a.isdigit())
print(a.isdecimal())
print(a.isnumeric())

print()

a = '3²'
print(a.isdigit())  # 단일 글자가 '숫자' 모양이면 True. 숫자처럼 생긴 '모든 글자' 를 숫자로 인정
print(a.isdecimal()) # 주어진 문자열이 int() 변환이 가능해야 True. 특수문자는 int 변환 안되니까 False
print(a.isnumeric()) # 숫자값 표현에 해당하는 문자열 까지 True. 제곱근, 분수. 거듭제곱..

print()

a = '⅔'
print(a.isdigit())
print(a.isdecimal())
print(a.isnumeric())

# -------------------------------------------------------------------------
# startswith(), endswith()
# 문자열이 특정 문자열로 시작/종료 하는지 여부
str5 = "https://www.nytimes.com/2000/01/01/news/visions-identity-a-generation-s-anthem-smells-like-teen-pressure.html"

print()
print(str5.startswith("http"))
print(str5.startswith("ftp"))

url = "www.naver.com"
if not url.startswith('https://'):
    url = "https://" + url
print(url)

#----------------------------------------------------------------
# ord() : 문자의 코드값
# chr() : 코드의 문자값

print()
print(ord('a'), ord('A'))
print(chr(97), chr(65))

print('알파벳 개수', ord('z') - ord('a') + 1)

# 초, 중, 종성
print('한글 개수', ord('힣') - ord('가') + 1)

# 연습
# 알파벳 소문자로 이루어진 리스트 작성
# List Comprehension 사용
# ['a', 'b', ... 'z']

result = [
    chr(i + ord('a'))
    for i in range(ord('z') - ord('a') + 1)
]
print(result)

data = [
        "aAaA",   # 1
        "aaAA",   # 2
        "AAaa",   # 3
        "AaAa"    # 4
        ]

print(sorted(data))
print(sorted(data, reverse=True))

# ---------------------------------------------------------
# str과 비교연산자

print("a" < "b")
print("abc" > "abd")
print("가마우지" > "까마귀")

