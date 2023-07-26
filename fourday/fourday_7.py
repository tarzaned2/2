a=[1,2,3]
b=[1,2,3]

a=b
#id : 주소값출력
print(id(a))
print(id(b))
print(a is b)

a,b=('a','b')
print(a)
print(b)

a,b=b,a

print(a)
print(b)