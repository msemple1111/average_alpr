import json
import re
import uuid
from error import error
class validate: #the validate class is pre vaidating every input
  def plate(self, plate):
    try:#validate the plate against known plate patterns
      plate_out = plate.replace(" ", "").upper()#take out spaces and convert all leters to uppercase
      plate_valid = re.compile("([A-Z]{2}[0-9]{2}[A-Z]{3}$)") #uk plate regex pattern
      #validate foreign plates- asume no characters and only numbers and letters
      f_plate_valid = re.compile("^[a-zA-Z.\d]{1,13}$")
      if plate_valid.match(plate_out): #if british
        return plate.upper(), False #return plate all uppercase and with no foreign tag
      elif f_plate_valid.match(plate_out): #if foreign
        return plate, True #return plate how it came, with foreign tag
      else: #return none type, because plate matched no rules
        return None, None
    except:
      error(31,'valid.plate() error', False)
      return None

  def site(self, site):
    try:
      site_is_str = str(site) #check site name is a string
      return site_is_str.lower() #make is lowercase for consistancy
    except Exception as e:
      error(32, str(e)+' vaild.site() error', False)
      return None

  def time(self, time):
    try:
      time_is_int = int(time)#check time is an interger
      return time_is_int #return the interger
    except Exception as e:
      error(33, str(e)+' vaild.time() error', False)
      return None

  def confidence(self, confidence):
    try:
      confidence_is_float = float(confidence) #check confidence is a real number
      if 0 < confidence_is_float <= 100: #check confidence is a number between 0.1 and 100
        return confidence_is_float #return float
      else:
        return None
    except Exception as e:
      error(34, str(e)+' vaild.confidence() error', False)
      return None

  def cam(self, cam):
    try:
      cam_is_int = int(cam) #check cam_id is an interger
      return cam_is_int #return interger
    except Exception as e:
      error(35, str(e)+' vaild.cam() error', False)
      return None

  def uuid(self, uuid_string): #https://gist.github.com/ShawnMilo/7777304
    try:
        val = uuid.UUID(uuid_string, version=4) #check UUID is valid to the UUID spec
    except ValueError as e:
        # If it's a value error, then the string
        # is not a valid hex code for a UUID.
        error(36, str(e)+' vaild.cam() error', False)
        return None

    # If the uuid_string is a valid hex code,
    # but an invalid uuid4,
    # UUID will convert it to a valid uuid4.

    return str(val)
