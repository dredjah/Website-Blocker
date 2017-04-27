import time
from datetime import datetime as dt

#Path of host file on computer. 'r' before filename is good practice when passing a string with slashes to stop python interpreting as 'new line' in case of '\n'

#temporary path for testing
hosts_temp = "hosts"

#path to real 'hosts path' on computer
hosts_path = "insert path to 'hosts' file on computer"
redirect = "127.0.0.1"

#list of websites to block
website_list = ["www.facebook.com", "facebook.com"]


#set up infinite loop that runs every 100 seconds
while True:

#Check if time is between 9 and 5.
#If True, check if websites are already in 'hosts' file, do nothing. Otherwise, insert websites to block and redirect
    if dt(dt.now().year,dt.now().month,dt.now().day, 9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 17):
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else: file.write(redirect + "  " + website + "\n")

#If outside time-period, remove lines that block websites
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            #returns cursor to start
            file.seek(0)
            for line in content:
                k=0
                for website in website_list:
                    if website in line:
                        k=k+1
                if k == 0:
                    file.write(line)
            #removes duplicated entry
            file.truncate()
    time.sleep(100)
