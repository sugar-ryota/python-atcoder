s = input().split()

sx = int(s[0])
sy = int(s[1])
tx = int(s[2])
ty = int(s[3])

answer = []

for num in range(ty - sy):
    answer.append('U')

for num in range(tx - sx):
    answer.append('R')

for num in range(ty - sy):
    answer.append('D')

for num in range(tx - sx):
    answer.append('L')

answer.append('L')

for num in range(ty - sy + 1):
    answer.append('U')

for num in range(ty - sx + 1):
    answer.append('R')

answer.append('D')

answer.append('R')

for num in range(ty - sy + 1):
    answer.append('D')

for num in range(tx - sx + 1):
    answer.append('L')

answer.append('U')

for num in range(len(answer)):
    print(answer[num], end='')
    
print('')