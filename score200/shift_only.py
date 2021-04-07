s = input()

n = int(s)

numbers = []
answer = 0
check = True

v  =input().split()

for i in range(n):
    numbers.append(int(v[i]))

while (check):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            check = False
        else:
            numbers[i] /= 2
    if check:
        answer += 1

print(answer)


