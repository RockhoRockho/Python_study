# list 는 iterable 하다.
# str 도 iterable 하다.

# str 의 index, slice, in

str2 = "hello python"
print(str2)
print(str2[0])
print(str2[1])
print(str2[11])
# print(str2[12])  # indexError

# 음수 인덱싱 가능
print(str2[-1])
print(str2[-4])

# 문자열 슬라이싱
print(str2[0:2])   # 0부터 2 전까지   [0, 2)
print(str2[3:9])
print(str2[6:])
print(str2[:5])   # 처음부터 5 전까지

# step
print(str2[:])
print(str2[::2])
print(str2[::-1])

# 도전
dd = "2022-01-20"

year = dd[0:4]
month = dd[5:7]
day = dd[8:10]
print(year, month, day)

# in 연산자, len() 가능
myStr = "Python"

print("t" in myStr)

print("t" in myStr)
print("Py" in myStr)
print("py" in myStr)

# sorted(str)
print(sorted(myStr)) # 알파벳 오름차순 (정확히는 코드값 오름차순)
# ※ 알파벳에서 대문자가 소문자보다 코드값이 작다

print(sorted(myStr, reverse=True))

print('-' * 20)
#----------------------------------------------------------
# str은 immutable하다!
# myStr[0] = 'K' 에러!
# myStr[0] = 'K'
# print(msyStr)

#----------------------------------------------------------
# str.join() : str → list로 쪼갬
animals = ["dog", "shark", "cat", "bird"]
result = "-".join(animals)
print(result)

# str.split() : str → list로 쪼갬
print(result.split("-"))

# split() 매개변수 없이 사용하면 공백 기준으로 문자열 쪼갬
# 공백 : 띄어쓰기, 탭, 줄바꿈...

myStr = "Hello Python 2022"
print(myStr.split())

myStr = "      Hello     \t\n\n    Python     \t     2022      "
print(myStr.split())

print(dd)
print(dd.split('-')) # '-' 기준으로 쪼갬.
# ※ 위와 같이 특정 문자열을 기준으로 동작할때
# 그러한 역할을 하는 문자열을 delimiter라고 한다.

# int(), float(), str()
# list() 형변환 함수

myStr = "animals"
print(list(myStr))

# 도전
# "animals" 문자열을 --> "a-n-i-m-a-l-s" 문자열로 바꾸어 보자
myStr = "animals"
result = "-".join(list(myStr))
print(result)

