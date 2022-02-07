# 디렉토리 관리 os 모듈
import os

print(os.path.curdir)

# 폴더 존재 확인, 생성

savedir = 'tmpdir1'
testdir_1 = 'testdir_1'

newdir = "./" + savedir + "/" + testdir_1
print(newdir)

print(os.path.join(savedir, testdir_1))
print(os.path.join('aaa', 'bbb', 'ccc', 'ddd'))

# makedirs() 한꺼번에 중간경로(intermediate directories)들 생성
# 반면에 mkdir()은 단일 디렉토리만 생성


if not os.path.exists(newdir):
    os.makedirs(newdir)
    print(newdir, '폴더생성')
else:
    print(newdir, '폴더가 존재합니다')

newdir = os.path.join("tmpdir1", "testdir_2")
if not os.path.exists(newdir):
    os.makedirs(newdir)
    print(newdir, '폴더생성')
else:
    print(newdir, '폴더가 존재합니다')

newdir = os.path.join("tmpdir2", "testdir_3")
if not os.path.exists(newdir):
    os.makedirs(newdir)
    print(newdir, '폴더생성')
else:
    print(newdir, '폴더가 존재합니다')

newdir = os.path.join("tmpdir2", "testdir_4")
if not os.path.exists(newdir):
    os.makedirs(newdir)
    print(newdir, '폴더생성')
else:
    print(newdir, '폴더가 존재합니다')

# 임시파일 생성
filelist = [
    "./tmpdir1/file1.txt",
    "./tmpdir1/testdir_1/file11.txt",
    "./tmpdir1/testdir_1/file12.txt",
    "./tmpdir1/testdir_2/file21.txt",
    "./tmpdir1/testdir_2/file22.txt",
    "./tmpdir2/file2.txt",
    "./tmpdir2/testdir_3/file31.txt",
    "./tmpdir2/testdir_3/file32.txt",
    "./tmpdir2/testdir_4/file41.txt",
    "./tmpdir2/testdir_4/file42.txt"
]

for file in filelist:
    with open(file, 'w') as f:
        pass

# --------------------------------------------------
print(os.path.dirname("./tmpdir2"))  # <-- 주어진 경로가 어느위치에 있는지 확인

print(os.path.dirname('aaa')) # 없는 경로는 empty str

print(os.path.dirname('./tmpdir2/testdir_1'))

# 절대 경로 추출
print(os.path.abspath('./tmpdir2/testdir_1'))

# 전체 경로에서 파일명 추출
fpath = os.path.abspath('./tmpdir1/testdir_8/file7.txt')
filename = os.path.basename(fpath)
print('filename =', filename)

# 파일명에서 '이름', '확장자' 추출
print(os.path.splitext(filename))

# 파일, 디렉토리 목록을 list로 추출
root_path = "./tmpdir1"
print(os.listdir(root_path))

# '파일' 혹은 '디렉토리' 여부까지 추출

for directory in os.listdir(root_path):
    path = os.path.join(root_path, directory)
    print(directory, end='-')
    if os.path.isdir(path): print('directory')
    if os.path.isfile(path): print('file')

# os.walk()
#  디렉터리 트리구조를 순회(traversing generator)
#  iterable 하다
print()
for root, dirs, files in os.walk("./tmpdir1"):
    print(root, dirs, files)

# 도전
# 도전!
# tmpdir1 디렉토리의 파일, 디렉토리 전체 리스트 업 해보기
# 전체경로로 출력하기

# .\tmpdir1\file1.txt
# .\tmpdir1\testdir_1
# .\tmpdir1\testdir_1\file11.txt
# .\tmpdir1\testdir_1\file12.txt
# .\tmpdir1\testdir_2
# .\tmpdir1\testdir_2\file21.txt
# .\tmpdir1\testdir_2\file22.txt
# .\tmpdir1\testdir_1\file11.txt
# .\tmpdir1\testdir_1\file12.txt
# .\tmpdir1\testdir_2\file21.txt
# .\tmpdir1\testdir_2\file22.txt

print('-' * 20)

# 사용 함수
# os.walk()
# os.path.join()
# os.path.abspath()

def enum_all(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            fname = os.path.join(root, f)
            print(os.path.abspath(fname))
        for d in dirs:
            dname = os.path.join(root, d)
            print(os.path.abspath(dname))

enum_all("./tmpdir1")

# -------------------------------------
# 파일 디렉토리 삭제

filelist = [
    "./tmpdir1/file1.txt",
    "./tmpdir1/testdir_1/file11.txt",
    "./tmpdir1/testdir_1/file12.txt",
    "./tmpdir1/testdir_2/file21.txt",
    "./tmpdir1/testdir_2/file22.txt",
    "./tmpdir2/file2.txt",
    "./tmpdir2/testdir_3/file31.txt",
    "./tmpdir2/testdir_3/file32.txt",
    "./tmpdir2/testdir_4/file41.txt",
    "./tmpdir2/testdir_4/file42.txt"
]

for file in filelist:
    os.remove(file)     # 파일 삭제
    print(file, '을 삭제했습니다')

dirlist = [
    "./tmpdir1/testdir_1",
    "./tmpdir1/testdir_2",
    "./tmpdir2/testdir_3",
    "./tmpdir2/testdir_4",
    # "./tmpdir1",
    # "./tmpdir2"
]

for dir in dirlist:
    os.removedirs(dir)
    # removedirs() 는 재귀적으로  끝단의 디렉토리부터 부모까지 차례로 제거

print(os.sep)  # 운영체제별 separator 문자
print(os.getcwd())  # 현재 작업 경로 (current working directory)

cwd = os.getcwd()

# cwd 변경하기
os.chdir('D:/DevRoot')
print(os.getcwd())
os.chdir(cwd)

# -----------------------------------------------------------------
# - glob 모듈
#  파일들의 목록을 편리하게 추출
#  와일드 카드 사용가능

import glob
print('-' * 20)
result = glob.glob('*.*') # 파일목록을 list로 리턴
print(result)

print()
result = glob.glob('*regexp.py')
print(result)

result = glob.glob(r'D:\**\**\*.csv')
print(result)

# --------------------------------------------------
# shutil : shell utility
#  파일 및 디렉토리 작업

import shutil

print('-' * 20)

# 실습용 폴더
test_dir3 = 'tmpdir3'

if not os.path.exists(test_dir3):
    os.makedirs(test_dir3)

# 현재 작업 폴더 변경하기
os.chdir(test_dir3)

# 현재 작업폴더 확인
print(os.getcwd())

# 실습용 파일 생성
with open('sample.txt', 'w') as f:
    pass

# 파일 복사 copy() 함수
result = shutil.copy('sample.txt', 'sample_copy.txt')
print('copy됨', result)

# 디렉토리 구조 복사 copytree(src, dst)
sub_dir = os.path.join('sub1', 'sub2', 'sub3', 'sub3')
print(sub_dir)

if not os.path.exists(sub_dir):
    os.makedirs(sub_dir)

# 부모 디렉토리로 '현재 작업경로' 이동
os.chdir("..")  # .. : parent directory
print(os.getcwd())

shutil.copytree('tmpdir3', 'tmpdir4')

# 디렉토리 이동하기 move()
shutil.move("tmpdir4", "tmpdir5")
# rename과 같은 효과
# 파일/디렉토리의 이름을 변경하고자 할때 사용

# 디렉토리 삭제하기 rmtree()
shutil.rmtree('tmpdir5')
#   주어진 경로부터 이하 디렉토리들 삭제
#   os.remove() : 파일 삭제
#   os.removedirs() : 재귀적으로 끝에서부터 부모까지 삭제



















