import itertools
import threading
import time
import sys

done = False

def animate():
    for c in itertools.cycle(['|','/','-','\\']):
	if done:
	    break
	sys.stdout.write('\rLoading ' + c)
	sys.stdout.flush()
	time.sleep(0.1)
	sys.stdout.write('\r ')

t = threading.Thread(target=animate)
t.start()

time.sleep(2)
done = True
