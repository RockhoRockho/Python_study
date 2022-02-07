# 여러개의 데이터를 담는 집합 데이터 타입들..
# 1. list   :  순서있다.  중복허용,  mutable
# 2. tuple  :  순서있다,  중복허용,  immutable
# 3. set : 순서없다,  중복허용안함    mutable
# 4. dict : key, value 쌍으로 구성, 순서없다.    mutable

# set
# 만드는 방법
# 1.set()  함수로 만들수도 있고
# 2. {  } 으로 만들수도 있다.

animals = {"dog", "dog", "cat", "bird"}
print(animals)
print(type(animals))
print(len(animals))

# index를 사용하지 못함 <- 순서가 없기 때문
# print(animals[0]) # not subscriptable

str1 = "aaaaabbbbbdddddaaaababadccccdd"
print(list(str1))
print(tuple(str1))
print(set(str1))    # set() 형변환 될때 중복된 데이터들은 제거됨.

animals = ["dog", "dog", "cat", "bird"]
# 위 list에서 중복된 데이터를 제거하고 싶다면?

print(list(set(animals)))

# 빈 set 만들기
a = []  # list
a = ()  # tuple
a = {}  # dict
a = set()   # set

print(a, type(a), len(a))

# 추가, 삭제
# add(), remove()

a.add('dog')
print(a)

a.add('cat')
print(a) # 출력된 형태를 보면 set가 순서를 유지하지 않음을 알 수 있다.

a.remove('cat')
print(a)

# a.remove('shark') 없는 데이터를 remove 하려하면 keyError
print(a)