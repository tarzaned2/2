money=50

#다중 if
#조건이 맞으면 밑에 if 실행안된다

if money>=60:
    print('정말 잘했습니다')


elif money>=50:
    print('잘했습니다')

# a(true) and b(true) -> true
# b(true) and b(false) ->false
print('='*50)
if 1==1 and 2==2:
    print(True)

print('='*50)
if 1==1 or 2==2:
    print(True)
else:
        print(False)


a=[1,2,3]
#a 안에 list type 요소를 검색 : in  요소가 맞으면 true
print('='*50)
if 1 not in a:
    print(True)
else:
    print(False)

if 2 not in a:
    print(True)
else:
    print(False)

if 3 not in a:
    print(True)
else:
    print(False)

    print('='*60)
a=60
if a==60:
    #print(True)
    pass
else:
    print(False)

