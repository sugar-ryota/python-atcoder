s = input()
n = int(s)

# 約数を求める処理
answer = n

for i in range(1,n + 1):
    for j in range(i, n + 1):
        if i > j:
            continue
        if i * j == n:
            x = i
            y = j
            count_i = 0
            count_j = 0
            while (x > 0):
                x = int(x/10)
                count_i += 1
            while (y > 0):
                y = int(y/10)
                count_j += 1
            answer = min(max(count_i,count_j),answer)
            break

print(answer)