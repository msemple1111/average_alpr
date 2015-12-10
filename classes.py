#!/bin/python
import json
#from webserver import http_error
import re
import sqlite3 as sql
from uuid import UUID

def http_error(no):
  one=1
def error(err_no, err_desc, end):
  import datetime
  error_dec = "Time: "+str(datetime.datetime.now())+" Error no: " + str(err_no) + "  " + err_desc + "\n"
  with open('log.txt', 'a') as afile:
    afile.write(error_dec)
  http_error(500)
  
  if end:
    raise SystemExit('Program Ended With Exit Code [1]')
    
class calculate:
  def average_speed(self, time_1, time_2, dist): #returns average speed in m/s after two time inputs
    time = time_2 - time_1 #find the time
    return dist/time #return speed = distance / time
  
  def speed_increase(self, car_speed, road_speed):
    return car_speed - road_speed #return speed relative to speed limit in m/s 
  
class database: #the database class is anything with a database connection
  def __init__(self):
    try:
      self.rdb = None
      self.rdb = sql.connect('average_check.db')
      self.ecx = self.rdb.cursor()    
      self.ecx.execute("PRAGMA synchronous = OFF")
      self.ecx.execute("PRAGMA journal_mode = MEMORY")
      self.ecx.execute("PRAGMA page_size = 4096")
      self.ecx.execute("PRAGMA locking_mode = EXCLUSIVE")
      self.ecx.execute("PRAGMA temp_store = MEMORY")
      self.ecx.execute("PRAGMA count_changes = OFF;")

    except:
      error(2,'sql connect error', True)
  
  def record_time(self, cam_id, p_id, site_id, uuid, time):
    try:
      self.ecx.execute("INSERT INTO data (p_id, cam_id, site_id, uuid, time) VALUES ('"+str(p_index)+"', '"+str(r_id)+"', '"+str(time_1)+"');")
      self.rdb.commit()
    except Exception as e:
      error(3,str(e)+' sql record_time_1() error', False)
    
  
  def find_site(self, site_id):
    try:
      foreign = str(foreign)
      self.ecx.execute("select s_id, s_limit from sites where site_id = '"+site_id+"' limit 1;")
      return self.ecx.fetchone()[0], self.ecx.fetchone()[1]
    except Exception as e:
       error(4,str(e)+'sql check_plates() error', True)
        
  def add_plate(self, plate, foreign=False):
    try:
      foreign = str(foreign)
      self.ecx.execute("select (1) from plates where plate = '"+plate+"' limit 1;")
      if str(self.ecx.fetchone()) == "None":
        self.ecx.execute("INSERT INTO plates (plate, p_foreign) VALUES ('"+plate+"', '"+foreign+"');")
        self.rdb.commit()
      self.ecx.execute("select p_index from plates where plate = '"+plate+"';")
      return self.ecx.fetchone()[0]
    except Exception as e:
       error(4,str(e)+'sql check_plates() error', True)

  def check_road_id(self, road):
    #try:
    self.ecx.execute("select (1) from roads where r_id = '"+str(road)+"' limit 1;")
    if str(self.ecx.fetchone()) == "None":
      error(5,'sql check_road_id() error (no road)', True)
    return road
    #except Exception as e:
    #   error(6,str(e)+' sql check_road_id() error', True)
    
  def get_d_index(self, p_index, road):
    self.ecx.execute("SELECT d_index FROM data where p_index = '"+str(p_index)+"' and r_id = '"+str(road)+"' order by time_1 DESC limit 1;")
    return self.ecx.fetchone()
    #if fetch == None:
    #  http_error(404)
    #  error(6,'get d_index error', False)
    #  return -1
    #return fetch[0]

  def get_time_1(self, p_index, road):
    self.ecx.execute("SELECT time_1 FROM data where p_index = '"+str(p_index)+"' and r_id = '"+str(road)+"' order by time_1 DESC limit 1;")
    fetch = self.ecx.fetchone()
    if fetch == None:
      error(7,'get time_1 error', False)
      return -1
    return fetch[0]
  
  def get_s_limit(self, r_id):
    self.ecx.execute("select s_limit from roads where r_id = '"+str(r_id)+"';")
    fetch = self.ecx.fetchone()
    if fetch == None:
      error(8,'get s_limit error', False)
      return -1
    return fetch[0]
  
  def get_r_dist(self, r_id):
    self.ecx.execute("select r_dist from roads where r_id = '"+str(r_id)+"';")
    fetch = self.ecx.fetchone()
    if fetch == None:
      error(9,'get r_dist error', False)
      return -1
    return fetch[0]
  
  def record_time_2(self, d_index, time_2, speed):
    try:
      self.ecx.execute(" UPDATE data SET time_2 = '"+str(time_2)+"', speed = '"+str(speed)+"' WHERE d_index = '"+str(d_index)+"';")
      self.rdb.commit()
    except Exception as e:
      error(10,str(e)+' sql record_time_2() error', False)
    
  
class validate: #the validate class is pre vaidating every input
  def plate(self, plate):
    try:
      self.plate = plate.replace(" ", "")
      plate_valid = re.compile("([A-Z]{2}[0-9]{2}[A-Z]{3}$)|([A-Z][0-9]{1,3}[A-Z]{3}$)|([A-Z]{3}[0-9]{1,3}[A-Z]$)|([0-9]{1,4}[A-Z]{1,2}$)|([0-9]{1,3}[A-Z]{1,3}$)|([A-Z]{1,2}[0-9]{1,4}$)|([A-Z]{1,3}[0-9]{1,3}$)") #https://gist.github.com/danielrbradley/7567269
      f_plate_valid = re.compile("^[a-zA-Z.\d]{1,13}$")
      if plate_valid.match(self.plate):
        return plate, False
      
      elif f_plate_valid.match(self.plate):
        return plate, True
      
      else:
        return None, None
    except:
      error(11,'valid.plate() error', False)
      return None
        
  def site(self, site):
    try:
      site_is_str = str(site)
      return site_is_str
    except Exception as e:
      error(12, str(e)+' vaild.site() error', False)
      return None
    
  def time(self, time):
    try:
      time_is_int = int(time)
      return time_is_int
    except Exception as e:
      error(13, str(e)+' vaild.time() error', False)
      return False
    
  def confidence(self, confidence):
    try:
      confidence_is_float = float(confidence)
      if 0 < confidence_is_float <= 100:
        return confidence_is_float
    except Exception as e:
      error(14, str(e)+' vaild.confidence() error', False)
      return False
    
  def cam(self, cam):
    try:
      cam_is_int = int(cam)
      return cam_is_int
    except Exception as e:
      error(15, str(e)+' vaild.cam() error', False)
      return False

def uuid(self, uuid): #https://gist.github.com/ShawnMilo/7777304
    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        # If it's a value error, then the string 
        # is not a valid hex code for a UUID.
        error(15, str(e)+' vaild.cam() error', False)
        return False

    # If the uuid_string is a valid hex code, 
    # but an invalid uuid4,
    # the UUID.__init__ will convert it to a 
    # valid uuid4.

    return uuid
      
      

#valid = validate()
#print(valid.road('1'))
#if __name__ == '__main__':
#  sqli = database()
#  print(sqli.get_d_index(26, 2))
#  sqli.record_time_1(28,1,1449999991)

  #print(sqli.get_plate_index(1))
  #valid = validate()
  #print(valid.road('1'))

