import getpass
import os, sys, time


p = getpass.getpass(prompt='Password : ')
if p == 'password' :
    os.system("python2 Loading.py")
    os.system("python2 success.py")
    time.sleep(2)
    os.system("clear")
else:
    os.system("python2 Loading.py")
    print("Access Denied , Incorrect Password Or Username")
    time.sleep(2)
    os.system("clear")
    os.system("python2 loginid.py")
