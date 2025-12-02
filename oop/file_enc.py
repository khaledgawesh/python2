class Student:
  def __init__(self, name, age):
    self.__name = name
    self.age = age

  def get_name(self):
    return self.__name
  
  def set_name(self, name):
    self.__name = name


std1 = Student("khaled", 20)
std_name = std1.get_name()
print(std_name)
std1.set_name("khaled gawesh")
print(std_name)