#!/bin/python
import json
import re
from bottle import route, run, request


@route('/api/camera/1', method='POST')
def camera_1():
  #post data should look like '{"plate":"YS54 GBF","time": 1442862678}'
  rawpostdata = request.body.read()
  try:
    postdata = json.loads(rawpostdata.decode()) #had to decode cause of problem https://stackoverflow.com/questions/24069197/httpresponse-object-json-object-must-be-str-not-bytes
  except:
    return '{"error":"True"}'
  postdata['plate'].replace(" ", "")
  plate_1 = re.compile("[A-Z]{2}[0-9]{2}[A-Z]{3}") #https://gist.github.com/danielrbradley/7567269
  plate_2 = re.compile("[A-Z][0-9]{1,3}[A-Z]{3}")
  plate_3 = re.compile("[A-Z]{3}[0-9]{1,3}[A-Z]")
  plate_4 = re.compile("[0-9]{1,4}[A-Z]{1,2}")
  plate_5 = re.compile("[0-9]{1,3}[A-Z]{1,3}")
  plate_6 = re.compile("[A-Z]{1,2}[0-9]{1,4}")
  plate_7 = re.compile("[A-Z]{1,3}[0-9]{1,3}")
  if plate_1.match(postdata['plate']) or plate_2.match(postdata['plate']) or plate_3.match(postdata['plate']) or plate_4.match(postdata['plate']) or plate_5.match(postdata['plate']) or plate_6.match(postdata['plate']) or plate_7.match(postdata['plate']):
    return '{"error":"False","stored":"True"}'
  else:
    return '{"error":"True","stored":"False"}'
run(host='0.0.0.0', port=8080)

'''
#/\b[a-z]{2}([1-9]|0[2-9]|6[0-9]|1[0-9])[a-z]{3}\b/i      # current series
#/\b[A-HJ-NP-Y]\d{1,3}[A-Z]{3}\b/        # previous series
#/\b[A-Z]{3}\d{1,3}[A-HJ-NP-Y]\b/        # previous series
#/\b(?:[A-Z]{1,2}\d{1,4}|[A-Z]{3}\d{1,3})\b/     # old series - letters first
#/\b(?:\d{1,4}[A-Z]{1,2}|\d{1,3}[A-Z]{3})\b/     # old series - digits first
'''