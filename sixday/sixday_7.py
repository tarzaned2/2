def home(**args):
    print(args)


home(name='현동윤',age=22,address='논현동')


# 1~5
#1.2 3 4 5일반변수 메소드로 출력

#1,2  *3 4 5 일반변수 메소드로 출력
#일반변수 1,2,3 키:4:4  키 5:5  나이 주소 일반변수 메소드로 출력->합을구해서출력#


a=[1,2,3,4,5]
def num(num):
    print(num)
    for i in a:
        result=0
        result=result+i
        print(result)

num(5)

def num2(num,num2,*num3):
    print(f'{num},{num2},{num3}')
    for i in a:
        for i in a:
            result = 0
            result = result + i
            print(result)


