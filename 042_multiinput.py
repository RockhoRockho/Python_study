# input() 으로는 한번에 여러개 입력 못받는다
# a, b, c = input('3개를 입려하세요')


# 여러개 한번에 입력받기

# 방법1: input().split() -- 공백으로 구분하여 여러개 입력
# a, b, c = input("3개를 입력하세요: ").split()
# print(f'a={a} b={b} c={c}')

# input() => "10 30 50" => split() => "10", "20", "30"

# hour, minute, second = input("시:분:초 입력 ").split(":")  # input() 값(str) 을 ":" 기준으로 쪼갬
# print(f'{hour}시 {minute}분 {second}초')

# 초 로 환산
# print(hour * 3600 + minute * 60 + second)

# hour = int(hour)
# minute = int(minute)
# second = int(second)
#
# print(hour * 3600 + minute * 60 + second)

# 방법2: 입력한 str(들)을 한번에 변환하기. map() 함수

# 변수1, 변수2, ... = map(타입, input().split())

# a, b, c = input('3개의 정수 입력: ').split()
#
# print(a, b, c)
# print(a + b + c)

# input() => "10 20 30"
# split() => "10" "20" "30"
# map() =>  ↓     ↓     ↓
#         int() int() int()
#           ↓     ↓     ↓
#          10    20    30


# 연습
# 키(cm) 와 몸무게(kg) 를 입력받아 bmi 를 계산하여 출력
# bmi = 몸무게(kg) /  (키(m) x 키(m))
# bmi는 소숫점 한자리까지 출력

# 실행 예)
# 키(cm) 와 몸무게(kg) 를 입력하세요: 183 93
# BMI 는 27.8 입니다

height, weight = map(float, input('키(cm) 와 몸무게(kg) 를 입력하세요: ').split())
bmi = weight / ((height/100)**2)
print('BMI 는 {:.1f} 입니다'.format(bmi))

















