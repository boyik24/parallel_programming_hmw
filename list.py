import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process
a=list(range(1,500))
def bound(a):
    p1=1
    p2=1
    p_id = os.getpid()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutush boshlandi")
    for i in a:
        if i%2==0:
            p1*=i
        else:
            p2*=i
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutush yakunlandi")
    print(p1-p2)

if __name__=="__main__":
    # single thread
    s_time=time.time()
    bound(a)
    e_time=time.time()
    print("vaqt =",e_time-s_time)

    # multi thread
    t1=Thread(target=bound,args=(a,))
    t2=Thread(target=bound,args=(a,))
    s_time=time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    e_time=time.time()
    print("vaqt =",e_time-s_time)

    # multiprocessing
    p1=Process(target=bound,args=(a,))
    p2=Process(target=bound,args=(a,))
    s_time=time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    e_time=time.time()
    print("vaqt =",e_time-s_time)