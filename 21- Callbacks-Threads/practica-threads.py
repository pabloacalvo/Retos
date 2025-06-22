import requests
import time
from threading import Thread
import logging

logging.basicConfig(level=logging.INFO,format='%(threadName)s-%(levelname)s-%(message)s')

def get_user(x):
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        #print(response.json())
        logging.info(f"Thread numero {x}")
    else:
        logging.info(response.status_code)

start = time.time()
threads = []

for x in range(100):
    thread = Thread(target=get_user,args=(x,), name=x)
    thread.start()
    threads.append(thread)

    print(x)

for t in threads:
    t.join()


# Algoritmo
print(time.time() - start)
