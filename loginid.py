import os,sys,time

x = "Mhilnt"

def login():
    user = raw_input("Username : ")
    os.system("python2 loginpw.py")
    if user ==x:
	time.sleep(2)
    else:
	time.sleep(2)
	os.system("pyton2 loginid.py")
if __name__ == "__main__":
	login()
