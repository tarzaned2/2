number='12345678911'
#auto인텔리전스 자동완성기능
print(number.count('1'))
# find 값을 찾지못하면 -1로 출력 (값이 없다)
print(number.find('10'))


print(number.index('8'))
#imdex 값을 찾지 못하면 오류 발생
#print(number.index('10'))

#빈 문자열
str=','
print(str.join('abcd'))
abc='abc'
print(abc.upper())

ABC='ABC'
print(ABC.lower())

ltrim=' 123'
print(ltrim.lstrip())

rtrim='123 '
print(rtrim.rstrip())

abc=' abc def '
print(abc.replace('abc','123'))

#현동윤 본인이름 성을 이씨로 바구고 출력

name='현동윤'
print(name.replace('현','이'))

number='123 456 789'
number2='123/456/789'
#기본적으로 split() 공백을 토큰으로 한다
#토큰 : 식별자 구별자
print(number.split())
print(number2.split('/'))

#이름\나이\주소 출력

home='현동윤!22!논현동'
print(home.split('!'))
