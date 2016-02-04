import json
import re
import uuid
from error import error
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
      error(31,'valid.plate() error', True)
      return None

  def site(self, site):
    try:
      site_is_str = str(site)
      return site_is_str.lower()
    except Exception as e:
      error(32, str(e)+' vaild.site() error', True)
      return None

  def time(self, time):
    try:
      time_is_int = int(time)
      return time_is_int
    except Exception as e:
      error(33, str(e)+' vaild.time() error', True)
      return False

  def confidence(self, confidence):
    try:
      confidence_is_float = float(confidence)
      if 0 < confidence_is_float <= 100:
        return confidence_is_float
    except Exception as e:
      error(34, str(e)+' vaild.confidence() error', True)
      return False

  def cam(self, cam):
    try:
      cam_is_int = int(cam)
      return cam_is_int
    except Exception as e:
      error(35, str(e)+' vaild.cam() error', True)
      return False

  def uuid(self, uuid_string): #https://gist.github.com/ShawnMilo/7777304
    try:
        val = uuid.UUID(uuid_string, version=4)
    except ValueError:
        # If it's a value error, then the string
        # is not a valid hex code for a UUID.
        error(36, str(e)+' vaild.cam() error', True)
        return False

    # If the uuid_string is a valid hex code,
    # but an invalid uuid4,
    # the UUID.__init__ will convert it to a
    # valid uuid4.

    return val
