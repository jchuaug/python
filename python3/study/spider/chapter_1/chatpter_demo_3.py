#!/usr/bin/python
#使用threading模块创建多线程
import random
import time,threading
#新线程执行的代码
def thread_run(urls):
    print("current %s is running..."%threading.current_thread().name)
    for url in urls:
        print("%s----->%s"%(threading.current_thread().name,url))
        time.sleep(random.random())
    print("%s ended"%(threading.current_thread().name))
print("%s is running..."%threading.current_thread().name)
t1=threading.Thread(target=thread_run,name="Thread1",args=(["urls_1",'urls_2',"urls_3"],))
t2=threading.Thread(target=thread_run,name="Thread2",args=(["urls_4",'urls_5',"urls_6"],))
t1.start()
t2.start()
t1.join()
t2.join()

print("%s ended"%threading.current_thread().name)