name='현동윤'
age=22
address='논현동'

print('이름은 %s 나이는 %d 사는 곳은 %s'%(name,age,address))

#인덱싱
#이름 나이 주소 이메일 전화번호
#이름은  나이는 주소는 이메일은 전화번호는

name='현동윤'
age=22
address='논현동'
email='dyoon0830@naver.com'
phonenumber='010-4124-9859'
home='현동윤 22 논현동 dyoon0830@naver.com 010-4124-9859'

print('이름은:',home[0:3])
print('나이는:',home[4:6])
print('주소는:',home[7:10])
print('이메일은:',home[11:30])
print('전화번호는:',home[31:44])

print('이릉은:%s,나이는:%d,주소는:%s,이메일은:%s,전화번호는:%s'%(name,age,address,email,phonenumber))
