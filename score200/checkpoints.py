s = input().split()

n = int(s[0])
m = int(s[1])

x = []
y = []

check_x = []
check_y = []

dis = 0
mindis = 1000000000
answer = []
for i in range(m):
    answer.append(0)

for i in range(n):
    a = input().split()
    x.append(int(a[0]))
    y.append(int(a[1]))

for i in range(m):
    a = input().split()
    check_x.append(int(a[0]))
    check_y.append(int(a[1]))

for j in range(n):
    dis = 0
    mindis = 1000000000
    for i in range(m):
        dis = abs(x[j] - check_x[i]) + abs(y[j] - check_y[i])
        if dis < mindis:
            mindis = dis
            answer[j] = i + 1

for i in range(n):
    print(answer[i])

        
        
