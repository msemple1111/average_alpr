import unittest
from main import *
from plate_gen import plate_gen
from plate_gen import gen_database
 
class validate_tests(unittest.TestCase):
  #test Validate() class
  #valid.road()
  def test_road_validation_valid1(self):#1
    valid = validate()
    result = valid.road(5)
    self.assertTrue(result)
    
  def test_road_validation_valid2(self):#2
    valid = validate()
    result = valid.road('5')
    self.assertTrue(result)
    
  def test_road_validation_invalid(self):#3
    valid = validate()
    result = valid.road('_5')
    self.assertFalse(result)
    
    
  #valid.plate()
  def test_plate_validation_british(self):#4
    valid = validate()
    result = valid.plate('YS56 BHC') #british number plate
    self.assertEqual('British', result)
    
  def test_plate_validation_usa(self):#5
    valid = validate()
    result = valid.plate('7LOV391') #califorian number plate
    self.assertEqual('Foreign', result)
    
  def test_plate_validation_invalid(self):#6
    valid = validate()
    result = valid.plate('7-ki-666777') #fake number plate
    self.assertFalse(result)
    
    
  #valid.time()
  def test_time_validation_valid1(self):#7
    valid = validate()
    result = valid.time(1234567890)#valid time
    self.assertTrue(result)
    
  def test_time_validation_valid2(self):#8
    valid = validate()
    result = valid.time('1234567890')#valid time in string
    self.assertTrue(result)
    
  def test_time_validation_invalid(self):#9
    valid = validate()
    result = valid.time('_1234567890')#in valid time
    self.assertFalse(result)
    
    
  #valid.postdata()
  def test_postdata_validation_valid1(self):#10
    valid = validate()
    json_input = '{"road":1, "plate":"YS54 GBF","time": 1442862678}'
    json_input = json_input.encode()
    road_result, plate_result, time_result = valid.postdata(json_input)
    
    self.assertEqual(1, road_result)
    self.assertEqual("YS54 GBF", plate_result)
    self.assertEqual(1442862678, time_result)
    
  def test_postdata_validation_valid2(self):#11
    valid = validate()
    json_input = '{"road":1, "plate":"YS54 GBF","time": 1442862678}'
    json_input = json_input.encode()
    road_result, plate_result, time_result = valid.postdata(json_input)
    
    self.assertEqual(1, road_result)
    self.assertEqual("YS54 GBF", plate_result)
    self.assertNotEqual(1442862679, time_result)
    
    
class database_tests(unittest.TestCase):
  #test Database() class
  def test_sql_checkplate_valid1(self):
    test_sql = gen_database() #initialising the database class from the plate generation/insertion file - to keep it seperate from the main.py
    no_plate = plate_gen() #initialising plate generating  
    sqlite = database() #initialising database  
    
    plate = no_plate.gen_uk() #generating random plate 
    test_sql.ecx.execute("SELECT MAX(p_index) FROM plates;") #finding the current hightest p_index
    max_index = test_sql.ecx.fetchone()[0] + 1 #then adding 1  
    
    result0 = sqlite.add_plate(plate) #adding new plate and returning p_index
    self.assertEqual(max_index, result0) #result should match the hightest p_index from before
    
  def test_sql_checkplate_valid2(self):
    sqlite = database() #initialising database  
    result1 = sqlite.add_plate('KU46 KRQ') #this plate is already in the database - so it should return ust the p_index
    self.assertEqual(13, result1) #i know the p_index for this plate is 13
    
    
    
if __name__ == '__main__':
    unittest.main()