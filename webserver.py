from main import *

#!flask/bin/python
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)

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
  return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
# return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.errorhandler(400)
def not_found(error):
  return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/api/camera/1', methods=['POST'])
def cam_1():
  road, plate, time = valid.postdata(request.body.read())
  data = {
    'road': request.json['road'],
    'plate': valid.postdata_plate(request.json['plate']),
    'description': request.json.get('description', ""),
     'done': False
  }
  #post data should look like (in any order) '{"road":1, "plate":"YS54 GBF", "time": 1442862678}'
                                             #(road id,   number plate,      time in unix epoch)
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=7000,debug=True)

from bottle import route, run, request
@route('/api/camera/1', method='POST')
def cam_1():
    #post data should look like (in any order) '{"road":1, "plate":"YS54 GBF","time": 1442862678}'
    #                                           (road id,   number plate,      time in unix epoch)
    
    road, plate, time = valid.postdata(request.body.read())
    return request.body.read()
    #return str(road),'\n', plate,'\n', str(time), '\n'

    
run(host='0.0.0.0', port=7000)