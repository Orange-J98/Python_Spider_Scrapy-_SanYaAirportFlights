import subprocess
import datetime
import time

def doSth():
    # 把爬虫程序放在这个类里 MySpider 是爬虫的name
    print('Start...')
    cmd = 'scrapy crawl MySpider -o '+"data"+str(datetime.datetime.now().month)+str(datetime.datetime.now().day)+'.json'
    p=subprocess.Popen(cmd)

# 想几点更新,定时到几点
def time_ti(h=17, m=14):
    while True:
        now = datetime.datetime.now()
        if now.hour == h and now.minute == m:
            doSth()
        # 每隔60秒检测一次
        time.sleep(60)
time_ti()
