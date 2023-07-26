
#배열: index 0부터 시작하고 0부터 값을 얻는다.
#요소 : element

list=[1,2,3]
print(list[0])

print(list[0]+list[2])

print('='*30)
list2=['1','2','3']
print(list[0])

print(list[-3])

print(list[-1]+list[-3])

#배열(array) number=[1,2,3] 1차원 배열
#number=[[1,2],[3,4],[5,6]] 2차원 배열

twoarray=[1,2,3]
print(twoarray[0])
print(twoarray[1])
print(twoarray[2])

twoarray=[1,2,3,[1,2,3]]

#1,2,3 (이름,나이,주소)

home=[1,2,3,['현동윤',22,'논현동']]
print(home[3][0]+'  '+str(home[3][1])+'  '+home[3][2])

twoarray4=[1,2,[1,2,[1,2]]]

print(twoarray4[0])

print(twoarray4[1])
print(twoarray4[2][0])
print(twoarray4[2][1])
print(twoarray4[2][2][0])
print(twoarray4[2][2][1])







