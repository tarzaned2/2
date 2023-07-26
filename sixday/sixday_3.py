# static 변수 전역변수
name = '현동윤'
age = 22
address = '논현동'


def name():
    # 지역변수
    name = '현동윤'
    return name


def age():
    age = 22
    return age


def address():
    address = '논현동'
    return address


print(name())
print(age())
print(address())

#이름 나이 주소 argument(인자,매개변수) 3개 받고 return해서 출력 name ,age ,address