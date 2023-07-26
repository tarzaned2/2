# 변수: 명사 메소드: 동사
# python 오버로딩이 안된다
# 오버로딩 :같은 이름이 올수없다


def printf():
    print('printf() 메소드입니다')


printf()


# 인자 , aregument
def printinput(name):
    print(name)


def stringstr():
    return '현동윤'

def intvalue():
    return 10


printinput('아무개')
name=stringstr()
print(name)
print(intvalue())