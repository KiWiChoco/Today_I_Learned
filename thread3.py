import threading
k=0
def worker(num):
    k=0
    for j in range(10000000):
        k+=j
#교재에 있는것에서 위에 for루프를 추가했는데 교재는 worker라는 함수가 너무간단해서 그냥 씹히게되서 active_coutn()가 제대로 출력되지않음
#함수한테 일을 좀 시켜야지 카운트가됨

    print('Worker : %s'%num)
    return

threads = []

for i in range(5):
    t = threading.Thread(target=worker,args=(i,))
    threads.append(t)
    t.start()
    #t.join() #<- 이걸 넣어주면 main thread가 thread 1,2,3,4,5 다섯개를 하나씩 거치면서 조인해서 흡수함 그래서 active_count()값은 1이나옴

print(threading.active_count())

