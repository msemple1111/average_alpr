import unittest
from validate import validate
from database import database
from calculate import calculate
from plate_gen import plate_gen
from plate_gen import gen_database

class validate_tests(unittest.TestCase):
  #test Validate() class

  #valid.road()
  def test_road_validation_valid(self):
    valid = validate()
    valid_in = "A site Name"
    result = valid.site(valid_in)
    valid_in = str(valid_in) #convert input to string
    self.assertEqual(valid_in.lower(), result) #.lower() because validate returns lower version


  #valid.plate()
  def test_plate_validation_british(self):
    valid = validate()
    valid_in = 'YS56 Bhc' #british number plat
    result0, result1 = valid.plate(valid_in)
    valid_in = 'YS56 BHC' #Change to upper case becuase the function does
    self.assertEqual(valid_in, result0)
    self.assertFalse(result1)

  def test_plate_validation_usa(self):
    valid = validate()
    valid_in = '7LOV391'
    result0, result1 = valid.plate(valid_in) #califorian number plate
    self.assertEqual(valid_in, result0)
    self.assertTrue(result1)

  def test_plate_validation_invalid(self):
    valid = validate()
    result0, result1 = valid.plate('7-ki-666777') #fake number plate
    self.assertFalse(result0)
    self.assertFalse(result1)


  #valid.time()
  def test_time_validation_valid1(self):
    valid = validate()
    valid_in = 1457543875
    result = valid.time(valid_in)#valid time
    self.assertEqual(valid_in, result)

  def test_time_validation_valid2(self):
    valid = validate()
    valid_in = '1234567890' #valid time in string
    result = valid.time(valid_in)
    valid_in = int(valid_in) #convert input to int
    self.assertEqual(valid_in, result)

  def test_time_validation_invalid(self):
    valid = validate()
    result = valid.time('34--vbghjn_._J.')#in valid time
    self.assertFalse(result)


  #valid.confidence()
  def test_confidence_validation_valid1(self):
    valid = validate()
    valid_in = 87.657
    result = valid.confidence(valid_in)#valid confidence
    self.assertEqual(valid_in, result)

  def test_confidence_validation_valid2(self):
    valid = validate()
    valid_in = 0
    result = valid.confidence(valid_in)#valid confidence
    self.assertFalse(result)

  def test_confidence_validation_valid3(self):
    valid = validate()
    valid_in = 100.000
    result = valid.confidence(valid_in)#invalid confidence
    self.assertEqual(valid_in, result)

  def test_confidence_validation_invalid1(self):
    valid = validate()
    valid_in = "Ggkjdhb86.gge"
    result = valid.confidence(valid_in)#invalid confidence
    self.assertNotEqual(valid_in, result)

  #valid.cam()
  def test_cam_validation_valid(self):
    valid = validate()
    valid_in = 5
    result = valid.cam(valid_in)#valid cam id
    self.assertEqual(valid_in, result)


  def test_cam_validation_invalid(self):
    valid = validate()
    valid_in = '765ghgt'
    result = valid.cam(valid_in)#invalid cam id
    self.assertFalse(result)


  #valid.uuid()
  def test_uuid_validation_invalid1(self):
    valid = validate()
    valid_in = "5678gvbn.euy7"
    result = valid.uuid(valid_in)#invalid uuid
    self.assertFalse(result)

  def test_uuid_validation_valid(self):
    valid = validate()
    valid_in = "30414be5-0924-4d7e-860a-113c5e039e30"
    result = valid.uuid(valid_in)#valid uuid
    self.assertEqual(valid_in, result)

  def test_uuid_validation_invalid2(self):
    valid = validate()
    valid_in = "9dc680e2-f8bc-11e5-9ce9-5e551"
    result = valid.uuid(valid_in)#invalid uuid
    self.assertFalse(result)

class calculate_tests(unittest.TestCase):
  #calculate.average_speed()
  def test_average_speed_calculate_invalid1(self):
    calc = calculate()
    time_1_in = 120
    time_2_in = 160
    dist_in = -2
    result = calc.average_speed(time_1_in, time_2_in, dist_in)#invalid speed
    self.assertFalse(result)

  def test_average_speed_calculate_invalid2(self):
    calc = calculate()
    time_1_in = 170
    time_2_in = 120
    dist_in = 4
    result = calc.average_speed(time_1_in, time_2_in, dist_in)#invalid speed
    self.assertFalse(result)

  def test_average_speed_calculate_valid(self):
    calc = calculate()
    time_1_in = 120
    time_2_in = 160
    dist_in = 56
    result = calc.average_speed(time_1_in, time_2_in, dist_in)#valid speed
    answer = 1.4
    self.assertEqual(answer, result)

  #calculate.speed_increase()
  def test_speed_increase_calculate_valid(self):
    calc = calculate()
    car_speed_in = 10.4673
    road_speed_in = 15
    result = calc.speed_increase(car_speed_in, road_speed_in)#valid speed
    answer = -4.5327 #10.4673 - 15 = -4.5327
    self.assertEqual(answer, result)

  def test_speed_increase_calculate_invalid(self):
    calc = calculate()
    car_speed_in = '10.4673'
    road_speed_in = 'a0hbv'
    result = calc.speed_increase(car_speed_in, road_speed_in)#valid speed
    self.assertFalse(result)


class database_tests(unittest.TestCase):
  #test Database() class
  def test_sql_checkplate_valid1(self):
    test_sql = gen_database() #initialising a different database cursor to avoid any problems with the database class
    no_plate = plate_gen() #initialising plate generating algorithm
    sqlite = database() #initialising database class

    plate = no_plate.gen_uk() #generating random uk plate
    test_sql.ecx.execute("SELECT MAX(p_id) FROM plates;") #finding the current hightest p_id (plate id)
    max_index = test_sql.ecx.fetchone()[0] + 1 #get max id then add 1

    result0 = sqlite.add_plate(plate) #adding new plate and returning p_index
    self.assertEqual(max_index, result0) #result should match the hightest p_index from before

  def test_sql_checkplate_valid2(self):
      sqlite = database() #initialising database
      result1 = sqlite.add_plate('SU84 XFR') #this plate is already in the database - so it should return ust the p_id
      self.assertEqual(2, result1) #i know the p_id for this plate is 2 because it is entered when the sql database is created


if __name__ == '__main__':
    unittest.main()
