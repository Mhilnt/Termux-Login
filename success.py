import os, sys, time
def jalan (kata):
    for e in kata: 
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)
jalan('[!]Access Granted , Login Success')
