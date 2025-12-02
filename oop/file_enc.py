class Student:
  def __init__(self, name, age):
    self.__name = name
    self.age = age

  def get_name(self):
    return self.__name


std1 = Student("khaled gawesh", 20)
std_name = std1.get_name()
print(std_name)
