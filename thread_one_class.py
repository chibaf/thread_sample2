class thread_one:

  def __init__(self,i):   # initial action
    print(" start "+str(i))

  def thread(self,a,q): # class body
    import time
    time.sleep(1)
    ret = [a,2]  # return value
    q.put(ret)   # set value to queu
    return
