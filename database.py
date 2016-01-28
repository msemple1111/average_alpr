import sqlite3 as sql
from error import error
class database: #the database class handles anything with a database connection
  def __init__(self):
    try:
      self.rdb = None
      self.rdb = sql.connect('average_check_test.db')
      self.ecx = self.rdb.cursor()

    except:
      error(1,'sql connect error', True)

  def record_time(self, p_id, cam_id, s_id, uuid, time, speed):
    try:
      self.ecx.execute("INSERT INTO data (p_id, cam_id, s_id, uuid, time, speed) VALUES ('"+str(p_id)+"', '"+str(cam_id)+"', '"+str(s_id)+"','"+str(uuid)+"','"+str(time)+"','"+str(speed)+"');")
      self.rdb.commit()
    except Exception as e:
      error(2,str(e)+' sql record_time() error', True)


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

  def get_s_limit(self, s_id):
    self.ecx.execute("select s_limit from sites where s_id = '"+str(s_id)+"';")
    fetch = self.ecx.fetchone()
    if fetch == None:
      error(7,'get s_limit error', True)
      return -1
    return fetch[0]

  def last_cam(self, p_id, s_id):
    self.ecx.execute("SELECT time, cam_id FROM data where p_id = '"+str(p_id)+"' and s_id = '"+str(s_id)+"' order by d_index DESC limit 1;")
    result = self.ecx.fetchone()
    if result == None:
      error(8,'get last_cam error - '+str(p_id)+' - '+str(s_id)+' - '+str(result), False)
      return -1
    return result[0], result[1]

  def cam_first(self, curr_cam_m, time, p_id, s_id):
    try:
      if curr_cam_m == 0:
        return True
      self.ecx.execute("SELECT time FROM data where p_id = '"+str(p_id)+"' and s_id = '"+str(s_id)+"' order by d_index DESC limit 1;")
      result = self.ecx.fetchone()
      if result == None:
        return True
      return (result[0] < time - 3600)# if older than 1 Hour
    except Exception as e:
      error(9,str(e)+' sql cam_first() error', True)

  def record_first(self, p_id, cam_id, s_id, uuid, time):
    try:
      self.ecx.execute("INSERT INTO data (p_id, cam_id, s_id, uuid, time) VALUES ('"+str(p_id)+"', '"+str(cam_id)+"', '"+str(s_id)+"', '"+str(uuid)+"', '"+str(time)+"')")
      self.rdb.commit()
    except Exception as e:
      error(10,str(e)+' sql record_first_time() error '+str(p_id)+' - '+str(cam_id)+' - '+str(s_id)+' - '+str(uuid)+' - '+str(time), True)

  def return_speeders(self):
    try:
      self.ecx.execute("")
      result = self.ecx.fetchone("SELECT * FROM data where speed > 0 order by d_index DESC;")
      return result

    except:
      error(11,str(e)+' sql record_speeders() error', True)
