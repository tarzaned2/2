# 메소드 오버로딩
# 오버로딩: 메소드이름이 이름을 다른 메소드명으로 쓸수없다

def name(*home):
    print(home)


def home2(*home):
    return home


def home3(name, *home):
    print(f'이름은 {name} 나머지는 {home}입니다')


name('현동윤', 22, '논현동')
print(home2('한재현', 22, '노들역'))

home3('현동윤', 22, '논현동')


# 이름 나이 주소 일반변수 *email phone

def home4(name, age, address, *etc):
    print(f'이름은 {name} 나이는 {age} 주소는 {address} 나머지는 {etc}입니다')


home4('현동윤', 22, '논현동', 'dyoon0830@naver.com', '01041249859')

#python 마우스 제어 ->게임 오토사냥
#주식 실시간 데이터


