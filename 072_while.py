# 중첩 순환문 (nested loop)
# 조건문 안에 조건문 블럭이 들어갈수 있듯이
# 순환문 안에도 얼마든지 순환문이 포함될수 있다..
# 조건문과 순환문 의 어떠한 조합도 가능하다


# 구구단 출력 : 2단 ~ 9단
# 중첩된 for 문

'''
2 x 1 = 2
2 x 2 = 4
...
2 x 9 = 18
3 x 1 = 3
...
4 x 1 = 4
…
...
9 x 9 = 81
'''

dan = 2
while dan <= 9: # 2단 ~ 9단
    print(f'{dan}단')
    mul = 1
    while mul <= 9:
        print(dan, 'x', mul, '=', dan * mul)
        mul += 1

    print()
    dan += 1