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

print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")
print("dfgfhjfh")
print("jxtcuvih")