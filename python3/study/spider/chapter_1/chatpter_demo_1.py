import  os
'''
with open(r'contacts.txt','r')as fileReader:
    for line in fileReader.readlines():
        print(line.strip())
'''


# print(os.getcwd())
# print(os.listdir("C :\\"))
#使用fork创建多线程
'''
if __name__=="__main__":
    print("current Process (%s) start ..."%(os.getpid()))
    pid=os.fork()
    if pid<0:
        print("Error in fork")
    elif pid==0:
        print("I am child process (%s) and myb parent process is (%s)",(os.getpid(),os.getppid()))
    else:
        print("I (%s) created a child process (%s)",(os.getpid(),pid))
'''

#使用mutiprocessing模块创建多线程


from multiprocessing import  Process
#The code that the child process is going to execute
def run_proc(name):
    print("Child process %s(%s) is Running..."%(name,os.getpid()))
if __name__=="__main__":
    print("Parent process %s"%os.getpid())
    for i in range(5):
        p=Process(target=run_proc,args=(str(i),))
        print("Process will be start")
        p.start()
    p.join()
    print("Process end")


#使用mutiprocessing模块提供的Pool类开生成大量的多线程
'''
import time,random
from multiprocessing import Pool
def run_task(name):
    print("task %s (pid=%s) is running..."%(name,os.getpid()))
    time.sleep(random.random()*3)
    print("task %s end."%name)
if __name__=="__main__":
    print("current process %s"%os.getpid())
    p=Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task(i))
    print("waiting for all subprocess done....")
    p.close()
    p.join()
    print("all process done")

'''