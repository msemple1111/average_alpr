from plate_gen import plate_gen
#import time
#import threading
import requests
from random import randint
#import timeit 
gen = plate_gen()
#url_1 = 'http://localhost:8080/api/camera/1'
#url_2 = 'http://localhost:8080/api/camera/2'
#headers = {'content-type': 'application/json'}


#  def letter_gen():
#    return str(chr(randint(65,90))
      
#  def number_gen(self,no):
#    from random import randint
#    self.number = []
#    self.number.append(str(randint(0,9)))
#    self.number.append(str(randint(5,6)))
#    return self.number
 
def gen_uk():
  return str(chr(randint(65,90))+chr(randint(65,90))+str(randint(0,9))+str(randint(0,9))+" "+chr(randint(65,90))+chr(randint(65,90))+chr(randint(65,90)))

def gen_timef():
  return gen.gen_time()

def gen_time():
  time_1 = randint(1448000000, 1448600000)
  return time_1, time_1 + randint(2, 20)

def gen_time1():
  return randint(1448000000, 1448600000)
#  def gen_time(self):
#    from random import randint
#    time_1 = randint(1448000000, 1448600000)
#    time = randint(2, 20)
#    time_2 = time_1 + time
#    return time_1, time_2, time
def gen_request():
  r_1 = requests.post('http://localhost:8080/api/camera/1', json={"road":1, "plate":"YH57 GHB", "time": 1448587846}, headers={'content-type': 'application/json'})
def run():
  plate = gen_uk()
  time_1, time_2, time = gen.gen_time()
  payload_1 = {"road":1, "plate":plate, "time": time_1}
  r_1 = requests.post(url_1, json=payload_1, headers=headers)
  payload_2 = {"road":1, "plate": plate, "time": time_2}
  r_2 = requests.post(url_2, json=payload_2, headers=headers)
  
import urllib3
import json
data = json.dumps({"road":1, "plate":"YH57 GHY", "time": 1448587846})
def gen_requests():
  http = urllib3.PoolManager()
  r = http.request('POST', 'http://localhost:7000/api/camera/1',headers={'Content-Type': 'application/json'},body=data)
  
http = urllib3.PoolManager()
def run_2():
  time1, time2 = gen_time()
  plate = "GH56 GHU"
  data1 = json.dumps({"road":1, "plate":plate, "time": time1})
  data2 = json.dumps({"road":1, "plate":plate, "time": time2})
  r1 = http.request('POST', 'http://localhost:7000/api/camera/1',headers={'Content-Type': 'application/json'},body=data1)
  r2 = http.request('POST', 'http://localhost:7000/api/camera/2',headers={'Content-Type': 'application/json'},body=data2)


#    with c.makefile() as f:
#        response = f.readline()
#        if response != RESPONSE_200_STRING:
#            response += f.read()
#print(gen_uk())
if __name__ == '__main__':
  run_2()
  #print('start')
#timeit.timeit('run()','from __main__ import run', number=1000)