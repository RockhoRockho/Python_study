#----------------------------------
# 문자열 타입 : str (string)
# 문자열 리터럴 만드는 방법
# 1. 쌍따옴표 (double quotation)
# 2. 홀따옴표 (single quotation)
# 3. 쌍따옴표3개
# 4. 홀따옴표3개

print("Python is fun")
print('Python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')

# she's gone <-- 출력하려면?

# print('She's gone')
print("She's gone")

# He says "It's OK!"
print('''He says "It's OK!"''')

# 문자열 연산 +
print("Hello" + 'Python') # 문자열 연결 연산
print("Hello" + " " + "Anaconda")
# print(12 + "monkeys") # ★ 절대로 문자 + 숫자 연산 불가!

# 문자열 *
print("-" * 20)

# len(str) 함수
# 문자열 안의 문자 개수
print(len("파이썬")) # 영어 한글 구분없이 글자수 계산 잘 해줌.
print(len('hello python'))

# 자동덥함 . 인접해 있으면 그냥 자동으로 붙는다
print("Hello" "Python")