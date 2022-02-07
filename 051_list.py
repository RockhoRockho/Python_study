# 여러개의 데이터를 담는 집합 데이터 타입들..
#1. list   :  순서있다.  중복허용,  mutable
#2. tuple  :  순서있다,  중복허용,  immutable
#3. set : 순서없다,  중복허용안함
#4. dict : key, value 쌍으로 구성, 순서없다.

# list
"""
list

# list 는   [   ]  으로 만든다
# 데이터(원소) 들은 , 콤마로 구분한다
# 각 데이터(원소) 들은 어떠한 타입도 가능하다
"""

animals = ["dog", "cat", "bird", "fish"]
print(animals)
print(type(animals))

animals = [
    "dog",
    "cat",
    "bird",
    "fish"
]

animals = [
    "dog"
    , "cat"
    , "shark"
    , "fish"
]

animals = [
    "dog",
    "cat",
    "bird",
    "fish",  # 마지막 원소 뒤에 콤마 붙여도 에러 아님.
]

print(animals)

# index 인덱싱 가능
# list는 순서가 있다.

print(animals[0]) # index , 첫번째 원소는 0부터 시작한다.
print(type(animals[0]))
print(animals[1])

# print(animals[4]) # IndexError 발생

# 음수 인덱싱 가능!
print(animals[-1])

# 원소 변경 가능(mutable)
animals[2] = 'mouse'
print(animals)

# len() : 리스트의 원소 개수
print(len(animals)) # list의 원소의 개수
print(len(animals[2])) # str의 문자의 개수

# 중복 가능
fruits = ["apple", "banana", "apple", "kiwi"]
print(fruits)

# 비어있는(empty) 리스트 가능
data = []   # 비어있는 리스트
print(data, len(data), type(data))

#------------------------------------------------------
# 슬라이싱 (slicing)
#  데이터의 일부분 추출
#  범위 연산자 [:] 사용
#  step 값 사용 가능

animals = ["dog", "cat", "mouse", "bird", "fish"]
print(animals)

print(animals[0]) #  index
print(animals[0:3])  # 0 부터 3 전까지
print(animals[1:4])
print(animals[:2])  # 처음부터 2 전까지
print(animals[2:])  # 2부터 끝까지
print(animals[:])   # 전체

i = 2
print(animals[:i], animals[i:])

print('-' * 20)
# step 값
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myList[1:7])
print(myList[1:7:2])  # step 2  건너 띄는 값
print(myList[3::3])
print(myList[:])
print(myList[::])
print(myList[::2])
print(myList[5:0])  #[]
print(myList[5:0:-1])
print(myList[::-1]) # 역순, 뒤집기

print('-' * 20)
#----------------------------------------------------
# append() : 데이터 (원소) 추가.  리스트의 맨 뒤에
#  ※ list 는 mutable 하기 때문에 가능
print(animals)
animals.append('tiger')  # 원본 데이터 변경
print(animals)

animals.append('cat')  # 중복 데이터 허용
print(animals)

#---------------------------------------------------
# del() 원소 삭제
del(animals[1])
print(animals)

print('-' * 20)
#--------------------------------------------
# list 연산 +, *
animals = ["dog", "dog", "cat", "bird"]
colors = ["white", "blue", "red"]

# list + list => list
print(animals + colors)
print(animals * 2)

# animals 는 바뀌었나?
print(animals)  # 원본 변화 없습니다

#----------------------------------------------------------
# extend()
print('-' * 20)
print(animals)
print(colors)

animals.extend(colors)  # animals 에 원소 추가 (원본 변경)
print(animals)

colors.extend(["orange"])
# ↑ colors.append("orange") 와 결과는 같다.
#     그러나 속도는 더 빠르다!
print(colors)

# 주의! extend(str) 문자열을 더하면?
colors.extend("oak")
print(colors)

# extend(iterable) <-- 반드시 iterable 을 매개변수로 받는다
colors.extend(10)

# 파이썬의 함수설계 할때 (일반적으로)
# 원본을 변화시키는 함수는 - None을 리턴
# 원본을 변화시키지 않는 함수가 -> 결과를 리턴