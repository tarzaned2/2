#if 조건문 if 맞으면 true : 실행 else : false 실행

if True:
    print(True)
else:
    print(False)

print('='*50)
init=10
if init<=5:
    print(True)
else:
    print(False)

a=1
#== : 같다 객체가 틀리더라도 타입하고 값이 같으면 같다
if a==1:
    print(True)
else:
    print(False)

#switch
print('='*50)
#50점이상이면 잘했습니다
#60점이상이면 정말 잘했습니다
#40점이상이ㅕㅁㄴ 보통입니다
#input() 키보드 <inputstream, 모니터 outputstream
#input()  키보드 입력을 받겠다 (문자열,)
#ins=input('키보드입력하세요')
#print(ins)


ins=input('점수를 입력하세요')

ins=int(ins)
if ins>=60:
        print('정말 잘했습니다')
else :
        if 50<=ins:
              print('잘했습니다')
        else:
            if 40<=ins:
                print('보통입니다')
