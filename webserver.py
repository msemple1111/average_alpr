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
def main():
  start = cam(request.json)
  return json.dumps({'error': False})
  
if __name__ == '__main__':
  application.run(host='0.0.0.0', port=7000, debug=True)
