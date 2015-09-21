#!/bin/python
import json
from bottle import route, run, request


@route('/api/camera/1', method='POST')
def camera_1():
  #post data should look like '{"plate":"YS54 GBF","time": 1442862678}'
  try:
    postdata = json.loads(request.body.read())
  except ValueError:
    return '{"error":"True"}'
  if re.match("/\b[a-z]{2}([1-9]|0[2-9]|6[0-9]|1[0-9])[a-z]{3}\b/i ", postdata[plate], flags=0):
    return '{"error":"False","stored":"true"}'
run(host='0.0.0.0', port=8080)

/\b[a-z]{2}([1-9]|0[2-9]|6[0-9]|1[0-9])[a-z]{3}\b/i      # current series
/\b[A-HJ-NP-Y]\d{1,3}[A-Z]{3}\b/        # previous series
/\b[A-Z]{3}\d{1,3}[A-HJ-NP-Y]\b/        # previous series
/\b(?:[A-Z]{1,2}\d{1,4}|[A-Z]{3}\d{1,3})\b/     # old series - letters first
/\b(?:\d{1,4}[A-Z]{1,2}|\d{1,3}[A-Z]{3})\b/     # old series - digits first