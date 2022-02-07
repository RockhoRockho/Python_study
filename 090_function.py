print('안녕하세요')
print('제 이름은 이정수 입니다')

print('안녕하세요')
print('제 이름은 김혜원 입니다')

print('안녕하세요')
print('제 이름은 이창준 입니다')

print('안녕하세요')
print('제 이름은 강재원 입니다')


# 반복되는 코드들이 보인다.

# ※ "코드가 너무 DRY 해요"
#    Don't Repeat Yourself

# 함수 (Function)
# 프로그래밍에서 동일한(혹은 거의 비슷한) 내용의 코드가 반복될때가 있다.
# 바로 이러한 코드 낭비를 없애기 위해
# 반복되는 코드를 묶어서 하나의 함수로 '정의'해 놓고 '사용'하는 것이다

# 즉, 반복되는 부분이 있을 경우 "반복적으로 사용되는 가치 있는 부분"을
# 한 뭉치로 묶어서
# "1. 어떤 입력값을 주었을 때,
#  2. 어떠한 일을 수행하고,
#  3. 어떤 결과값을 돌려준다" 라는식의
# 함수로 작성하는 것이 현명하다.

# -------------------------------------------------------------

# 함수 만들기 (함수 정의 : Function Definition)

# def 키워드로 작성

# def 함수이름( 매개변수 들):
#     함수 본체 <수행할 문장1>
#     함수 본체 <수행할 문장2>
#     ...

# 함수의 동작 정의
#   입력(매개변수) -> 본체 수행 -> 결과(리턴)

# 함수이름은 변수 이름 작성과 거의 동일한 규칙

# ----------------------------------------------------------
# 함수 호출 (함수 사용 )  Function call, invoke
# 함수호출시 넘겨지는 인자(parameter) 값들은
# 함수의 매개변수(argument)들이 받습니다.
# 매개변수는 0개, 한개, 여러개 있을수 있을수 있습니다

# 함수에는 리턴값이 있다.
# 리턴값은 함수를 호출(call) 한쪽에 돌려준다
# return 키워드로 리턴값을
# 함수 본체 수행중 return 을 만나면 함수를 종료 하게 됩니다
# 어떠한 타입도 리턴할수 있다.
# 리턴값은 없을수도 있다. None 리턴

# -----------------------------------------------------
# 함수 정의
# 함수 이름 : sayAnthem

def sayAnthem():
    print('동해물과 백두산이')
    print('마르고 닳도록')
    print('하느님이 보우하사')
    print('우리나라 만세')


# 함수 호출
sayAnthem()
sayAnthem()
sayAnthem()
sayAnthem()
sayAnthem()


# 함수 정의
# 매개변수 지정
def sayName(name):
    print('안녕하세요')
    print('제 이름은', name, '입니다')


sayName('김도희')
sayName('김혜원')

# 매개변수 지정된 함수는 호출시
# 반드시 매개변수에 넘겨줄 값 (인자값)이 있어야 한다

# sayName()  #
# TypeError: sayName() missing 1 required positional argument: 'name'
print('-' * 20)


def sayAge(age):
    print('제 나이는요...')
    print(age, '살 입니다')


sayAge(100)
sayAge(23)
sayAge(77)


# 함수가 다른 함수 호출 할 수 있다.
def sayHello(name, age):
    print('--' * 10)
    sayName(name)
    sayAge(age)
    print('--' * 10)


sayHello('맹주빈', 24)
sayHello('장서희', 26)
sayHello('이현승', 18)

# 함수 호출 관련 디버깅 명령
# step into : 실행할 함수 내부로 이동
# step out : 실행중인 함수 리턴까지 진행
# 호출스택 (call stack) : 함수 호출관계 모니터링

# sayHello('김현채') # 에러
sayHello(100, '토르')  # 매개변수의 순서대로 전달된다.

# 함수 호출시 매개변수 명시 가능!
sayHello(age=100, name='토르')
