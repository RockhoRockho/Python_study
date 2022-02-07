# 클래스의 상속 (inheritance)

# 기존의 만들어진 클래스를 상속받아 새로운 클래스 정의 가능

# 상속받아 만들어진 클래스는 기존의 클래스의 메소드, 객체변수 를 그대로 가지고 있다.
# 상속받은뒤, 새로운 객체변수, 메소드 추가 할수 있다.
# 상속받은뒤, 상속받은 메소드 재정의 가능 (오버라이딩)

# 상속의 장점:
#    기존의 코드를 다시 재작성 할 필요 없이. 새로이 변경 추가 되는 코드에만 집중할수 있기 때문에 생산성 향상

# 기존의 클래스 상속하여 새로운 클래스 정의하는 구문
#    class 새클래스명(기존의 클래스명)
#    class 새클래스명(기존클래스1, 기존클래스2, ...)  <-- 다중상속 허용

# 기존의 클래스를 '부모클래스(parent class)' 라고 하고  (혹은 super class,  base class ...)
# 상속받은 클래스를 '자식클래스(child class) 라고 한다  (혹은 sub class, derived class ...)


# 왜 상속이 필요한가?

class BasicTV:

    # 생성자, 인스턴스변수들.
    def __init__(self):
        self.power = False # 전원
        self.channel = 1 # 채널
        self.volume = 1 # 볼륨

    # 동작, 메소드들
    def display_info(self):
        print('전원:', self.power)
        print('채널:', self.channel)
        print('볼륨:', self.volume)

    def power_on_off(self):
        self.power = False if self.power else True
        print('전원이', self.power, '되었습니다')

    def volume_up(self):
        self.volume += 1
        print('볼륨 ->', self.volume)

    def volume_down(self):
        self.volume -= 1
        print('볼륨 ->', self.volume)

    def channel_up(self):
        self.channel += 1
        print('채널 ->', self.channel)

    def channel_down(self):
        self.channel -= 1
        print('채널 ->', self.channel)

tv1 = BasicTV()
tv1.display_info()
tv1.power_on_off()
tv1.volume_up()
tv1.volume_up()
tv1.channel_up()
tv1.channel_up()
tv1.channel_up()
tv1.display_info()

print()
tv2 = BasicTV()
tv2.power_on_off()
tv2.channel_up()
tv2.channel_down()
tv2.volume_up()
tv2.display_info()

#-------------------------------------

class SmartTV:

    def __init__(self):
        self.power = False
        self.channel = 1
        self.volume = 1
        self.ip = '192.168.0.1'  # IP (추가된 속성)

    def display_info(self):
        print('전원:', self.power)
        print('채널:', self.channel)
        print('볼륨:', self.volume)
        print('IP:', self.ip)

    def power_on_off(self):
        self.power = False if self.power else True
        print('전원이', self.power, '되었습니다')

    def volume_up(self):
        self.volume += 1
        print('볼륨 ->', self.volume)

    def volume_down(self):
        self.volume -= 1
        print('볼륨 ->', self.volume)

    def channel_up(self):
        self.channel += 1
        print('채널 ->', self.channel)

    def channel_down(self):
        self.channel -= 1
        print('채널 ->', self.channel)

    def set_ip(self, ip):  # 새로 추가된 동작
        self.ip = ip
        print('ip ->', self.ip)

print('-' * 20)

tv3 = SmartTV()
tv3.display_info()
tv3.power_on_off()
tv3.power_on_off()
tv3.volume_up()
tv3.channel_up()
tv3.set_ip('100.200.100.200')
tv3.display_info()

# 고찰: 새로운 클래스 생성하는데 기존에 만들었던 코드를 재작성 해야 한다?!?
#  --> 생산성 문제 !

# -------------------------------------------------------------------
# 상속을 사용한 SmartTV 정의
print('-' * 20)

class SmartTV(BasicTV):
    def __init__(self):
        super().__init__()  # 부모(super()) 의 생성자 먼저 호출
        self.ip = '192.168.0.1' # 새로 추가되는 것만 정의

    def display_info(self):
        super().display_info()  # 부모(super()) 의 display_info() 먼저 호출
        print('ip:', self.ip)   # 추가되는 기능만 추가

    def set_ip(self, ip):   # 새로 추가된 동작
        self.ip = ip
        print('ip ->', self.ip)

tv4 = SmartTV()
tv4.display_info()
tv4.power_on_off()
tv4.volume_down()
tv4.set_ip('123.123.123.123')
tv4.display_info()

# f: field, m: method























