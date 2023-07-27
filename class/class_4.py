class Fourcal:
    def setdata(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        result = self.a + self.b
        return result


fcal = Fourcal()
fcal.setdata(1, 2)
print(fcal.add())


# class Room1304 현재인원을 체크해서 출력하는데
# 인원이 2명 더 늘었다
# 인원이 1명 빠졌다
# 최종 인원 체크해서 출력하세요

class Room1304:




    def setdata2(self, current, new, gone):
        self.current = current
        self.new = new
        self.gone = gone
        print(f'현재 인원 :{current}명')

    def final(self, current, new, gone):
        result2 = current + new - gone
        print(f'최종 인원 :{result2}명')


r = Room1304()
r.setdata2(5, 2, 1)
r.final(5, 2, 1)
