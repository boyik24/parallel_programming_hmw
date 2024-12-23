import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process

def file_read(file_name):
    p_id = os.getpid()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutush boshlandi")
    with open(file_name) as file:
        file.read()
    print(f"{p_id} --- {current_process().name} --- {current_thread().name} --- kutush yakumlandi")
file_name=["file_1.py","file_2.py"]

if __name__=="__main__":
    for i in range(2):
        print(f"{i+1} chi file uchun")
        print("Single thread")
        s_time = time.time()
        file_read(file_name[i])
        e_time = time.time()
        print(f"vaqt = {e_time - s_time}")
        print("multithread")
        t1 = Thread(target=file_read,args=(file_name[i],))
        t2 = Thread(target=file_read,args=(file_name[i],))
        s_time = time.time()
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        e_time = time.time()
        print(f"vaqt = {e_time - s_time}")
        print("multiprocessing")
        p1 = Process(target=file_read,args=(file_name[i],))
        p2 = Process(target=file_read,args=(file_name[i],))
        s_time = time.time()
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        e_time = time.time()
        print(f"vaqt = {e_time - s_time}")
        print()