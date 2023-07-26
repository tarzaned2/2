a = [1, 2, 3, 4]
b = []

for i in a:
    b.append(i * 2)

print(b)

# 1~10 a리스트 b리스트 홀수값만저장

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []

for i in a:
    if i % 2 != 0:
        b.append(i)

print(b)

# a 1부터 5까지 b는 짝수만 저장 C는 홀수의 합 저장

print('=' * 50)
a = [1, 2, 3, 4, 5]
b = []
c = []
d = []

for i in a:
    if i % 2 == 0:
        b.append(i)

one = 0
for i in a:
    if i % 2 != 0:
        one = one + i
c.append(one)

two = 0
for i in a:
    if i % 2 == 0:
        two = two + i
d.append(two)

print(a)
print(b)
print(c)
print(d)
