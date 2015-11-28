from plate_gen import plate_gen
#import time
#import threading
import requests
#import timeit 
gen = plate_gen()
url_1 = 'http://localhost:7000/api/camera/1'
url_2 = 'http://localhost:7000/api/camera/2'
headers = {'content-type': 'application/json'}
    
def run():
  plate = gen.gen_uk()
  time_1, time_2, time = gen.gen_time()
  payload_1 = {"road":1, "plate":plate, "time": time_1}
  r_1 = requests.post(url_1, json=payload_1, headers=headers)
  payload_2 = {"road":1, "plate": plate, "time": time_2}
  r_2 = requests.post(url_2, json=payload_2, headers=headers)

#if __name__ == '__main__':
  #print('start')
#timeit.timeit('run()','from __main__ import run', number=1000)