import sqlite3 as sql
from error import error
class database: #the database class handles anything with a database connection
  def __init__(self):
    try:
      self.rdb = None
      self.rdb = sql.connect('average_check.db')
      self.ecx = self.rdb.cursor()

    except:
      error(1,'sql connect error', True)

  def record_time(self, p_id, cam_id, s_id, uuid, time, speed): #Record the time the plate passes with the data associated
    try:
      self.ecx.execute("INSERT INTO data (p_id, cam_id, s_id, uuid, time, speed) VALUES ('"+str(p_id)+"', '"+str(cam_id)+"', '"+str(s_id)+"','"+str(uuid)+"','"+str(time)+"','"+str(speed)+"');")
      self.rdb.commit()#commit is need to properly insert the data
    except Exception as e:
      error(2,str(e)+' sql record_time() error', True)

  def find_site(self, site_id):#Find the s_id and max speed integer from site_id input string
    try:
      self.ecx.execute("select s_id, s_limit from sites where site_id = '"+str(site_id)+"' limit 1;")
      result = self.ecx.fetchone() #fetchone gets any output from sqlite
      if result == None: #if no output
          error(3,'sql find site() error (none type) - ', True)#error
      return result[0], result[1]#else return item 1 then item 2
    except Exception as e:
      error(3, str(e)+'sql find site() error', True)

  def add_plate(self, plate, foreign=False):#To add a p_id or get the existing p_id for a number plate
    try:
      foreign = str(foreign).upper() #make the bool into a upper string
      self.ecx.execute("select (1) from plates where plate = '"+plate+"' limit 1;") #check if plate exsists
      if self.ecx.fetchone() == None: #if not, enter plate
        self.ecx.execute("INSERT INTO plates (plate, p_foreign) VALUES ('"+plate+"', '"+foreign+"');")
        self.rdb.commit()#commit insert
      self.ecx.execute("select p_id from plates where plate = '"+plate+"';")#get the p_id
      return self.ecx.fetchone()[0]#Return the p_id
    except Exception as e:
       error(4,str(e)+'sql add_plate() error', True) #should be no error

  def get_cam_m(self, cam_id, s_id):#Get the meters along the road the input cam id is
    try:
      self.ecx.execute("select cam_m from cams where s_id = '"+str(s_id)+"' and cam_id = '"+str(cam_id)+"' limit 1;")
      result = self.ecx.fetchone()
      if result == None:
        error(5,'sql get_cam_m() error (no cam) - '+str(s_id)+' - '+str(cam_id), True)
      return float(result[0])
    except Exception as e:
      error(5,str(e)+'sql get_cam_m() error - '+str(result), True)

  def last_cam(self, p_id, s_id):#Find the time and id of the last cam passed by the car
    self.ecx.execute("SELECT time, cam_id FROM data where p_id = '"+str(p_id)+"' and s_id = '"+str(s_id)+"' order by d_index DESC limit 1;")
    result = self.ecx.fetchone()#fetch from sqlite
    if result == None: #
      error(8,'get last_cam error - '+str(p_id)+' - '+str(s_id)+' - '+str(result), True)
      return False
    return result[0], result[1]

  def cam_first(self, curr_cam_m, time, p_id, s_id):#Find if the cam passed is the first of this trip
    try:
      if curr_cam_m == 0: #if first cam on road
        return True
      self.ecx.execute("SELECT time FROM data where p_id = '"+str(p_id)+"' and s_id = '"+str(s_id)+"' order by d_index DESC limit 1;")
      result = self.ecx.fetchone()
      if result == None:
        #error(9,' sql cam_first() error '+str(curr_cam_m)+' '+str(time)+' '+str(p_id)+' '+str(s_id), False)
        return True
      return (result[0] < time - 3600)# if older than 1 Hour
    except Exception as e:
      error(10,str(e)+' sql cam_first() error', True)

  def record_first(self, p_id, cam_id, s_id, uuid, time):#Record the time the plate passes with the data associated, only for the first record with no speed
    try:
      self.ecx.execute("INSERT INTO data (p_id, cam_id, s_id, uuid, time) VALUES ('"+str(p_id)+"', '"+str(cam_id)+"', '"+str(s_id)+"', '"+str(uuid)+"', '"+str(time)+"')")
      self.rdb.commit()#commit insert
    except Exception as e:
      error(11,str(e)+' sql record_first_time() error '+str(p_id)+' - '+str(cam_id)+' - '+str(s_id)+' - '+str(uuid)+' - '+str(time), True)

  def return_speeders(self):#Return all data of cars over speed limit.
    try:
      self.ecx.execute("SELECT * FROM data where speed > 0 order by d_index DESC;")
      result = self.ecx.fetchall()
      return result
    except Exception as e:
      error(12,str(e)+' sql record_speeders() error', True)

  def return_foreign_speeders(self):#Return all data of foreign cars over speed limit.
    try:
      self.ecx.execute("select d_index, p.p_id, uuid, s_id, time, cam_id, speed from data as d, plates as p where d.speed > 0 and p_foreign = 'TRUE' and p.p_id=d.p_id;")
      result = self.ecx.fetchall()
      return result
    except Exception as e:
      error(13,str(e)+' sql record_speeders() error', True)

  def get_cam_id(self, site_cam_id, s_id):#Get the actual cam_id relative to the program rather than the cam_id relative to the site id
    try:
      self.ecx.execute("SELECT cam_id FROM cams where site_cam_id = '"+str(site_cam_id)+"' and s_id = '"+str(s_id)+"' LIMIT 1;")
      result = self.ecx.fetchone()
      if result == None:
        error(14,' sql get_cam_id() error '+str(site_cam_id)+' '+str(s_id), True)
        return None
      return result[0]
    except Exception as e:
      error(14,str(e)+' sql get_cam_id() error', True)

  def get_plate(self, p_id):#Get the plate string from the p_id
    try:
      self.ecx.execute("SELECT plate FROM plates where p_id = '"+str(p_id)+"' LIMIT 1;")
      result = self.ecx.fetchone()
      if result == None:
        error(15,' sql get_plate() error '+str(p_id), False)
        return None
      return result[0]
    except Exception as e:
      error(16,str(e)+' sql get_plate() error', True)

  def get_site(self, s_id):#Get the site string from the s_id
    try:
      self.ecx.execute("SELECT site_id, s_limit FROM sites where s_id = '"+str(s_id)+"' LIMIT 1;")
      result = self.ecx.fetchone()
      if result == None:
        error(17,' sql get_site() error '+str(s_id), False)
        return None
      return result[0], result[1]
    except Exception as e:
      error(17,str(e)+' sql get_site() error', True)

  def get_owner(self, p_id):#Get the owner info string from the p_id
    try:
      self.ecx.execute("select * from owners where p_id= '"+str(p_id)+"' LIMIT 1;")
      result = self.ecx.fetchone()
      if result == None:
        return None
      return result[1], result[2]
    except Exception as e:
      error(18,str(e)+' sql get_owner() error', True)
