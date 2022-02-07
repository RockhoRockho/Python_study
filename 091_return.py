# 기본적으로
# 함수가 실행이 종료되면 (마지막 문장 실행되면) 리턴합니다.

# return [값]
#  -- 함수 종료
#  -- 호출한 쪽으로 '값 하나' 을 돌려준다

def codeEveryday():
    print('파이썬 열공중')
    print('Life is short')
    print('You need Python')
    # ↑ 마지막 문장 실행하면 함수 종료하고 리턴
    return  # return을 명시하면 함수 종료하고 리턴


codeEveryday()  # 호출
print('종료')
print()


def codeEveryday():  # 동일이름의 함수 정의하면 이전 함수 정의는 사라짐(덮어쓰기)
    print('파이썬 열공중')
    print('Life is short')
    return  # 중간에 리턴하게 되면, 아래의 코드는 실행되지 않는다.
    print('You need Python')


codeEveryday()
print('종료')
print()

# 함수 정의 예
# 입력: 두개의 수를 입력 받아서
# 수행: 덧셈을 수행한뒤
# 리턴: 덧셈 결과를 리턴

print('-' * 20)


def add(a, b):
    result = a + b
    return result


add(10, 20)
result = add(10, 20)
print('r =', result)
print('r =', add(150, 40))  # add()의 리턴값을 print()
print('r =', add(10, add(10, 20)))

#                   add(10, 20)
#                       ↓   return
#               add(10, 30)
#                   ↓   return
#           print(..., 40)

def mul(a, b):
    print(f'mul 호출: a={a}, b={b}')
    return a * b


mul(10, 20)
mul(b=30, a=40)
# mul(a=15, 45) # '호출' 시 keyword argument 뒤에 positional argument 붙을수 없다
mul(7, b=50)

# positional argument : 호출시 값만 명시
# keyword argument : 호출시 이름=값 명시

# ----------------------------------------------------
# 파이썬에선 함수가 여러개의 값을 리턴할 수 있다?

# 결론적으로 말하자면 함수의 리턴 값은 오직 '하나' 다
# 그런데 파이썬에선 여러개의 값도 리턴이 가능했다!  어떻게 가능?  tuple 로 리턴하면 가능하다.
# 기술적으로는 tuple 하나 만 리턴했지만, tuple 안에 값이 여러개 있기 때문에
# 여러개의 값을 리턴한것과 같은 효과를 보는것이다

def sum_and_mul(a, b):
    return a + b, a * b

s, m = sum_and_mul(3, 4)
print(s, m)

result = sum_and_mul(3, 4)
print(result, type(result))

# 리턴값을 tuple로 하는 함수들도 많다.
print(divmod(10, 3))

















