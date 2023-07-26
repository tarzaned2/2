person={'name':'현동윤','age':22,'address':'논현동'}

#객체지향
#객체지향언어 python java C++ C# php  # cobol(기계식언어)은행권 속도가빨라서
#큰에서 작은데로간다 무조건
#지구.대한민국.서울시.강남구.서초동.w건물.1304.현동윤
#. 큰데에서 작은데로 가는 토큰
#지구.미국.바이든
#객체.  ->변수, 메소드
person.keys()
#get 얻는다 set 설정한다
keys=person.keys()
print(keys)
print('='*50)
values=person.values()
print(values)

print('='*50)
print(person.get('name'))
print(person.get('age'))
print(person.get('address'))

