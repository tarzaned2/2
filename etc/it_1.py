# iter 이터레이터 type
# 해당하는데이터를 이터레이터로 바꾸면
# next 로 접근할수있다

class it_1:
    def __init__(self, name):
        self.name = name

    def itprint(self):
        a = 'abc'
        ait = iter(a)

        init = 1
        while init <= len(a):
            print(next(ait))
            init = init + 1

    def namemethod(self):
        itname = iter(self.name)

        init = 1
        while init <= len(self.name):
            print(next(itname))
            init = init + 1


it = it_1('현동윤')
it.namemethod()

# 메소드 만들어서 본인이름 출력
