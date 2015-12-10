#!bin/python
#import classes
from classes import *
from flask import Flask, jsonify, request, abort, make_response
import json
application = Flask(__name__)

@application.errorhandler(400)
def bad_request_400(error):
  #error(400,'error 400')
  return make_response(jsonify( { 'error': True, 'error_type': 'Bad request', 'error_no': 400} ), 400)

@application.errorhandler(404)
def not_found_404(error):
  #error(404,'error 404')
  return make_response(jsonify( { 'error': True, 'error_type':'Not found', 'error_no': 404} ), 404)
  
@application.errorhandler(405)
def not_found_404(error):
  #error(405,'error 405')
  return make_response(jsonify( { 'error': True, 'error_type':'Method Not Allowed', 'error_no': 405} ), 405)
@application.errorhandler(500)
def internal_error_500(error):
  #error(500,'error 500')
  return make_response(jsonify( { 'error': True, 'error_type':'Internal Server Error', 'error_no': 500 } ), 500)

@application.route("/", methods=['GET','POST'])
def hello():
  return "<h1 style='color:blue'>Hello There!,,G</h1>"

@application.route('/api/camera', methods=['POST'])
def cam():
  request_data = json.loads(request.json)
  valid = validate()
  site_id = valid.site(request_data['site_id'])
  cam_id = valid.cam(request_data['camera_id'])
  uuid = valid.uuid(request_data['uuid'])
  epoch_time = valid.time(request_data['epoch_time'])
  sqlite = database()
  calc = calculate()
  curr_cam_m = sqlite.curr_cam(cam_id, site_id)#
  plates = []
  s_limit, s_id = sqlite.find_site(site_id)
  for plate in range(0,len(request_data['results'])):
    p_name, p_forign = valid.plate(request_data['results'][plate]['plate'])
    p_confidence = valid.confidence(request_data['results'][plate]['confidence'])
    p_id = sqlite.add_plate(p_name, p_forign)#
    plates.append(p_name, p_forign, p_confidence)#
    time_1, prev_cam_m = sqlite.last_cam(p_id, site_id)#
    r_dist = prev_cam_m - curr_cam_m
    car_speed = calc.average_speed(time_1, time_2, r_dist)
    speed = calc.speed_increase(car_speed, s_limit)
    sqlite.record_time(cam_id, p_id, site_id, uuid, time)#
  #log p_id to sqlite data with r_id
  #post data should look like (in any order) '{"road":1, "plate":"YS54 GBF", "time": 1442862678}'
                                             #(road id,   number plate,      time in unix epoch)
  return json.dumps({'error': False})

@application.route('/api/camera/2', methods=['POST'])
def cam_2():
  
  valid = validate()
  road_id = valid.road(request.json['road'])#validating the road number input and then assinging it to a varible
  p_name, p_forign = valid.plate(request.json['plate']) #validating the number plate input, assinging it to a varible and then returning if it is forign or not
  time_2 = valid.time(request.json['time']) #validating the 'time' input and then assing it to a varible
  
  sqlite = database() #initlising the database class
  p_id = sqlite.add_plate(p_name, p_forign) #the plate id
  r_id = sqlite.check_road_id(road_id) #the road id
  
  d_index = sqlite.get_d_index(p_id, r_id) #the data storage id
  time_1 = sqlite.get_time_1(p_id, r_id) # time in sec
  r_dist = sqlite.get_r_dist(r_id) #road distance in m
  s_limit = sqlite.get_s_limit(r_id) #speed limit in m/s
  
  calc = calculate()
  car_speed = calc.average_speed(time_1, time_2, r_dist)
  speed = calc.speed_increase(car_speed, s_limit)
  
  sqlite.record_time_2(d_index, time_2, speed)
  return jsonify({'error': False}) #return green light

def http_error(error_no):
  abort(error_no)
  
if __name__ == '__main__':
  application.run(host='0.0.0.0', port=7000, debug=True)
