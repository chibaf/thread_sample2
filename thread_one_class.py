class thread_one:

  def __init__(self,i):
    print(" start "+str(i))

  def thread(self,a,q):
    import time
    time.sleep(1)
    ret = [a,2]
    q.put(ret)
    return
