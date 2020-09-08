#parent class
class Customer:
  def __init__(self, fname, lname, rid):
    self.firstname = fname
    self.lastname = lname
    self.registerid = rid

  def getDetails(self):
    print(self.firstname, self.lastname, self.registerid)

#child class 
class CustomerInfo(Customer):
  def __init__(self, fname, lname,rid,prof):
      #inheriting all parent class properties using super()
    super().__init__(fname, lname,rid)
    self.profession = prof
    

obj = CustomerInfo("Linus", "Torvalds",1,"Software Developer")
print(obj.firstname)
print(obj.lastname)
print(obj.registerid)
print(obj.profession)
