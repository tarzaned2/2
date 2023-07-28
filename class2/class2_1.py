class Room1304:

    # 객체가 생성되면 해당하는 객체가 init로 들어온다
    # 생성자 (constructor) init는 생성자이면서 메소드

    # self : Room1304
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print(self.name)
        print(self.age)
        print(self.address)

    def home(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

        print(self.name)
        print(self.age)
        print(self.address)


# 인자 없는 생성자 (기본 생성자)
# r1304 = Room1304()
# r1304.home('현동윤', 22, '논현동')

# 인자 있는 생성자
# 인자 있는 생성자가 오면 기본 생성자를 못 쓴다
# r1304_2 = Room1304('한재현', 22, '스페인')
# print('='*50)
# r1304_3 = Room1304('나이팅게일', 29, '이탈리아')

