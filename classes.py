#!/bin/python
import json
#from webserver import http_error
import re
import sqlite3 as sql
import uuid

def http_error(no):
  one=1
def error(err_no, err_desc, end):
  import datetime
  error_dec = "Time: "+str(datetime.datetime.now())+" Error no: " + str(err_no) + "  " + err_desc + "\n"
  with open('log.txt', 'a') as afile:
    afile.write(error_dec)
  http_error(500)
  #if end:
   # raise SystemExit('Program Ended With Exit Code [1]')
    
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
      self.rdb = sql.connect('average_check_test.db')
      self.ecx = self.rdb.cursor()    
      #self.ecx.execute("PRAGMA synchronous = OFF")
      #self.ecx.execute("PRAGMA journal_mode = MEMORY")
      #self.ecx.execute("PRAGMA page_size = 4096")
      #self.ecx.execute("PRAGMA locking_mode = EXCLUSIVE")
      #self.ecx.execute("PRAGMA temp_store = MEMORY")
      #self.ecx.execute("PRAGMA count_changes = OFF;")

    except:
      error(2,'sql connect error', True)
  
  def record_time(self, p_id, cam_id, s_id, uuid, time, speed):
    try:
      self.ecx.execute("INSERT INTO data (p_id, cam_id, s_id, uuid, time, speed) VALUES ('"+str(p_id)+"', '"+str(cam_id)+"', '"+str(s_id)+"','"+str(uuid)+"','"+str(time)+"','"+str(speed)+"');")
      self.rdb.commit()
    except Exception as e:
      error(2,str(e)+' sql record_time() error', False)
    
  
  def find_site(self, site_id):
    try:
      self.ecx.execute("select s_id, s_limit from sites where site_id = '"+str(site_id)+"' limit 1;")
      result = self.ecx.fetchone()
      return result[0], result[1]
    except Exception as e:
       error(3, str(e)+'sql find site() error', True)
        
  def add_plate(self, plate, foreign=False):
    try:
      foreign = str(foreign)
      self.ecx.execute("select (1) from plates where plate = '"+plate+"' limit 1;")
      if self.ecx.fetchone() == None:
        self.ecx.execute("INSERT INTO plates (plate, p_foreign) VALUES ('"+plate+"', '"+foreign+"');")
        self.rdb.commit()
      self.ecx.execute("select p_id from plates where plate = '"+plate+"';")
      return self.ecx.fetchone()[0]
    except Exception as e:
       error(4,str(e)+'sql add_plate() error', True)

  def get_cam_m(self, cam_id, s_id):
    try:
      self.ecx.execute("select cam_m from cams where s_id = '"+str(s_id)+"' and cam_id = '"+str(cam_id)+"' limit 1;")
      result = self.ecx.fetchone()
      if result == None:
        error(5,'sql get_cam_m() error (no cam) - '+str(s_id)+' - '+str(cam_id), False)
      return float(result[0])
    except Exception as e:
      error(5,str(e)+'sql get_cam_m() error - '+str(result), True)

#   def get_d_index(self, p_index, road):
#     self.ecx.execute("SELECT d_index FROM data where p_index = '"+str(p_index)+"' and r_id = '"+str(road)+"' order by time_1 DESC limit 1;")
#     return self.ecx.fetchone()
#     #if fetch == None:
#     #  http_error(404)
#     #  error(6,'get d_index error', False)
#     #  return -1
#     #return fetch[0]



#   def get_time_1(self, p_index, road):
#     self.ecx.execute("SELECT time_1 FROM data where p_index = '"+str(p_index)+"' and r_id = '"+str(road)+"' order by time_1 DESC limit 1;")
#     fetch = self.ecx.fetchone()
#     if fetch == None:
#       error(7,'get time_1 error', False)
#       return -1
#     return fetch[0]

  def get_s_limit(self, s_id):
    self.ecx.execute("select s_limit from sites where s_id = '"+str(s_id)+"';")
    fetch = self.ecx.fetchone()
    if fetch == None:
      error(7,'get s_limit error', False)
      return -1
    return fetch[0]
  
  def last_cam(self, p_id, s_id):
    self.ecx.execute("SELECT time, cam_id FROM data where p_id = '"+str(p_id)+"' and s_id = '"+str(s_id)+"' order by d_index DESC limit 1;")
    result = self.ecx.fetchone()
    if result == None:
      error(8,'get last_cam error - '+str(p_id)+' - '+str(s_id)+' - '+str(result), False)
      return -1
    return result[0], result[1]
  
