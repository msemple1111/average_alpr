#!bin/python
#import classes
from classes import *
from flask import Flask, jsonify, request, abort, make_response
from flask.ext.httpauth import HTTPBasicAuth
application = Flask(__name__)

auth = HTTPBasicAuth()
@auth.get_password
def get_password(username):
  if username == 'cam_1':
    return 'python'
  if username == 'cam_2':
    return 'python'
  return None

@auth.error_handler
def unauthorized():
  #error(403,'error 403')
  return make_response(jsonify( { 'error': True, 'error_type': 'Unauthorized access', 'error_no': 403}), 403)
# return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@application.errorhandler(400)
def bad_request_400(error):
  #error(400,'error 400')
  return make_response(jsonify( { 'error': True, 'error_type': 'Bad request', 'error_no': 400} ), 400)

@application.errorhandler(404)
def not_found_404(error):
  #error(404,'error 404')
  return make_response(jsonify( { 'error': True, 'error_type':'Not found', 'error_no': 404} ), 404)
  
@application.errorhandler(500)
def internal_error_500(error):
  #error(500,'error 500')
  return make_response(jsonify( { 'error': True, 'error_type':'Internal Server Error', 'error_no': 500 } ), 500)

@application.route("/")
def hello():
  return "<h1 style='color:blue'>Hello There!,,G</h1>"

@application.route('/api/camera/1', methods=['POST'])
def cam_1():
  valid = validate()
  road = valid.road(request.json['road'])
  p_name, p_forign = valid.plate(request.json['plate'])
  time_1 = valid.time(request.json['time'])
  
  sqlite = database()
  p_id = sqlite.add_plate(p_name, p_forign)
  r_id = sqlite.check_road_id(road)
    
  sqlite.record_time_1(p_id,r_id,time_1)
  #log p_id to sqlite data with r_id
  #post data should look like (in any order) '{"road":1, "plate":"YS54 GBF", "time": 1442862678}'
                                             #(road id,   number plate,      time in unix epoch)
  return jsonify({'error': False})

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
  app.run(host='0.0.0.0', port=7000,debug=False)
  
  