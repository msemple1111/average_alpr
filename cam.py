from validate import validate
from database import database
from calculate import calculate
class cam: # the cam class is the controlling class that takes the input and processes it
  def __init__(self, request_data):
    self.request_data = request_data
    self.valid = validate()
    site_id = self.valid.site(request_data['site_id'])
    self.site_cam_id = self.valid.cam(request_data['camera_id'])
    self.uuid = self.valid.uuid(request_data['uuid'])
    self.time_2 = self.valid.time(request_data['epoch_time'])
    self.sqlite = database()
    self.calc = calculate()
    self.s_id, self.s_limit = self.sqlite.find_site(site_id)
    self.cam_id = self.sqlite.get_cam_id(self.site_cam_id, self.s_id)
    self.curr_cam_m = self.sqlite.get_cam_m(self.cam_id, self.s_id)
    for plate_no in range(0,len(self.request_data['results'])):
      self.plate(plate_no)

  def plate(self, plate_no):
    plate, p_foreign = self.valid.plate(self.request_data['results'][plate_no]['plate'])
    p_confidence = self.valid.confidence(self.request_data['results'][plate_no]['confidence'])
    p_id = self.sqlite.add_plate(plate, p_foreign)#
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