#   def get_r_dist(self, r_id):
#     self.ecx.execute("select r_dist from roads where r_id = '"+str(r_id)+"';")
#     fetch = self.ecx.fetchone()
#     if fetch == None:
#       error(9,'get r_dist error', False)
#       return -1
#     return fetch[0]

  def cam_first(self, curr_cam_m, time, p_id, s_id):
    if curr_cam_m == 0:
      return True
    self.ecx.execute("SELECT time FROM data where p_id = '"+str(p_id)+"' and s_id = '"+str(s_id)+"' order by d_index DESC limit 1;")
    result = self.ecx.fetchone()
    if result == None:
      return True
    return (result[0] < time - 3600)# if older than 1 Hour
  
#   def record_time_2(self, d_index, time_2, speed):
#     try:
#       self.ecx.execute(" UPDATE data SET time_2 = '"+str(time_2)+"', speed = '"+str(speed)+"' WHERE d_index = '"+str(d_index)+"';")
#       self.rdb.commit()
#     except Exception as e:
#       error(10,str(e)+' sql record_time_2() error', False)
  def record_first(self, p_id, cam_id, s_id, uuid, time):
    try:
      self.ecx.execute("INSERT INTO data (p_id, cam_id, s_id, uuid, time) VALUES ('"+str(p_id)+"', '"+str(cam_id)+"', '"+str(s_id)+"', '"+str(uuid)+"', '"+str(time)+"')")
      self.rdb.commit()
    except Exception as e:
      error(10,str(e)+' sql record_first_time() error '+str(p_id)+' - '+str(cam_id)+' - '+str(s_id)+' - '+str(uuid)+' - '+str(time), False)
      
    
  
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

  def uuid(self, uuid_string): #https://gist.github.com/ShawnMilo/7777304
    try:
        val = uuid.UUID(uuid_string, version=4)
    except ValueError:
        # If it's a value error, then the string 
        # is not a valid hex code for a UUID.
        error(15, str(e)+' vaild.cam() error', False)
        return False

    # If the uuid_string is a valid hex code, 
    # but an invalid uuid4,
    # the UUID.__init__ will convert it to a 
    # valid uuid4.

    return uuid_string
      
      
class cam:
  def __init__(self, request_data):
    self.request_data = request_data
    self.valid = validate()
    site_id = self.valid.site(request_data['site_id'])
    self.cam_id = self.valid.cam(request_data['camera_id'])
    self.uuid = self.valid.uuid(request_data['uuid'])
    self.time_2 = self.valid.time(request_data['epoch_time'])
    self.sqlite = database()
    self.calc = calculate()
    self.s_id, self.s_limit = self.sqlite.find_site(site_id)
    self.curr_cam_m = self.sqlite.get_cam_m(self.cam_id, self.s_id)
    for plate_no in range(0,len(self.request_data['results'])):
      self.plate(plate_no)
    
  def plate(self, plate_no):
    plate, p_forign = self.valid.plate(self.request_data['results'][plate_no]['plate'])
    p_confidence = self.valid.confidence(self.request_data['results'][plate_no]['confidence'])
    p_id = self.sqlite.add_plate(plate, p_forign)#
    cam_first = self.sqlite.cam_first(self.curr_cam_m, self.time_2, p_id, self.s_id)
    if cam_first:
      self.sqlite.record_first(p_id, self.cam_id, self.s_id, self.uuid, self.time_2)
    else:
      time_1, prev_cam_id = self.sqlite.last_cam(p_id, self.s_id)#
      prev_cam_m = self.sqlite.get_cam_m(prev_cam_id, self.s_id)
      r_dist = prev_cam_m - self.curr_cam_m
      car_speed = self.calc.average_speed(self.time_2, time_1, r_dist)
      speed = self.calc.speed_increase(car_speed, self.s_limit)
      self.sqlite.record_time(p_id, self.cam_id, self.s_id, self.uuid, self.time_2, speed)#
      
#valid = validate()
#print(valid.road('1'))
# if __name__ == '__main__':
#   calc = calculate()
#   time_1 = 1449866925
#   time_2 = 1449866926
#   dist = 250
#   road_speed = 15
#   car_speed = calc.average_speed(time_1, time_2, dist) #returns average speed in m/s after two time inputs
#   increase = calc.speed_increase(car_speed, road_speed)
#   print(increase)
#  sqli = database()
#  print(sqli.get_d_index(26, 2))
#  sqli.record_time_1(28,1,1449999991)

  #print(sqli.get_plate_index(1))
  #valid = validate()
  #print(valid.road('1'))

