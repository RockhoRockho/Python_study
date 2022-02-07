# 예외 (Exception), 오류 (Error)

# kk = 10 20 # <-- 에시당초 문법적인 구문 오류 SyntaxError

# 반면에, '실행중'에 발생할 수 있는 논리적인 오류들도 있다.
# 이러한 것들을 '예외'라고 한다.

# 일단 예외가 발생하면, 기본적으로 프로그램은 예외에 대한 에러 메세지를 내고
# 강제 종료 된다.

# 신뢰성(reliable) 하고 견고한(robust) 함 프로그래밍을 작성하려면
# 이러한 에러들을 잘 처리 해야 한다

# https://docs.python.org/3/tutorial/errors.html

# 다양한 예외 상황들

def func_sum(data):
    result = 0
    for i in data:
        result = result + i
    return result

data = [10, 20, 30]
result = func_sum(data)
print('result =', result)

data = {'name': 'John', 'age': 20}
# func_sum(data) # 예외 (에러) 발생
data = ['10', '20', '30']
# func_sum(data) # 예외 (에러) 발생

# 존재하지 않는 파일에 대한 오류 FileNotFoundError
# f = open('없는파일.txt', 'r')

a = 10
b = 0
print(a + b)
# print(a / b) ZeroDivisionError

# --------------------------------------------------
# 에러를 피하기 위해 조건문 사용은 가능하나...

a = 10
b = 0
if b != 0:
    print(a / b)
else:
    print('0 으로 나눌 수 없습니다')

# 수많은 예외상황을 매번 if조건문으로 처리하면
# 코드가 매우 난잡해진다. --> 유지보수 힘들어짐.

# 그래서 예외처리 관련하여
# '코드수행블럭'과 '예외처리블럭'을 구분하여 예외를 다루는게 바람직.

# 파이썬 에서는
# try ~ except 문으로 오류를 다룹니다

# 구문]
# try:
#     코드수행블럭
#     ...
# except [발생 오류[as 오류 메시지 변수]]:
#     예외처리블럭
#     ...

#  try 블록 수행 중 오류가 발생하면 except 블록이 수행된다.
# 하지만 try블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

# 1. try: ~ except:
print('-' * 20)
num = 2
try:
    result = 4 / num
    print('1.결과는', result)
except:
    print('2.오류발생')

print('3.프로그램 종료')

# 2. try: ~ except:
print('-' * 20)
num = "0"
try:
    result = 4 / num
    print('1.결과는', result)
except ZeroDivisionError:
# 위 try: 블럭 안에서 ZeroDivisionError가 발생하면 아래 수행
    print('2-1. ZeroDivisionError 오류발생')
except TypeError:
    print('2-2. TypeError 오류발생')

print('3.프로그램 종료')


# 3. try: ~ except 오류 as 변수:
print('-' * 20)
num = 0
try:
    result = 4 / num
    print('1.결과는', result)
except ZeroDivisionError as e:
    print('2.ZeroDivisionError 오류발생')
    print(e.args)
    print(e)

print('3.프로그램 종료')

# 4. try: ~ else:
# try문은 else절을 지원한다.
# else절은 예외가 발생하지 않은 경우에 실행되며
# 반드시 except절 바로 다음에 위치해야 한다.
# 그닥 비추, 차라리 걍 try 블럭 안에 넣자

try:
    f = open('새파일.txt', 'r')
    print('1. 파일을 열었습니다')
except FileNotFoundError as e:
    print('2.', e)
else:
    # try: 에서 예외 발생하지 않으면 수행
    data = f.read()
    print('3. else: 수행\n', data)
    f.close()

print('4. 프로그램 종료')


# 5. try: ~ finally:
#  예외가 발생했든 안했든 반드시 수행해야 하는 코드들을 finally: 에 작성

print('-' * 20)

print('1. 프로그램 시작')

try:
    print('2. try: 시작')
    f = open('foo.txt', 'w')
    a = 10
    # a = a + bbbb # NameError 발생
    print('3. try: 종료')
except NameError as e:
    print('4. except: 수행')
    print(e.args)
finally:
    print('5. finally: 수행')
    f.close()

print('6.프로그램 종료')

print('-' * 20)

# 주의 사항
# try: except: else: finally: 블럭등에 걸쳐
# 사용할 변수는
# try: 블럭 이전에 선언하고 초깃값 주고 사용하는 것을 추천
del(f)
f = None
try:
    f = open('없는파일.txt', 'r')
    print('1. try: 종료')
except FileNotFoundError as e:
    print(e)
finally:
    print('2. finally: 시작')
    # f.close()  # 이 시점에서는 f는 모르는 변수다
    f and f.close()
    print('3. finally: 종료')

print('4. 프로그램 종료')

# ------------------------------------------

# 6. 여러개의 오류 처리하기

# try:
#     ...
# except 발생 오류1:
#    ... 
# except 발생 오류2:
#    ...

# 방법2
# try:
#     ...
# except (발생 오류1, 발생오류 2 ..):
#    ... 

try:
    print('1. try: 시작')
    a = [1, 2]
    print(a[3])
    b = 4 / 0
    print('2. try: 종료')
except ZeroDivisionError as e:
    print('3-1', e)
except IndexError as e:
    print('3-2', e)

print('4. 프로그램 종료')

print('-' * 20)

try:
    print('1. try: 시작')
    a = [1, 2]
    print(a[1])
    b = 4 / 0
    print('2. try: 종료')
except (ZeroDivisionError, IndexError) as e:
    print('3', e)

print('4. 프로그램 종료')

# ---------------------------------------------------
# 7. 오류 회피
# 프로그래밍을 하다 보면 특정 오류(에러, 예외)가 발생할 경우 
# 그냥 통과시켜야 할 때가 있을 수 있다. 다음의 예를 보자
print('-' * 20)
try:
    f = open('없는 파일', 'r')
except Exception: # 어떠한 에러도 처리
    pass

print('프로그램은 계속된다.')

# Exception : 모든종류의 예외처리