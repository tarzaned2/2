




a=[1,2,3]
#
for i in a:
    print(i)

    #1부터 3가지 합 출력
print('='*60)
a=[1,2,3]
result=0
for i in a:
    result=result+i

print(result)

print('='*50)
a=[1,2,3,4,5,6,7,8,9,10]
result=0
for i in a:
    result=result+i

print(result)

print('='*50)

a=[[1,2],[3,4],[5,6]]
for (first, last) in a:
    print(first+last)

    print('='*50)

a=[1,2,3,5,6]
#예약어 : 이미 정해져있는거

for x in a:
    print(x)
    if x>=5:
        continue

        #print(x)

