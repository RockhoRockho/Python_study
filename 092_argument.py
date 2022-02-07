# 디폴트 매개변수 (Default Argument)
# 함수정의시 매개변수에 디폴트 값을 지정해 주면,  호출시 생략가능하다
# 생략된 상태에서 호출되면 디폴트 값으로 작동된다

# 디폴트 매개변수 작성 구문
#    def 함수명(매개변수명=디폴트값)

# 디폴트 매개변수 작성 구문
#   def 함수명(매개변수명=디폴트값)

def say_myself(name, old, gender='M'):
    print(f'제 이름은 {name} 입니다')
    print(f'나이는 {old} 입니다')

    (gender == 'M') and print('남자입니다')
    (gender == 'F') and print('여자입니다')
    print()

say_myself('고길동', 43, 'M')
say_myself('홍길동', 25) # gender 값을 명시 안해도 default값으로 동작
say_myself('임순옥', 32, 'F')

# 디폴트 매개변수 사용시 주의사항
# 디폴트 매개변수 사용하여 함수 정의시
# default argument  다음에 non-default  argument 정의 불가!!
# def say_myself(name, adult=True, age): # 에러
#     print(f'이름은 {name} 입니다')
#     print(f'나이는 {age} 입니다')
#     print('성인' if adult else '미성년자')

# 가변매개변수(various arguments) 함수 구문

# def 함수이름(*매개변수):
#     <수행할 문장>
#     ...

# 함수 호출시 전달된 복수개의 매개변수는 하나의 tuple 의 형태로 묶여서(packing) 다루어진다

def var_args(*args):
    print(type(args), ":", len(args), ":", args)

var_args(10)
var_args(10, 20, 30)
var_args()
var_args([10, 20], [30, 40], 44, (10,))

# 가변 매개변수도 어떠한 이름으로도 가능하긴 하나  관례적으로 args 를 많이 사용한다

def sum_many(*args):
    result = 0
    for num in args:
        result += num
    return result

print(sum_many(10, 20, 30))
print(sum_many(0.1, 10.4, 213.3435, -455.33))

# 다른 비가변 매개변수와 혼합 사용가능!
# 그러나..

def sum_mul(operation, *args):
    result = None
    if operation == 'sum':
        result = 0
        for i in args:
            result += i
    elif operation == 'mul':
        result = 1
        for i in args:
            result *= i

    return result

print(sum_mul("sum", 10, 20, 30))
print(sum_mul("mul", 10, 20, 30))

# 가변매개변수가 비가변매개변수보다 앞에 정의된 경우... (매우 비추)
def sum_mul(*args, operation):  # 함수 정의는 성공...
    result = None
    if operation == 'sum':
        result = 0
        for i in args:
            result += i
    elif operation == 'mul':
        result = 1
        for i in args:
            result *= i

    return result

# print(sum_mul(10, 20, 30, 'sum')) # 에러.. (10, 20, 30, 'sum') --> args로 packing됨
print(sum_mul(10, 20, 30, operation='sum'))

# 함수호출시 함수의 인수로 key = value 형태로 주어지면
# 함수에선 kwargs 가 dict 형태로 packing 하여 받아옴

def func(**kwargs):
    print(type(kwargs), len(kwargs), kwargs)

# func("john") # 에러
func(name='john', age=32)
func()

# *args, **kwargs 혼용가능.
def func(*args, **kwargs):
    print(args, end=" ")
    print(kwargs)

func(1, 2, 3, name='foo', age=4)

# func(1, 2, 3, name='foo', age = 4, 5, 6) # 에러
# ↑ 함수 호출시 keyword argument  다음에 positional argument  명시 불가

# 함수 정의할때도 키워드 인수 뒤에는 키워드 형태가 아닌 인수가 올 수 없다.
# def func(**kwargs, *args): # 에러
#       pass