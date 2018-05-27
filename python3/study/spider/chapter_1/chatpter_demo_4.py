#!/usr/bin/python
#从threading.Thread继承创建线程
import random
import time,threading
class myThread(threading.Thread):
    def __init__(self,name,urls):
        threading.Thread.__init__(self,name=name)
        self.urls=urls
    def run(self):
        print("Current %s is running..."%threading.current_thread().name)
        for url in self.urls:
            print("%s--->>>%s"%(threading.current_thread().name,url))
            time.sleep(random.random())
        print("%s ended"%threading.current_thread().name)
print("%s is running..."%threading.current_thread().name)
t1=myThread(name="Thread1",urls=["urls_1","urls_2","urls_3"])
t2=myThread(name="Thread2",urls=["urls_4","urls_5","urls_6"])
t1.start()
t2.start()
t1.join()
t2.join()


print("%s ended"%threading.current_thread().name)