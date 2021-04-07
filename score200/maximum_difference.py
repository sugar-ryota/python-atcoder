s = input()
n = int(s)

arrays = []

max_num = 0

v = input().split()
for i in range(n):
    arrays.append(int(v[i]))

for i in range(len(arrays)):
    max_num = max(max_num, arrays[i])

min_num = max_num

for i in range(len(arrays)):
    min_num = min(min_num,arrays[i])

answer = max_num - min_num

print(answer)