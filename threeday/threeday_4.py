
float=3.42134234
#모든숫자 표시 0.4는 소수점 표시 자릿수

#int 정수 float 실수
print('%0.2f'%float)
#기본적으로 우측정렬 10칸이동 6칸 이동 + 3.42(4자리) =10칸
print('%10.2f'%float)

name='현동윤'
#object : 어떤 타입이든 올수 있다 (문자열, 정수형,실수형)
#형식  {0}.format(object)
print('='*30)
print('이름은 {0}'. format(name))
print('이름은 {0}'.format('현동윤'))

print('나이는 {0}'.format(22))

name='현동윤'
age=22
print('이름은 {0} 나이는 {1}'.format(name,age))
print('이름은 {name2} 나이는 {age2}'.format(name2='현동윤',age2=22))

#