a=[1,2,3,4]
result=[]
for i in a:
    print(i)


a=[1,2,3,4]
for i in a:
    result=[i*2 for i in a if i%2==0]

print(result)

print('='*50)
a=[1,2,3,4,5]
print(a)
for i in a:
    b=[i for i in a if i%2==0]

print(b)
for i in a:
    result=0
    c=[result+i for i in a if i%2!=0]
print(c)
for i in a:
    result2=0
    d=[result2+i for i in a if i%2==0]
print(d)