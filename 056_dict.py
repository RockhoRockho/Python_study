# 여러개의 데이터를 담는 집합 데이터 타입들..
# 1. list   :  순서있다.  중복허용,  mutable
# 2. tuple  :  순서있다,  중복허용,  immutable
# 3. set : 순서없다,  중복허용안함    mutable
# 4. dict : key, value 쌍으로 구성, 순서없다.    mutable

# dict : 딕셔너리

# dictionary 데이터 타입은  key-value 쌍으로 저장되는 데이터 집합이다.

# {Key1:Value1, Key2:Value2, Key3:Value3 ...}
# "이름" = "홍길동", "생일" = "몇 월 몇 일"   과 같은 자료형 담음

# 기존의 list, tuple 등은 value 중심
# 그러나 이 또한 알고 보면 key-value 쌍으로 구성

# 순서는 고정이 안된다
# key 는 중복 안된다.

student = {
    "name" : "최현진",
    "email" : "choi@mail.com",
}
print(type(student))
print(student)
print(len(student))

# value 읽기
print(student["name"])  # 방법1
print(student.get("name"))  # 방법2

# 위 두 방법의 차이점 : 존재하지 않는 key에 접근하는 경우
# print(student['age']) # KeyError
print(student.get("age")) # None

# get()  을 사용하면 예외적인 상황에서도
# 동작 가능하게 처리 가능
# student.get(key, default) : key 값이 없으면 default 값으로 리턴

print(student.get('age', 20)) # 'age' 키가 없으면 20을 리턴하도록 처리

# 수정하기
student['name'] = '이민규'
print(student)

# 추가하기
student['address'] = '논현동' # 기존에 없던 key-value쌍을 입력하면 추가된다.
print(student)

# 삭제하기
del(student['email'])
print(student)

# dict.update()
# 해당 key 값 수정
student.update({"name" : "김만두"})
print(student)
student.update({'age' : 13})
print(student)

# dict의 key, value의 타입
# value는 어떠한 타입이라도 가능!
# key는 hash 가능한 타입만 가능 (ex: int, float, str, bool..)

dict1 = {
    1: "haha",
    2: "hoho",
    2: "hehe", # key 중복 불가
    "one": 3.14,
    # ["one"]: 3.14, # TypeError, unhashable type: 'list
    "two": {
        3.14: "pi",
        "pi": 3.14,
    },
    False: [10, 20, 30]
}

print(dict1)
print(dict1[1])
# dict1의 type ? => dict
# dict1[1] ==> str
print(dict1['two'])
print(dict1['two'][3.14])
print(dict1['two']['pi'])
print(dict1[False])
print(dict1[False][1])

# dict 의 keys(), values()
student = {
    "name": "김동훈",
    "email": "dongdong@mail.com",
    "age": 23,
    "addr": "서울",
}

print(student.keys())  # key 들로만 구성된 iterable 객체 리턴됨.
print(student.values()) # value 들로만 구성된 iterable 객체 리턴됨.

print(set(student.keys()))
print(set(student))  # dict 자체도 iterable 하다

print(list(student.values()))

# dict 와 in 연산자
#  key 가 존재하는지 여부
print("name" in student)
print("place" in student)

#------------------------------------------
# 비어있는 데이터
a = []  # list
a = ""  # str
a = ()  # tuple
a = {}  # dict


a_dict = {"b": 5, "c": 3, "a": 2}

# key 로 정렬
dict_items = a_dict.items()  # (key, value) 쌍으로 이루어진 iterable 객체를 리턴
print(dict_items)
sorted_items = sorted(dict_items)  # key 기준으로 정렬
print(sorted_items)

# value로 정렬
sorted_items = sorted(dict_items, key=lambda x:x[1]) # key 기준으로 정렬
print(sorted_items)

sorted_items = sorted(dict_items, key=lambda x:x[1], reverse=True   ) # key 기준으로 정렬
print(sorted_items)
