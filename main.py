import requests
from time import sleep
import threading
import subprocess
import json
import random
from fake_useragent import UserAgent






url = input('URLを貼ってください')
time = float(input('一回のリクエストでかかる遅延'))










ua = UserAgent()



import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)





while True:
    f = open('proxies.txt')
    combos = f.readlines()
    proxys = random.choice(combos)
    proxies = {
    "http":"http://"+proxys,
    "https":"http://"+proxys
    }
    r = requests.get(url, proxies=proxies, headers={"User-Agent": f"{ua.random}"},verify=False,allow_redirects = False)
    if r.status_code == 200:
      print("Connection Successful"+proxys)
    sleep(time)
