from plate_gen import plate_gen
import requests
import json
import urllib3
gen = plate_gen()
http = urllib3.PoolManager()
url_1 = 'http://localhost:7000/api/camera/1'
url_2 = 'http://localhost:7000/api/camera/2'
road = 1
headers = {'Content-Type': 'application/json'}

def make_payload(road, plate, time):
  data = {"version":2,"data_type":"alpr_results",
          "epoch_time":time,
          "img_width":480,"img_height":640,
          "processing_time_ms":160.482773,
          "regions_of_interest":[],
          "results":[
      {"plate":plate,
       "confidence":87.164879,
       "matches_template":0,
       "plate_index":0,
       "region":"",
       "region_confidence":0,
       "processing_time_ms":16.496367,
       "requested_topn":10,
       "coordinates":[{"x":190,"y":378},{"x":268,"y":378},{"x":268,"y":415},{"x":190,"y":415}],
       "candidates":[{"plate":"plate","confidence":87.164879,"matches_template":0},
          {"plate":"7860","confidence":85.919258,"matches_template":0},
          {"plate":"78610","confidence":83.191833,"matches_template":0},
          {"plate":"786W0","confidence":80.517082,"matches_template":0},
          {"plate":"786D0","confidence":80.371925,"matches_template":0},
          {"plate":"786B0","confidence":80.036629,"matches_template":0},
          {"plate":"786PO","confidence":74.894852,"matches_template":0},
          {"plate":"786PQ","confidence":73.900421,"matches_template":0},
          {"plate":"786O","confidence":73.649231,"matches_template":0},
          {"plate":"786Q","confidence":72.654800,"matches_template":0}]
      }
    ]}

  return json.dumps(data)

#using the requests framwork
def run():
  time_1, time_2 = gen.gen_time()
  plate = gen.gen_uk()
  payload_1 = json.dumps({"road":1, "plate":plate, "time": time_1})
  payload_2 = {"road":1, "plate": plate, "time": time_2}
  r_2 = requests.post(url_2, json=payload_2, headers=headers)
  r_1 = requests.post(url_1, json=payload_1, headers=headers)
  
#using the urllib3 framwork
def run_2():
  time_1, time_2 = gen.gen_time()
  plate = gen.gen_uk()
  payload_1 = make_payload(road, plate, time_1)
  payload_2 = make_payload(road, plate, time_2)
  r1 = http.request('POST', url_1, headers=headers, body=payload_1)
  r2 = http.request('POST', url_2, headers=headers, body=payload_2)

if __name__ == '__main__':
  run_2()
