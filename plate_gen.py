class plate_gen:
  def __init__(self):
    from random import randint
  def letter_gen(self, no):
    letter = []
    for i in range(no):
      letter.append(chr(randint(65,90)))
    return letter
      
  def numbers_gen(self):
    number = []
    number.append(str(randint(0,9)))
    number.append(str(randint(5,6)))
    return number
  
  def gen_uk(self):
    letters = self.letter_gen(5)
    numbers = self.numbers_gen()
    return str(letters[0]+letters[1]+numbers[0]+numbers[1]+" "+letters[2]+letters[3]+letters[4])
  
  def gen_time(self):
    time_1 = randint(1448000000, 1448600000)
    return time_1, (time_1 + randint(2, 20))
  

class gen_database:
  def __init__(self):
    import sqlite3 as sql
    self.rdb = None
    self.rdb = sql.connect('average_check.db')
    self.ecx = self.rdb.cursor()    

  def plate(self, no):
    no_plate = plate_gen()
    for x in range(1, no):
      self.plate = no_plate.gen_uk()
      self.ecx.execute("INSERT INTO plates (plate) VALUES ('"+plate+"');")
      self.rdb.commit()
      return self.plate

  def road(self, r_name, s_limit, r_dist):
    self.ecx.execute("INSERT INTO roads (r_name, s_limit, r_dist) VALUES ('"+r_name+"',"+s_limit+","+r_dist+");")
    self.rdb.commit()
    return r_name
if __name__ == '__main__':
  gen = plate_gen()
  #print(insert.plate(2))
  print(gen.gen_uk())


#print(no_plate.letter_gen(4))
#print(no_plate.number_gen(4))