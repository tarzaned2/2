for i in range(1, 6):
    for x in range(1, 4):
        print(f'{i}가 돌때 안쪽 for문은 {x}', end='\t')
    print('\n')

# 구구단 2*1=2  2*2=4 ... 2*9=18


print('=' * 50)
for i in range(2, 10):
    for x in range(1, 10):
        print(f'{i} x {x}=', i * x, end='\t')
    print('\n')

print('=' * 50)
for x in range(1, 10):
    for i in range(2, 10):
        print(f'{i} x {x}=', i * x, end='\t')
    print('\n')
