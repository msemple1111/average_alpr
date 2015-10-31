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
    for i in range(no):
      self.number.append(str(randint(0,9)))
    return self.number
  
  def gen_uk(self):
    letters = self.letter_gen(5)
    numbers = self.number_gen(2)
    return letters[0]+letters[1]+numbers[0]+numbers[1]+" "+letters[2]+letters[3]+letters[4]
    
no_plate = plate_gen()
print(no_plate.gen_uk())

#print(no_plate.letter_gen(4))
#print(no_plate.number_gen(4))