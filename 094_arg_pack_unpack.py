# 파이썬에서 * 의 의미

# 1. 함수 정의할때 *  => 함수 호출시 argument packing

def hello(*args, **kwargs):
    print(args)  # tuple 로 packing 되어 받는다
    print(kwargs)  # dict 로 packing 되어 받는다

hello(10, 20, a=100, b=200)



# 2. 함수 호출할때 *

def print_val(kor, eng, math):
    print(kor, eng, math)
    print('총점=', kor + eng + math)
print_val(10, 20, 30)

score = [10, 20, 30]

# print_val(score) 에러
print_val(*score)
print_val(*(100, 200, 300))
print_val(*"abc")

student = {"name": "Sam", "email": "sam@mail.com", "nick": "Samuel"}
print_val(*student)

def print_dict(name, email, nick):
    print(f'이름:{name}, 이메일:{email}, 별명:{nick}')

# print_dict(student) # 당연히 에러
print_dict(*student) # dict를 *로 unpacking하면 key들의 tuple
print_dict(**student)

# * => arguments ( 순서만 있는 인자들; tuple )
# ** => keyword arguments ( 키값이 있는 인자들, dict )

# ------------------------------------------------------------
# 함수정의시 매개변수 첫번째에 * 를 명시하면
# 반드시 명시적으로 매개변수명을 사용하여 호출하든지
# dict 으로 패킹하여 호출해야 한다
def print_dict2(*, name, email):
    print(name, email)
# print_dict2("hong", "HHH@mail.com") # 에러
print_dict2(name='hong', email='HHH@mail.com')

dict2 = {"name": "hong", "email": "ddd@mail.com"}
print_dict2(**dict2)

# -----------------------------------------------------------
# [도전]
# log(10, 20, 30) 호출하면
# print(10, 20, 30) 으로 동작하게 하려면

def log(*args, **kwargs):
    print(*args, **kwargs)
log(10, 20, 30, sep='-')
log(100, 200, "안녕하세요")

