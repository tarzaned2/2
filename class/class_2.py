# 반, 모임
class Calu:

    # 객체(instance) 인스턴스 생성할때 초기값
    # 메모리 상주

    # self: 해당하는 객체를 넘기겠다 Calu

    def __init__(self):
        self.result = 0
        self.result2 = 0

    def add(self, num):
        self.result = self.result + num
        return self.result

    # 큰데에서 작은데로
    # 대한민국.서울.강남구.서초4동.w건물.13층.1304

    # Calu() 객체생성

    #
    # caluob.add(1)
    # caluob.add(2)
    # caluob.add(3)
    # print(caluob.add(4))

    # 1부터 5까지 합을 구해서 출력 add2(self,num)

    def add2(self, i):
        for i in range(1, i+1):
            self.result2 += i
        return self.result2


caluob = Calu()

print(caluob.add2(5))
print(caluob.add2(30))
print(caluob.add2(4516))