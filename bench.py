from plate_gen import plate_gen
import requests
import json
import urllib3
import uuid
from database import database
gen = plate_gen()
http = urllib3.PoolManager()
url = 'http://localhost:7000/api/camera'
#url_2 = 'http://localhost:7000/api/camera/2'
road = 1
#plate = "HT57 GHU"
headers = {'Content-Type': 'application/json'}

def make_payload(cam_id, plate, time):
  cam_uuid = str(uuid.uuid4())
  data = {"version":2,
          "data_type":"alpr_results",
          "epoch_time":time,
          "site_id":"Cdon Way",
          "camera_id":cam_id,
          "uuid":cam_uuid,
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

  return str(json.dumps(data))

#using the requests framwork
def run():
  plate = gen.gen_uk()
  time_1 = gen.gen_time()
  time_2 = gen.gen_more_time(time_1)
  time_3 = gen.gen_more_time(time_2)
  time_4 = gen.gen_more_time(time_3)
  payload_1 = make_payload(1, plate, time_1)
  payload_2 = make_payload(2, plate, time_2)
  payload_3 = make_payload(3, plate, time_3)
  payload_4 = make_payload(4, plate, time_4)
  r_1 = requests.post(url, data=payload_1, headers=headers)
  r_2 = requests.post(url, data=payload_2, headers=headers)
  r_3 = requests.post(url, data=payload_3, headers=headers)
  r_4 = requests.post(url, data=payload_4, headers=headers)

#using the urllib3 framwork
def run_2():
  time_1, time_2 = gen.gen_time()
  #plate = gen.gen_uk()
  payload_1 = make_payload(road, plate, time_1)
  payload_2 = make_payload(road, plate, time_2)
  r1 = http.request('POST', url, headers=headers, body=str(payload_1))
  r2 = http.request('POST', url, headers=headers, body=str(payload_2))

def run3():
    site_id = 'cdon way'
    site_cam_id = 1
    time_2 = gen.gen_time()
    sqlite = database()
    s_id, s_limit = sqlite.find_site(site_id)
    self.cam_id = sqlite.get_cam_id(site_cam_id, s_id)
    self.curr_cam_m = sqlite.get_cam_m(cam_id, s_id)

if __name__ == '__main__':
  run3()
