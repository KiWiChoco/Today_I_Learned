import threading

def countdown(count):
    while count != 0 :
        count = count - 1

    return

t1 = threading.Thread(target = countdown, args = (10,))

t1.start()

t1.join()
