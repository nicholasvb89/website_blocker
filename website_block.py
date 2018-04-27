import time
from datetime import datetime as dt

hosts_temp= "hosts.txt"
hosts_path=r"/etc/hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 18) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
        with open(hosts_path, 'r+') as f:
            content = f.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    f.write(f'{redirect} {website}\n')
            
    else:
        with open(hosts_path, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    f.write(line)
            f.truncate()
    time.sleep(5)
