import threading

x = 0

def inc():
    global x
    for i in range(1000000):
        x = x + 1
def dec():
    global x
    for i in range(1000000):
        x = x - 1

t1 = threading.Thread(target=inc)
t2 = threading.Thread(target=dec)
t1.start()
t2.start()
t1.join()
t2.join()
print(x)

# inc와 dec가 각자 돌게됨 