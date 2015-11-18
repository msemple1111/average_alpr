class plate_gen:
  def __init__(self):
    print()
    
  def letter_gen(self,no):
    from random import randint
    self.letter = []
    for i in range(no):
      self.letter.append(chr(randint(65,90)))
    return self.letter
      
  def number_gen(self,no):
    from random import randint
    self.number = []
    self.number.append(str(randint(0,9)))
    self.number.append(str(randint(5,6)))
    return self.number
  
  def gen_uk(self):
    self.letters = self.letter_gen(5)
    self.numbers = self.number_gen(2)
    return str(self.letters[0]+self.letters[1]+self.numbers[0]+self.numbers[1]+" "+self.letters[2]+self.letters[3]+self.letters[4])
  

class gen_database:
  def __init__(self):
    import sqlite3 as sql
    self.rdb = None
    self.rdb = sql.connect('average_check_test.db')
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
insert = gen_database()
#print(insert.plate(2))
print(insert.road("Clevedon Way", '15', '100'))


#print(no_plate.letter_gen(4))
#print(no_plate.number_gen(4))