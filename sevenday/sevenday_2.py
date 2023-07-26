print('test')
a = 1


def vartest():
    # global a
    b = 0
    result = b + 1
    global a
    a = result
    print(a)


vartest()

# dictionary input key value 데이터 입력 name 이름
# {'name':'현동윤','name':'이순신'}

# 출력 검색
print('=' * 50)
print('q를 누르면 종료')
while True:

    print('name:')
    if a != 'q':
        a = input()
        print({'name': a})
    if a == 'q':
        quit()

    print(a.get('name', '있습니다'))
