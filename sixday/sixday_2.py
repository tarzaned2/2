name = '현동윤'

# f_string f'{변수}' 변수명 대입
# 지역변수 : 해당하는 문이 끝나면 (괄호) 소멸한다

# def name(name):
#     print(f'이름은 {name}입니다')
#
# name('현동윤')

i=0
result=0
for i in range(1, 11):
   #print(i)
    result=result+i

print(i)

# 매개변수 인자 지역변수 argument

def printsum(name):
    print(f'{name}입니다')

printsum('현동윤')
#
# 나이 메소드 출력

def age(age):
    print(f'나이는 {age}입니다')

age(22)

def address(address):
    print(f'사는곳은 {address}입니다')

address('논현동')

print('='*50)

def home(name,age,address):
    print(f'이름은 {name}입니다\n나이는 {age}입니다\n사는곳은 {address}입니다\n')

home('현동윤',22,'논현동')