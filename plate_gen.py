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
    letters = self.letter_gen(5)
    numbers = self.number_gen(2)
    return str(letters[0]+letters[1]+numbers[0]+numbers[1]+" "+letters[2]+letters[3]+letters[4])

def insert_plate(no):
  import sqlite3
  no_plate = plate_gen()
  conn = sqlite3.connect('average_check_test.db')
  for x in range (1,no):
    plate = no_plate.gen_uk()
    print(plate)
    conn.execute("INSERT INTO plates (plate) VALUES ('"+plate+"');")
    conn.commit()
  conn.close()

insert_plate(2)


#print(no_plate.letter_gen(4))
#print(no_plate.number_gen(4))