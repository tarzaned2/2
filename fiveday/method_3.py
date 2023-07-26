def home(*home):
    print(home)


def home2(name, *home):
    print(f'이름은 {name} 데이터는 {home}')


home(1, 2, 3, 4, 5)
home2('현동윤', '논현동', '2222')


# 1~10을 메소드 sum(input)합을 return해서 풀력하시오

def sum(*input):
    result = 0
    for i in input:
        result = result + i
    return result


result = sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(result)
