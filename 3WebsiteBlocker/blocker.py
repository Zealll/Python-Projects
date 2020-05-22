import time
from datetime import datetime as dt
host_path = r"C:\Windows\System32\drivers\etc\hosts"
temp = 'hosts'
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com"]

# print(dt(dt.now().year, dt.now().month, dt.now().day, 8))

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        with open(temp, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write('\n' + redirect + ' ' + website)
    else:
        with open(temp, 'r+') as file:
            content = file.readlines()
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)

    time.sleep(5)