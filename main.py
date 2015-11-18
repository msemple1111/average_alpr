#!/bin/python
import json
from bottle import route, run, request
import re
import sqlite3 as sql

def error(err_no, err_desc, end):
  error_dec = "Error no: " + str(err_no) + "  " + err_desc + "\n"
  with open('log.txt', 'a') as afile:
    afile.write(error_dec)
  
  if end:
    raise SystemExit('Program Ended With Exit Code [1]')
    
class calculate:
  def average_speed(self, time_1, time_2): #returns average speed in m/s after two time inputs
    time = time_1 - time_2
  
class database: #the database class is anything with a database connection
  def __init__(self):
    try:
      self.rdb = None
      self.rdb = sql.connect('average_check_test.db')
      self.ecx = self.rdb.cursor()    
    except:
      error(2,'sql connect error', True)
  
  def add_plate(self, plate, foreign=False):
    try:
      foreign = str(foreign)
      self.ecx.execute("select (1) from plates where plate = '"+plate+"' limit 1;")
      if str(self.ecx.fetchone()) == "None":
        self.ecx.execute("INSERT INTO plates (plate, p_foreign) VALUES ('"+plate+"', '"+foreign+"');")
        self.rdb.commit()
      self.ecx.execute("select p_index from plates where plate = '"+plate+"';")
      return self.ecx.fetchone()[0]
    except:
       error(3,'sql check_plates() error', True)

  def check_road_index(self, road):
    try:
      self.ecx.execute("select (1) from roads where r_index = '"+road+"' limit 1;")
      if str(self.ecx.fetchone()) == "None":
        return False
      return True
    except:
       error(4,'sql check_road_index() error', True)
        
  #def 

  
class validate: #the validate class is pre vaidating every input
  def plate(self, plate):
    try:
      self.plate = plate.replace(" ", "")
      plate_valid = re.compile("([A-Z]{2}[0-9]{2}[A-Z]{3}$)|([A-Z][0-9]{1,3}[A-Z]{3}$)|([A-Z]{3}[0-9]{1,3}[A-Z]$)|([0-9]{1,4}[A-Z]{1,2}$)|([0-9]{1,3}[A-Z]{1,3}$)|([A-Z]{1,2}[0-9]{1,4}$)|([A-Z]{1,3}[0-9]{1,3}$)") #https://gist.github.com/danielrbradley/7567269
      f_plate_valid = re.compile("^[a-zA-Z.\d]{1,13}$")
      if plate_valid.match(self.plate):
        return "British"
      elif f_plate_valid.match(self.plate):
        return "Foreign"
      else:
        return False
    except:
       error(6,'sql valid.plate() error', False)
        
  def road(self, road):
    try:
      is_int = int(road)
      return True
    except:
      error(7, 'vaild.road() error', False)
      return False
    
  def time(self, time):
    try:
      is_int = int(time)
      return True
    except:
      error(8, 'vaild.time() error', False)
      return False
      
      

#valid = validate()
#print(valid.road('1'))
#if __name__ == '__main__':
  #sqli = database()
  #print(sqli.get_plate_index(1))
  #valid = validate()
  #print(valid.road('1'))

