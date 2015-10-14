#!/bin/python
import json
import re
from bottle import route, run, request
import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user="average_check", passwd="x9ojrs74VXCwapEmJ88XXIEg5", db="average_check") #http://ianhowson.com/a-quick-guide-to-using-mysql-in-python.html
rdb = db.cursor()

@route('/api/camera/1', method='POST')
def camera_1():
  #post data should look like '{"plate":"YS54 GBF","time": 1442862678}'
  rawpostdata = request.body.read()
  try:
    postdata = json.loads(rawpostdata.decode()) #had to decode cause of problem https://stackoverflow.com/questions/24069197/httpresponse-object-json-object-must-be-str-not-bytes
    plate = postdata['plate']
  except:
    return '{"error":"True"}'
  re_plate[1] = re.compile("[A-Z]{2}[0-9]{2}[A-Z]{3}") #https://gist.github.com/danielrbradley/7567269
  re_plate[2] = re.compile("[A-Z][0-9]{1,3}[A-Z]{3}")
  re_plate[3] = re.compile("[A-Z]{3}[0-9]{1,3}[A-Z]")
  re_plate[4] = re.compile("[0-9]{1,4}[A-Z]{1,2}")
  re_plate[5] = re.compile("[0-9]{1,3}[A-Z]{1,3}")
  re_plate[6] = re.compile("[A-Z]{1,2}[0-9]{1,4}")
  re_plate[7] = re.compile("[A-Z]{1,3}[0-9]{1,3}")
  
  if re_plate[1].match(plate) or re_plate[2].match(plate) or re_plate[3].match(plate) or re_plate[4].match(plate) or re_plate[5].match(plate) or re_plate[6].match(plate) or re_plate[7].match(plate):
    if rdb.execute("select (1) from plates where plate = '"+plate+"' limit 1;"): 
      lol = str(rdb.execute("select p_index from plates where plate = 'YS54 GBF';"))
      return lol
    else:
      return '{"error":"True","stored":"False1"}'+plate
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