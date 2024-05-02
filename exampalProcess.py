from multiprocessing import Process
import os
def square():
    for i in range(1000000):
        print(i*i)

cpu = os.cpu_count()
print("cpu count is",cpu)
ps=[]
for i in range(cpu):
    p= Process(target = square)
    ps.append(p)
 


if __name__ == '__main__':
    for p in ps:
        p.start()
    for p in ps:
        p.join()  