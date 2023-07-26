#이름 나이 주소
# %s %d %s  출력
#이름 우측정렬 5칸 이동 나이 좌측정렬 3칸이동 주소 우측정렬 4칸이동
#format 을 이용해서 이름 나이 주소 출력

name='현동윤'
age=22
address='논현동'

print('이름은 %s 나이는 %d 주소는 %s'%(name,age,address))
print('이름은 %5s 나이는 %-3d 주소는 %4s'%(name,age,address))
print('이름은 {0} 나이는 {1} 주소는 {2}'.format(name,age,address))

#{0:<10} 10칸 좌측으로 이동
print('{0:=<10}1234567'.format('hi'))
#우측정렬 10칸 우측으로 이동
print('123{0:=>10}'.format('123'))

print('123456789')
print('{0:!^10}'.format('hi'))

print('{0:10.2f}'.format(3.4134234))

print('{{hi}}'.format())