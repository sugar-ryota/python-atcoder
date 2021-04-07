import queue

a_cards = input()
b_cards = input()
c_cards = input()


a_c = list(a_cards)
b_c = list(b_cards)
c_c = list(c_cards)

a_que = queue.Queue()
b_que = queue.Queue()
c_que = queue.Queue()

for num in range(len(a_c)):
    a_que.put(a_c[num])

for num in range(len(b_c)):
    b_que.put(b_c[num])

for num in range(len(c_c)):
    c_que.put(c_c[num])




x = a_que.get()

while True:
    if x == 'a':
        if a_que.empty():
            answer = 'A'
            break
        x = a_que.get()
    elif x == 'b':
        if b_que.empty():
            answer = 'B'
            break
        x = b_que.get()
    else:
        if c_que.empty():
            answer = 'C'
            break
        x = c_que.get()

print(answer)
 