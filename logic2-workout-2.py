#Threading:
#Each function or class have one thread
from threading import *
import time
class process1(Thread):
    def run(self):
        list1=[]
        for i in range(1,11):
            if i%2==0:
                list1.append(i)
                print(i)
                time.sleep(0.1)
class process2(Thread):
    def run(self):
        list2=list()
        for i in range(1,11):
            if i%2!=0:
                list2.append(i)
                print i
                time.sleep(0.1)
obj_p1 = process1()
obj_p1.start()
obj_p2 = process2()
obj_p2.start()

# one func() have muliple thread
from threading import Thread
import os

iplist = ['192.168.125.219', '192.168.125.188', '192.168.125.235']
def post_fdr(arg):
    cmd = "./probefdr22_mod.sh" + ' ' + arg
    print cmd
    os.system(cmd)
for ip in iplist:
    th = Thread(target=post_fdr, args=(ip,))
    th.start()
    print "threading...."


