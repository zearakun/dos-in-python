import requests
from time import sleep
import threading






url = input('URLを貼ってください')
time = float(input('一回のリクエストでかかる遅延'))
thread_count = int(input('スレッドの数'))











import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


def target():
  while True:
    r = requests.get(url,verify=False,allow_redirects = False)
    if r.status_code == 200:
      print("Connection Successful")
    sleep(time)

threads = []


for a in range(thread_count):
  threads.append(threading.Thread(target=target))
  threads[a].start()
