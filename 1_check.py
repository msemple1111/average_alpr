#!/bin/python
import json
import re
from bottle import route, run, request
import sqlite3 as sql
def error(err_no, err_desc):
  error = str(err_no) + err_desc
  with open('log.txt', 'a') as afile:
    afile.write(error)
  print(error)
    
class database:
  def __init__(self):
    #try:
    self.rdb = None
    self.rdb = sql.connect('average_check_test.db')
    self.ecx = self.rdb.cursor()    
    #except:
    #  error(2,'sql connect error')
  
  def check_plate(self, plate):
    self.ecx.execute("select (1) from plates where plate = '"+plate+"' limit 1;")
    if str(self.ecx.fetchone()) == "None":
      return False
    return True
  
  def get_plate_index(self, plate):
    self.ecx.execute("select p_index from plates where plate = '"+plate+"';") 
    return self.ecx.fetchone()
  
class validate:
  def plate(self, plate):
    self.plate = plate.replace(" ", "")
    self.plate_valid = re.compile("([A-Z]{2}[0-9]{2}[A-Z]{3}$)|([A-Z][0-9]{1,3}[A-Z]{3}$)|([A-Z]{3}[0-9]{1,3}[A-Z]$)|([0-9]{1,4}[A-Z]{1,2}$)|([0-9]{1,3}[A-Z]{1,3}$)|([A-Z]{1,2}[0-9]{1,4}$)|([A-Z]{1,3}[0-9]{1,3}$)") #https://gist.github.com/danielrbradley/7567269
    self.f_plate_valid = re.compile("^[a-zA-Z.\d]{1,13}$")
    if self.plate_valid.match(self.plate):
      return "British"
    elif self.f_plate_valid.match(self.plate):
      return "Forign"
    else:
      return False
    
  def road(self, road):
    try:
      is_int = int(road)
      return True
    except:
      return False
    
  def time(self, time):
    try:
      is_epoch = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    except:
      print('no no')
      
@route('/api/camera/1', method='POST')
def camera_1():
  #post data should look like (in any order) '{"road":1, "plate":"YS54 GBF","time": 1442862678}'
  #                                           (road id,   number plate,      time in unix epoch)
  rawpostdata = request.body.read()
  try:
    postdata = json.loads(rawpostdata.decode()) #had to decode cause of problem https://stackoverflow.com/questions/24069197/httpresponse-object-json-object-must-be-str-not-bytes
    plate = postdata['plate']
    road = postdata['road']
    time = postdata['time']
  except:
    return '{"error":"True", "err_id": 1}'
  plate_validate = re.compile("([A-Z]{2}[0-9]{2}[A-Z]{3}$)|[A-Z][0-9]{1,3}[A-Z]{3}$)|([A-Z]{3}[0-9]{1,3}[A-Z]$)|([0-9]{1,4}[A-Z]{1,2}$)|([0-9]{1,3}[A-Z]{1,3}$)|([A-Z]{1,2}[0-9]{1,4}$)|([A-Z]{1,3}[0-9]{1,3}$)") #https://gist.github.com/danielrbradley/7567269
  
  if plate_validate.match(plate):
    if rdb.execute("select (1) from plates where plate = '"+plate+"' limit 1;"): 
      lol = str(rdb.execute("select p_index from plates where plate = 'YS54 GBF';"))
      return lol
    else:
      return '{"error":"True","stored":"False1"}'+plate
  else:
    return '{"error":"True","stored":"False"}'
  
valid = validate()
print(valid.road('1'))
#sqli = database()
#print(sqli.check_plate('KU46KRQ'))
#run(host='0.0.0.0', port=8080)

'''
#/\b[a-z]{2}([1-9]|0[2-9]|6[0-9]|1[0-9])[a-z]{3}\b/i      # current series
#/\b[A-HJ-NP-Y]\d{1,3}[A-Z]{3}\b/        # previous series
#/\b[A-Z]{3}\d{1,3}[A-HJ-NP-Y]\b/        # previous series
#/\b(?:[A-Z]{1,2}\d{1,4}|[A-Z]{3}\d{1,3})\b/     # old series - letters first
#/\b(?:\d{1,4}[A-Z]{1,2}|\d{1,3}[A-Z]{3})\b/     # old series - digits first
'''