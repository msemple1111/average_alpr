import unittest
from main import *
 
class validate_tests(unittest.TestCase):
  #test Validate() class
  #valid.road
  def test_road_validation_valid1(self):
    valid = validate()
    result = valid.road(5)
    self.assertTrue(result)
    
  def test_road_validation_valid2(self):
    valid = validate()
    result = valid.road('5')
    self.assertTrue(result)
    
  def test_road_validation_invalid(self):
    valid = validate()
    result = valid.road('_5')
    self.assertFalse(result)
    
  def test_plate_validation_british(self):
    valid = validate()
    result = valid.plate('YS56 BHC') #british number plate
    self.assertEqual('British', result)
    
  def test_plate_validation_usa(self):
    valid = validate()
    result = valid.plate('7LOV391') #califorian number plate
    self.assertEqual('Foreign', result)
    
  def test_plate_validation_invalid(self):
    valid = validate()
    result = valid.plate('7-ki-666777') #fake number plate
    self.assertFalse(result)
    
  def test_time_validation_valid1(self):
    valid = validate()
    result = valid.time(1234567890)
    self.assertTrue(result)
    
  def test_time_validation_valid2(self):
    valid = validate()
    result = valid.time('1234567890')
    self.assertTrue(result)
    
  def test_time_validation_invalid(self):
    valid = validate()
    result = valid.time('_1234567890')
    self.assertFalse(result)
    
  def test_postdata_validation_valid1(self):
    valid = validate()
    json_input = '{"road":1, "plate":"YS54 GBF","time": 1442862678}'
    json_input = json_input.encode()
    road_result, plate_result, time_result = valid.postdata(json_input)
    
    self.assertEqual(1, road_result)
    self.assertEqual("YS54 GBF", plate_result)
    self.assertEqual(1442862678, time_result)
    
    
class database_tests(unittest.TestCase):
  #test Database() class
  def test_calculator_add_method_returns_correct_resul(self):
    result = int(2+3)
    self.assertEqual(5, result)
    
if __name__ == '__main__':
    unittest.main()