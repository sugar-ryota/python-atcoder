import queue

o = input()
e = input()

odd = list(o)
even = list(e)

answer = []

o_q = queue.Queue()
e_q = queue.Queue()

for i in range(len(odd)):
    o_q.put(odd[i])

for i in range(len(even)):
    e_q.put(even[i])

while not o_q.empty():
    answer.append(o_q.get())
    if e_q.empty():
        continue
    answer.append(e_q.get())

for i in range(len(answer)):
    print(answer[i],end='')

    