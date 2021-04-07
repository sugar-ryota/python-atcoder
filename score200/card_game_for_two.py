s = input()
n = int(s)

cards = []

answer = 0

v = input().split()
for i in range(n):
    cards.append(v[i])

v = sorted(v,reverse=True)

alice_array = []
bob_array = []

for i in range(len(v)):
    if i % 2 == 0:
        alice_array.append(v[i])
    else:
        bob_array.append(v[i])

sum_alice = 0
sum_bob = 0
for i in range(len(alice_array)):
    sum_alice += int(alice_array[i])

for i in range(len(bob_array)):
    sum_bob += int(bob_array[i])

answer = sum_alice - sum_bob
print(answer)
