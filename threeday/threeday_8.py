a=[1,2,3]

print(a[0:3])
b=[1,2,[1,2,3,4]]
print(b[2][0:2])

print(b[2][0:4])
print(b[2][0:])

a=[1,2,3]
b=[4,5,6]

c=a+b
print(c)
print(a*3)
print(len(a))

age=22
age=22+1


#str 정수형을 문자열로 바꿔준다 (형변환)(캐스팅)
print(age)
print(str(age)+'str')





#age2='22'
#print(age2+1)

#list 수정
a=[1,2,3]
a[1]=5
print(a)

del a[1]
print(a)

a=[1,2,3,4]
del a[0:2]
print(a)

a=[1,2,3]
a.append(4)
print(a)

a=[4,2,1,3]
a.sort()
print(a)

a=['a','b','c']
a.reverse()
print(a)

print(a.index('c'))

#index : element의 index 위치를 나타냄
a=[1,2,3,1]
print(a.index(2))

#del : x번째 위치로 제거 #remove :첫번째 x만 제거
a.remove(1)
print(a)

a=[1,2,3]
a.insert(3,4)
print(a)

a=[1,2,3,1]
print(a.count(1))

a.extend([4,5])

print(a)