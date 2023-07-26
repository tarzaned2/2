#이름 나이 주소 이메일 전화번호

name='현동윤'
age=22
address='논현동'
email='dyoon0830@naver.com'
phonenumber='010-4124-9859'

print('이름은:%s 나이는:%d 주소는:%s 이메일은:%s 전화번호는:%s'%(name,age,address,email,phonenumber))

#기본적으로 우측정렬인데 %10이면 10칸 문자열 포함해서 10칸
print('%10s' %'123')
print('123456789')
print('%10s'%'123456789')

#좌측정렬 좌측으로 10칸
print('%-10s1234567'%'123')
