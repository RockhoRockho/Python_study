# 파일 (File) 다루기

# 1. 파일 생성하기

# 파일을 다루기 위해선 open(), close() 함수로 감싸여진다

# 파일객체 = open(파일 이름, 파일 열기 모드)
#   ... 파일객체사용 (읽기 or 쓰기)
#   ... 파일객체사용 (읽기 or 쓰기)
#   ... 파일객체사용 (읽기 or 쓰기)
# 파일객체.close()


# 파일 열기 모드
# r  읽기모드 - 파일을 읽기만 할 때 사용
# w  쓰기모드 - 파일에 내용을 쓸 때 사용.  해당 파일이 없으면 새로 생성.   해당 파일이 있었으면 삭제하고 새로 생성 ★
# a  추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용.  해당 파일이 없으면 새로 생성

f= open('새파일.txt', 'w')
print(type(f))
f.close()


# 파일에 쓰기 write()
f = open('새파일.txt', 'w')

for i in range(1, 11):
    data = f'Line {i}\n'
    f.write(data)

f.close()

# 읽기
# 한줄 읽기 readline()

f = open('새파일.txt', 'r')    # 읽기모드 'r'

line = f.readline() # 한줄읽기
print(line, end='')
line = f.readline() # 마지막으로 읽은 지점부터 한줄 읽기
print(line, end='')

f.close()

# 모든 라인 읽기
print('-' * 20)
# 방법1 : readline() 사용
# readline은 더 이상 읽을 라인이 없는 경우 None을 리턴

f = open('새파일.txt', 'r')
while True:
    line = f.readline()
    if not line: break  # 파일 끝까지 읽었으면 종료
    print(line, end="")
f.close()

print('-' * 20)
# 방법2 : readlines() 사용
# line들을 담은 list를 리턴

f = open('새파일.txt', 'r')
lines = f.readlines()
# print(lines)
print(''.join(lines))
f.close()

print('-' * 20)
# 방법3 : iterable 사용
# f <- 파일객체도 iterable하다!

f = open('새파일.txt', 'r')
for line in f: # 파일에서 한 line씩 뽑혀나옴
    print(line, end='')
f.close()

print('-' * 20)
# 방법4 : read() 사용
# 파일 전체 읽어옴.

f = open('새파일.txt', 'r')
data = f.read()
print(data)
f.close()

# -------------------------------------------
# 추가(append)

print('-' * 20)
f = open('새파일.txt', 'a')    # 추가모드
for i in range(11, 21):
    data = f'{i} Line appended\n'
    f.write(data)
f.close()

# -------------------------------------------
# with 구문
print('-' * 20)

# 매번 close() 를 해주는게 불편하고, 까먹기도 쉽다
# with 구문을 사용하면 자동적으로 close 해준다   (파이썬 2.5 부터 지원)

# 블럭 형태로 작성한다.
# 블럭이 끝나면 자동적으로 f를 close() 해준다.
with open('새파일.txt', 'r') as f:
    data = f.read()
    print(data)

# -------------------------------------------------
# 폴더 생성
import os

# 'out'폴더 존재여부 확인
print(os.path.exists('out'))
print(os.path.exists('jungol'))

if not os.path.exists('out'):
    os.makedirs('out')
    print('out 폴더 생성')
else:
    print('out 폴더가 이미 있습니다.')

# --------------------------------------------------
# 인코딩 문제

f = open('out/새파일.txt', 'w')
for i in range(1, 11):
    data = f'{i}번째 줄입니다\n'
    f.write(data)
f.close()

# Windows 는 시스템 인코딩이 기본 2byte (cp949, ANSI, euc-kr)이다
# 특별히 encoding 옵션을  지정하지 않으면 파일은 2byte 로 인코딩되어 있다
# ※ 반면 MAC, Linux 등에선 기본인코딩이 3byte (utf8) 이다
print()
with open('out/새파일.txt', 'r') as f:
    data = f.read()
    print(data)

# 명시적으로 encoding 옵션 지정
f = open('out/새파일utf-8.txt', 'w', encoding='utf8', errors='ignore')
for i in range(1, 11):
    data = f'{i}번째 줄입니다\n'
    f.write(data)
f.close()

print('-' * 20)
with open('out/새파일utf-8.txt', 'r', encoding='utf8') as f:
# with open('out/새파일utf-8.txt', 'r') as f:  # 읽어들일 파일과 encoding 이 다르면 에러
    data = f.read()
    print(data)





