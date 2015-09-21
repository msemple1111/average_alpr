#!/bin/python
import json
from bottle import route, run, request


@route('/api/average_speed', method='POST')
def average_speed():
  postdata = request.body.read()
   return 

run(host='0.0.0.0', port=8080)