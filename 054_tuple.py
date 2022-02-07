# 여러개의 데이터를 담는 집합 데이터 타입들..
#1. list   :  순서있다.  중복허용,  mutable
#2. tuple  :  순서있다,  중복허용,  immutable
#3. set : 순서없다,  중복허용안함
#4. dict : key, value 쌍으로 구성, 순서없다.

# tuple 튜플 데이터 타입
#  콤마 , 로 구분된 집합 데이터 타입

animals = ("dog", "dog", "cat", "bird")
print(animals)
print(type(animals))

student = "김이박", "최성구", "정소우"
print(student)
print(type(student))

print(len(animals))

animals = ["dog"] # length 1인 리스트

# length 1인 튜플 만들기
animals = ("dog") # <-- 이건 tuple이 아니라 rmsid str로 인식된다.
print(animals, type(animals))

animals = ("dog",) # <-- length 1 (원소 1개)인 tuple 만들기, 뒤에 콤마를 꼭 찍어주자.
print(animals, type(animals))

# index 가능
animals = ("dog", "dog", "cat", "bird")
print(animals[0], animals[-1])

# slicing 가능
print(animals[1:3])
print(animals[::-1])

# tuple은 immutable하다! <-- 값을 변경할 수 없다.
# animals[0] = "puppy"
# animals.pop(0)

# animals.append("puppy") <-- 내용 변경하는 동작 없음

animals = animals + ("fish", "turtle")
print(animals)

animals = animals * 3
print(animals)

#-------------------------------------------------------------
# tuple은 언제 사용하나?
# 1. 변경되지 말아야 할 데이터들을 담을때
# 2. 복수의 값 '전달' 목적으로

# 그래서 tuple 은 list 와 달리 다음의 재미있는 성질이 있습니다

# 사각형을 나타내기 위해 가로(width), 세로(height) 값을 담는 경우
# 리스트의 경우에는
rec = [100, 200]
width = rec[0]
height = rec[1]

print()
print('width:', width)
print('height:', height)


# 반면 tuple의 경우
rec = (333, 500)
# width = rec[0]
# height = rec[1]
width, height = rec

print()
print('width:', width)
print('height:', height)

a, b, c = 10, 20, 30   # 여러개의 변수 초기화. 이 또한 tuple이었다.
print(a, b, c)

a, b, c = "ABC"
print(a, b, c)

#-----------------------------------------------------------------
print("\n count()")
myList = [10, 20, 30, 10, 10, 10, 20, 20]
print(myList.count(10))

myTuple = (10, 20, 30, 10, 10, 10, 20, 20)
print(myTuple.count(10))

myStr = "aaaabbaaaabbbabababaabab"
print(myStr.count("a"))