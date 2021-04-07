s = input()
n = int(s)

check = True

arrays = []

for i in range(n):
    v = input()
    x = list(v)
    if i > 0:
        if not y == x[0]:
            check = False
            break
    for j in range(len(arrays)):
        if arrays[j] == v:
            check = False
            break
    arrays.append(v)
    y = x.pop()

if check:
    print('Yes')
else:
    print('No')
        
    