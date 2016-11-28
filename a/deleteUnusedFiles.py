import os, time
from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
ref_time = now - relativedelta(months = 6)
print(now)
print(ref_time)

def func():
    files = os.listdir()
    for f in files:
        stats = os.stat(f)
        access_time = datetime.fromtimestamp(stats.st_atime)
        print(f, access_time)
        if access_time < ref_time:
            print(f, '---')

func()


#if __name__ == '__main__':

