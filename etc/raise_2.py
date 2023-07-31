
#raise ValueError : 값이 틀릴 때 에러
class raise_2:
    def formethod(self):
        for i in range(1,6):
            if i==4:
                raise ValueError


ra=raise_2()
ra.formethod()