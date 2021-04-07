s = input()
n = int(s)
arrays = []

for i in range(n):
    v = input()
    w = int(v)
    check = True
    for j in range(len(arrays)):
        if arrays[j] == w:
            arrays[j] = -1
            check = False
            break
    if check:    
        arrays.append(w)

count = 0
for i in range(len(arrays)):
    if arrays[i] >= 0:
        count += 1
        
print(count)