from error import error
class calculate:
  def average_speed(self, time_1, time_2, dist): #returns average speed in m/s after two time inputs
    try:
      time = time_2 - time_1 #find the time
      speed =  dist/time # speed = distance / time
      if speed < 0: #if speed is less than 0, raise an error
          error(20,'calculate.average_speed() error', False)
          return None #
      else:#otherwise return speed as a float
          return speed
    except:
      error(21,'calculate.average_speed() error', False)
      None

  def speed_increase(self, car_speed, road_speed):
    try:
      return car_speed - road_speed #return speed relative to speed limit in m/s
    except:
      error(22,'calculate.average_speed() error', False)
      return None
