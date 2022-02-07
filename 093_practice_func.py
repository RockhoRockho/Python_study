# 반지름은 입력받아
# 원의 둘레를 계산하여 리턴하는 함수를 작성하세요
# 정의, 호출

# TODO

import math

def calc_perimeter(radius):
    perimeter = 2 * radius * math.pi
    return perimeter

result = calc_perimeter(10)
print('둘레=', result)

# 반지름은 입력받아
# 원의 면적를 계산하여 리턴하는 함수를 작성하세요
# 정의, 호출

# TODO

def calc_size(radius):
    size = math.pi * radius ** 2
    return size
result = calc_size(10)
print('원의 면적=', result)

# 직사각형의 '가로', '세로' 의 크기를 입력받아
# 직사각형의 넒이를 구하는 함수를 작성하세요
# 정의, 호출

def square_size(v, h):
    size = v * h
    return size
result = square_size(5, 4)
print('직사각형 넓이=', result)

# TODO

# 직각삼각형의 '밑변'과 '높이'가 주어졌을때
# 빗변의 길이를 구하는 함수를 작성하세요
# 정의, 호출

def triangle_size(v, h):
    size = v * h / 2
    return size
result = triangle_size(5, 4)
print('직각삼각형 넓이=', result)

# TODO

# 반지름은 입력받아
# 원의 '둘레'와 '면적'을 계산하여 리턴하는 함수를 작성하세요
# 정의, 호출

def calc(radius):
    perimeter = 2 * radius * math.pi
    size = radius ** 2 * math.pi
    return perimeter, size
perimeter, size = calc(10)
print(f'원의 둘레= {perimeter}, 원의 면적={size}')

# 정규표현식 연습 사이트 추천
# : https://regexr.com/    (정규식 , 문자열 매칭 연습)
# : https://regexone.com/  ( step by step 으로 연습 하기 좋음)
# : https://regexper.com/  (특징: 시각화, 정규식을 이미지로 다운가능)
# : https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html  (오라클 공식)


