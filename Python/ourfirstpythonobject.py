class PartyAnimal:
   x = 0

# __init__ metode tiks izpildita tikai vienu
# reizi, veidojot (katru) instanci
   def __init__(self):
    print('I am construced')
    self.x=0
        
   def party(self) :
     self.x = self.x + 1
     print("So far x property of object",\
           "is: ",self.x)

   def __del__(self):
     print('I am destructed', self.x)

print("Before an = PartyAnimal()")
#print(vars())
an = PartyAnimal()
print("After an = PartyAnimal()")
#print(vars())
#print("an data type or class"), type(an)
#print("an methods and properties"), dir(an)
#print("an x property data type"), type(an.x)
#print("an party method data type"), type(an.party)
#print(vars(an))
# tikai ja klase ir ar __init__ ar self.x = ...
#tikai tad {'x': 0}, savadāk ir {}

print("Before first an.party()")
an.party()
print("After first an.party")
#print(vars()) # objekts "aiztikts"“ {'x': 1}

an.x = 100
an.__init__()

print("Before second an.party")
an.party()
print("After second an.party()")

an.x = 200

print("Before third an.party()")
an.party()
print("After third an.party()")

print("\nBefore one more party()")
PartyAnimal.party(an)
print("After one more party()")
