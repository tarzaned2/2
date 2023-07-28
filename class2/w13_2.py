class Ezen100:
    def __init__(self,rnumber,total,gone,now):
        self.rnumber=rnumber
        self.total=total
        self.gone=gone
        self.now=now

    def ezenprint(self):
        print(f'방:{self.rnumber}')
        print(f'총인원:{self.total}')
        print(f'빠진인원:{self.gone}')
        print(f'현재인원:{self.now}')



for i in range(1,101):


    b=int(input('총 인원:'))
    c=int(input('빠진 인원:'))

    eze=Ezen100(1300+i,b,c,b-c)

    eze.ezenprint()
    print('='*50)




