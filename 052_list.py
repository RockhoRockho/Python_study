animals = ["dog", "dog", "cat", "bird"]
colors = ["white", "blue", "red"]

# 1차월 리스트 : index 하나만 사용하여 원소에 접근하는 리스트
print(colors[0], colors[1])

# 리스트의 원소는 '어떠한 타입'도 가능
myList = [100, 200, "john", 0.29, False, None]
print(myList)

# 다차원 리스트
# 리스트의 원소가 리스트

data = [[1, 2, 3], [10, 20, 30], [40, 50, 60]]
print(len(data))
print(data[0])
print(data[1])
print(data[2])

print(data[0][1]) # 2차원 리스트에서 원소 접근하기 위해 index 2개 사용
print(data[2][1])

# data -> 2차원 list
# data[0] -> 1차원 list
# data[0][0] -> 0차원, scalar 값

# ★ 인덱싱을 한다는 것은 차원 축소 발생!
# n차원 리스트의 원소는 n-1 차원 리스트

# 다차원 리스트에선
# 각각의 원소들의 length는 제 각각 다를 수 있다.
animals = [
    ['dog', 'cat', 'tiger', 'bear', 'wolf'],
    ['sparrow', 'eagle'],
    ['salmon', 'tuna', 'shark']
]

print(len(animals[0]))
print(len(animals[1]))
print(len(animals[2]))

# 다차원 배열에선 아래와 같이 slicing 가능
data = [
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [11, 22, 33, 44, 55]
]
print(data[1][3])
print(data[1][:3])

print(data[0:2])

print(data[::2])

print('-' * 20)
#---------------------------------------------------
# list 중간에 데이터(들) 삽입하기
# 1. slice 사용

# 2. insert() 사용
animals = ['dog', 'dog', 'cat', 'bird']
# cat의 위치에 ["shark", "fish"] 추가하려면
# ['dog', 'dog', 'shark', 'fish', 'bird']
animals[2] = ['shark', 'fish']
print(animals)

animals = ['dog', 'dog', 'cat', 'bird']
# slicing 결과에 대입 가능!!?
animals[2:3] = ['shark', 'fish'] # 'cat' 위치에 'shark', 'fish' 삽입
print(animals)

animals = ['dog', 'dog', 'cat', 'bird']
animals[2:4] = ['shark', 'fish']
print(animals)

animals = ['dog', 'dog', 'cat', 'bird']
animals[2:2] = ['shark', 'fish']
print(animals)

# 2. .insert()  사용
fruits = ['Apple', 'Bananas', 'Orange']
fruits.insert(0, "Lemon")
print(fruits)

#------------------------------------------------------
# .index(value) : 값으로 인덱스 찾기
# list안에 특정 value가 있나?

print(animals.index("cat"))
print(animals.index("dog")) # 가장 먼저 발견한 인덱스
# print(animals.index('tiger')) # 없는 값은 ValueError

# .remove(value) : 특정 값을 리스트에서 삭제
animals.remove('dog') # 첫번째 원소만 삭제
print(animals)
# animals.remove('whale')  # 없는값 제거하려 하면 에러

# ※ del() 는 index, slice  를 사용했다

#---------------------------------------------
# pop()
# 리스트 안의 원소 꺼내기 (리스트에선 제거됨)
# (디폴트) 맨 뒤의 원소를 꺼낸다
animals = ['dog', 'shark', 'cat', 'bird']
print(animals)
print('pop() 결과', animals.pop())
print('pop() 이후', animals)

# 리스트의 중간 원소를 pop 할 수 있다.
print(animals.pop(1))
print(animals)

#------------------------------------------
print('-' * 20)
# .sort()
# 오름차순 정렬
animals = ['dog', 'shark', 'cat', 'bird']
print('sort() 전', animals)
animals.sort()
print('sort() 후', animals)

# 역정렬 (내림차순)
animals.sort(reverse=True)
print(animals)

#------------------------------------------------------------
print('-' * 20)
animals = ['dog', 'shark', 'cat', 'bird']
print(animals)
print(animals[::-1]) # 원본 변화 X
animals.reverse() # 원본 변화 발생!
print(animals)

print('-' * 20)
#--------------------------------------------------------------
# sorted() 함수
# sorted(iterable, key=key, reverse=reverse)
#    iterable : sort 대상 (list, dict, tuple 등..)
#   key : 대소비교를 하는 함수 (디폴트 None)
#   reverse : False 오름차순 (디폴트), True 내림차순

# 리턴값 : 정렬된 list
a = ["b", "g", "a", "d", "f", "c", "h", "e"]
x = sorted(a)
print(x)
print(a)

# list와 in 연산자
# data in iterable
animals = ['dog', 'dog', 'cat', 'bird']

print('dog' in animals) # animals라는 list 안에 "dog"가 존재하나? => True / False
print('shark' in animals)