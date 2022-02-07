# 클래스메소드 vs. 인스턴스 메소드
# class method     instance method

class Foo:

    # 클래스 메소드 (class method)
    # self 가 안붙은 메소드. '클래스이름'. ~ 으로 사용
    def func1():
        print('function1')

    # 인스턴스 메소드 (instance method)
    # self가 붙은 메소드. '인스턴스 생성'하여 사용
    def func2(self):
        print('function2')


f1 = Foo()
# f1.func1()  # 클래스메소드는 클래스이름으로 사용해야 한다.
#   -> Foo.func1(f1)
Foo.func1()

f1.func2()  # 인스턴스 메소드는 인스턴스로 사용


# 클래스변수 vs. 인스턴스 변수
# class variable vs. instance variable

# self.변수이름  : <-- 인스턴스 변수
#       인스턴스 변수는 '인스턴스 마다' 생성  --> 인스턴스 네임스페이스에 생성

# 클래스 내부에서 선언된변수 <-- 클래스 변수  (self 가 안 붙음)
#        사용하려면 클래스이름.변수이름  으로 사용해야 함
#        클래스 변수는 '클래스에 딱 하나' 생성 --> 클래스 네임스페이스에 생성

# ★ 어떤 경우에 클래스변수 혹은 인스턴스 변수로 설계하나??

class Account:
    num_accounts = 0  # ★ 클래스 변수

    # 생성자(constructor)
    def __init__(self, name):
        print(f'Account({name}) 생성')
        self.name = name  # ★ 인스턴스 변수
        Account.num_accounts += 1

    # 소멸자(destructor) : 인스턴스가 소멸될때 자동으로 호출
    def __del__(self):
        print(f'Account({self.name}) 소멸')
        Account.num_accounts -= 1


print()
print(Account.num_accounts)
acc1 = Account('회사')
# ▼ 인스턴스 이름으로도 클래스 변수 접근은 가능하나
# 매우 비추
print(Account.num_accounts, acc1.num_accounts)

acc2 = Account('개인')

print(Account.num_accounts)

# 네임스페이스

# Account (class)
#   └  {'num_account': 2}

# acc1 (instance)
#   └  {'name': '회사'}

# acc2 (instance)
#   └  {'name': '개인'}

del (acc1)  # 회사계좌 삭제
print(Account.num_accounts)  # ??


# -------------------------------------------------------------
# 생각해보기

class Foo:
    num_instance = 0

    def __init__(self):
        self.num_instance += 1


obj1 = Foo()
print()
print(obj1.num_instance)
print(Foo.num_instance)

#  self.num_instance += 1

# self.num_instance = self.num_instance + 1   <-- 연산 과정 고려,  그리고 네임스페이스 로 고려해보자

print(Foo.__dict__)
print(obj1.__dict__)


# 클래스 변수는 클래스변수 답게 사용하자
# 인스턴스 변수는 인스턴스 변수 답게 사용하자
# 안그러면 위와 같은 실수 종종 발생합니다.


# ------------------------------------------------------------------
# 연습 : PartTimer 설계

# '매 직원(PartTimer)'에 공통적으로 적용되는 자료
# - 시급
# - 전체 직원수

# 각 직원별 객체 생성시 직원별로 '별칭'과 '근무지' '급여총액' 초기화 (속성)
#   '근무지' 생략시 '113동' 으로 지정
#   직원별로 '급여총액'  0으로 초기화

# 직원의 급여 계산하기(동작)
#    '몇시간 근무',  '+상여금'  에 따른 직원급여 계산
#   '상여금' 은 지정안하면 0 으로 처리


# 예]
# park = PartTimer('라이언')   // park 은 ‘라이언’ 이라는 닉네임의 직원으로 등록

# park 이 4시간 일한 급여 총액은?  → 34400
# park 이 2시간 일한 급여 총액은? → 17200
# park 이 2시간 일한 급여 + 상여급 2000 총액은? → 19200

class PartTimer:
    hour_rate = 9160  # 시급
    total_part_timers = 0  # 전체 직원수

    def __init__(self, nickname, workplace='113동'):
        PartTimer.total_part_timers += 1
        # 인스터스 변수들
        self.nickname = nickname
        self.workplace = workplace
        self.total_wage = 0 # 급여총액

    # 급여 계산하기
    def calculate_wage(self, hour, bonus=0): # 시간 상여금
        self.total_wage = PartTimer.hour_rate * hour + bonus
        return self.total_wage

print('-' * 20)
park = PartTimer('라이언')
lee = PartTimer('네오', '127-1동')
print(park.total_wage, lee.total_wage)

print(park.__dict__)
print(lee.__dict__)

print('급여', park.calculate_wage(4))
print('급여', park.calculate_wage(2))

print('직원수', PartTimer.total_part_timers)

print('급여', lee.calculate_wage(3, 15000))



print('프로그램 종료')