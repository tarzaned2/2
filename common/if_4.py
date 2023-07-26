if 'abc' == 'abc':
    print('if문 실행')
else:
    print('else문 실행')

# 출력값: if문 실행

if 'abc' != 'abc':
    print('if문 실행')
else:
    print(' else문 실행')

# 출력값: else문 실행

if 3 >= 2:
    print('if문 실행')
else:
    print('else문 실행')

# 출력값: if문 실행

if 3 < 2:
    print('if문 실행')
else:
    print('else문 실행')

# 출력값: else문 실행

if 3 is 3.0:
    print('if문 실행')
else:
    print('else문 실행')

# 출력값: else문 실행

if 3 == 3.0:
    print('true')
else:
    print('false')

a = [1, 2, 3]
b = [1, 2, 3]

# 주소값이 같아진다
# id 주소값 출력

print(id(a))
print(id(b))
a = b

print(id(a))
print(id(b))
print(a is b)
