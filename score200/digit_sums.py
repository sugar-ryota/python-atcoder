s = input()

n = int(s)

arrays = []

y = n

while y > 0:
    arrays.append(y % 10)
    y = int(y / 10)

sum_num = 0

for i in range(len(arrays)):
    sum_num += arrays[i]

if n % sum_num == 0:
    print('Yes')
else:
    print('No')

