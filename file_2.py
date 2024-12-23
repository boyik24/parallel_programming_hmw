import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

sleep=10
count=100_000_000

def io_b(sec):
    p_id = os.getpid()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutush boshlandi")
    time.sleep(sleep)
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutush yakumlandi")
def cpu_b(k):
    p_id = os.getpid()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutush boshlandi")
    while k>0:
        k=-1
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutush yakumlandi")

# if __name__=="__main__":
    # 1 - single thread  ---  io_b
    s_time = time.time()
    io_b(sleep)
    e_time = time.time()
    print(f"vaqt = {e_time - s_time}")

    # 2 - multithread   ---  io_b
    t1 = Thread(target=io_b,args=(sleep,))
    t2 = Thread(target=io_b,args=(sleep,))
    s_time = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    e_time = time.time()
    print(f"vaqt = {e_time - s_time}")

    # 3 - single thread  ---  cpu_b
    s_time = time.time()
    cpu_b(count)
    e_time = time.time()
    print(f"vaqt = {e_time - s_time}")

    # 4 - multithread  ---   cpu_b
    t1 = Thread(target=cpu_b, args=(count,))
    t2 = Thread(target=cpu_b, args=(count,))
    s_time = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    e_time = time.time()
    print(f"vaqt = {e_time - s_time}")

    # 5 - multiprocessing   ---  io_b
    p1 = Process(target=io_b,args=(sleep,))
    p2 = Process(target=io_b,args=(sleep,))
    s_time = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    e_time = time.time()
    print(f"vaqt = {e_time - s_time}")
    # 6 - multiprocessing   ---  cpu_b
    p1 = Process(target=cpu_b, args=(count,))
    p2 = Process(target=cpu_b, args=(count,))
    s_time = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    e_time = time.time()
    print(f"vaqt = {e_time - s_time}")
