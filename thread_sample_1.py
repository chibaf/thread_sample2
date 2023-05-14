import threading
import queue,time
from thread_one_class import thread_one

i=1
thread1=thread_one(i)
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=thread1.thread, args=(i,q),daemon=True)
th.start()
#th.join()
while True:
  if th.is_alive()==False:
    result = q.get()
    print("thread: "+str(i)+" "+str(result))
    i=i+1
    if i>5:
      break;
    thread1=thread_one(i)
    th = threading.Thread(target=thread1.thread, args=(i,q),daemon=True)
    th.start()
  time.sleep(2)  #do other tasks

exit()
