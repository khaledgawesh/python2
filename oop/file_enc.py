# class Student:
#   def __init__(self, name, age):
#     self.__name = name
#     self.age = age

#   def get_name(self):
#     return self.__name
  
#   def set_name(self, name):
#     self.__name = name


# std1 = Student("khaled", 20)
# std_name = std1.get_name()
# print(std_name)              

# std1.set_name("khaled gawesh")
# print(std1.get_name())


##############################################

class Student:
  def __init__(self, name, age):
    self.__name = name
    self.age = age

  def get_name(self):
      return self.__name
  
  def set_name(self, name):
      self.__name = name

  def get_name(self):
      return self.__age
  
  def set_name(self, name):
      self.__age = age

  def get_all_info(self):
     return self.__name, self.__age
    
std1 = Student("ahmed", 55)
print(std1.age)
print(list)
