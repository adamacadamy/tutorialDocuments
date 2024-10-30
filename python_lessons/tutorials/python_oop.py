""" 
  paradigm | model
  Object Oriented Programming
  
   Objects
     - properties | variables | attributes
        public : properties which are accessible to the external world
        private:  properties which are not accessible to the external world
        protected: sub classes can have access but not external world
     - methods  | functions
        public : functions which are accessible to the external world
        private:  functions which are not accessible to the external world
        protected: sub classes can have access but not external world

- Encapsulation: grouping of data together in single unit
 class Iphone:
    pass
- Inheritance: Creating new class out of an existing class
class CellPhone:
    pass

class Iphone(CellPhone):
    pass

- Polymorphism: existence of the same term (thing) in different forms

 existence of Animal in the form of Dog and Cat
 
    class Dog: # super class
        pass
        
    class DogoArgnitino(Dog): # child class
        pass
        
    class Shiwawa(Dog): # child class
        pass
        
- Abstraction: Hiding of complex implementation showing only necessary parts 
from abc import ABC, abstractmethod
-- dogoar = (DogoArgnitino)
class Animal(ABC)

    @abstractmethod
    def bark(self):
        pass
        
        
class DogoArgnitino(Dog): # child class
    def bark(self):
        print("mild_bark")
    
class Shiwawa(Dog): # child class
    def bark(self):
        print("some_Bark")

import dogoar

animal: Animal = dogoar 
__
_
"""
# a class is a blueprint for an object
from abc import ABC, abstractmethod

class Car: 

    def __init__(self, make: str, model: int, mileage: int, age: int): # constructor 
        self.make = make #public
        self.model = model # public
        self.__mileage = mileage #private
        self._age = age # java, c++, c# protected means protected but in python you can call a protect property
        
    def get_mileage(self)-> int:
        return self.__mileage
    
    def set_mileage(self, mileage:int):
        self.__mileage = mileage
        
    def star_car(self, ignite=True):
        print(f"car {self.make}-{self.model} started")
        if not ignite:
            self.__dont_ignite()
        
    def __dont_ignite(self):
        print("not_igniting")
    
    def __str__(self) -> str: # object hasher 
        return f"{self.make}-{self.model}-{self.__mileage}"
        
my_car = Car(make="BMW", model=1121, mileage=3242, age=20)

print(my_car)

print(my_car.model)
print(my_car.make)
print(my_car.get_mileage())
print(my_car._age)

my_car.set_mileage(7888)
print(my_car.get_mileage())

my_car.star_car()

my_car.star_car(ignite=False)

class Plane(ABC):
    @abstractmethod
    def fly(self):
        pass
    
class B787(Plane):
    def __init__(self) -> None:
        super().__init__()
    
    def fly(self):
        print("Flying")
        
my_plane: Plane = B787()

my_plane.fly()

class Person:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name
        # self.age = self.__age
    
        
    @property
    def age(self): 
        return self.__age
    
    @age.setter
    def age(self, some_age):
        self.__age = some_age
        
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, some_name):
        self.name = some_name


adam = Person("adam", "35")

print(adam.age)
adam.age = 11
print(adam.age)
 