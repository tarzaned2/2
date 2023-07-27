class Calu2:
    def __init__(self):
        # 전역변수
        self.result = 0
        self.result2 = 0

    def add(self, num):
        self.result = self.result + num

    def sub(self, num1, num2):
        self.result2 = num1 - num2

    def printtotal(self):
        print(self.result)

    def printtotal2(self):
        print(self.result2)


# 객체생성
cal = Calu2()
cal.add(10)
cal.add(20)
cal.printtotal()
cal.sub(4400, 1500)
cal.printtotal2()
