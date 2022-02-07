"""
Function annotation 이란?

 Python 의 장점 : 문법의 제약성이 적다. → 높은 유연성
 Python 의 단점 : 위 장점이 반대로 단점이 된다.
     변수나 함수 사용시 자료형에 대한 선언없이  자유롭게 사용
     작성된 코드를 볼때 명시적으로 해석이 어렵다.

 annotation 은 이러한 불편한 점을 조금이나마 덜기 위해 나온 기능이다.

    Python3>= 이상에서 사용가능
"""

"""
Fuctnion annotation  구문
   def func(arg1: str, arg2: 1+2, arg3: 'this is annotation') -> bool

   parameter 에  :expressoin 형태로 매개변수마다 annotation 을 쓸수 있다.
   annotation 에는 arg1 처럼 매개변수의 type 을 써놓을 수도 있고,

   arg2 의 annotation 처럼 덧셈과 같은 간단한 연산 표현도 작성 가능하며, 

   arg3 처럼 string 형태로도 작성 가능하다. 

   또한, function 의 return 값에 대해서는 -> expression 형태로 사용한다. 

   return 또한 매개변수와 사용 방법은 동일하다.

"""

def func(arg1: str, arg2: 1 + 2, arg3: 'this is annotation') -> bool:
    print(f'arg1 = {arg1}')
    print(f'arg2 = {arg2}')
    print(f'arg3 = {arg3}')

    return True

result = func('test1', 3, 'this is test')
print(f'result = {result}')

# 함수정의에 작성된 annotation과 무관한 인자를 넣어 호출하면????
result = func('test1', 'test2', 'test3')
print(f'result = {result}')
# annotation에 적혀 있는 내용은 주석이므로 실제로는 이와 상관없이 실행되게 된다.

print(func)
print(func.__annotations__)

"""
 function comment
 function 을 작성할때 아래와 같이 주석(comment)를 달아 
 개발자간 커뮤니케이션에 쓰이긴 하지만 이것 또한 지속적으로 작성하기 쉽지 않은게 현실이다. (귀찮...)

"""

def func(arg1, arg2, arg3):
    '''

    :param arg1: str
    :param arg2: str
    :param arg3: list
    :return: bool
    함수 설명 어쩌구 저쩌구
    '''
    pass

# function annotation 자체가 문법적인 강제성을 가진것은 아니나.
# 파이썬 코드의 명확성을 표현하는데 도움이 되며 (가독성)
# IDE (ex: Pycharm, VSC ..) 와 함께 사용되면 도움기능들을 기대할 수 있다.










