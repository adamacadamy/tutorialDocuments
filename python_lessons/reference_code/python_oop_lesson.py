
# Python Object-Oriented Programming (OOP) Lesson

# 1. Introduction to Object-Oriented Programming (OOP)
# Object-Oriented Programming (OOP) is a paradigm centered around creating objects.
# OOP is based on four principles:
# - Encapsulation: Grouping data and methods in a single unit (class).
# - Inheritance: Creating new classes based on existing ones.
# - Polymorphism: Providing a single interface for different data types.
# - Abstraction: Hiding the complex implementation and showing only necessary parts.

# 2. Creating Classes and Objects

# Basic Class Structure
class Car:
    pass

# Instantiating an Object
my_car = Car("Toyota", "Corolla")

# 3. Attributes and Methods

# Instance Attributes and the `__init__` Method
class Car:
    def __init__(self, make, model):
        self.make = make  # Instance attribute
        self.model = model

# Creating an instance
my_car = Car("Toyota", "Corolla")
print(my_car.make)  # Output: Toyota

# Instance Methods
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def description(self):
        return f"This car is a {self.make} {self.model}"

# Using the method
my_car = Car("Toyota", "Corolla")
print(my_car.description())  # Output: This car is a Toyota Corolla

# 4. Encapsulation
class Car:
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.__mileage = mileage  # Private attribute

    def get_mileage(self):
        return self.__mileage

my_car = Car("Toyota", "Corolla", 10000)
print(my_car.get_mileage())  # Output: 10000

# 5. Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):  # Car inherits from Vehicle
    def description(self):
        return f"This car is a {self.make} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.description())  # Output: This car is a Toyota Corolla

# 6. Polymorphism
class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started")

class Bike(Vehicle):
    def start(self):
        print("Bike engine started")

for vehicle in [Car(), Bike()]:
    vehicle.start()

# 7. Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine started")

my_car = Car()
my_car.start()  # Output: Car engine started

# 8. Advanced OOP Concepts

# Magic (Dunder) Methods
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car)  # Output: Toyota Corolla

# Static and Class Methods
class Car:
    wheels = 4  # Class attribute

    @staticmethod
    def honk():
        print("Beep Beep!")

    @classmethod
    def default_wheels(cls):
        return cls.wheels

Car.honk()  # Output: Beep Beep!
print(Car.default_wheels())  # Output: 4

# Summary Exercise:
# Create a hierarchy of different vehicles with attributes like speed, fuel type, etc.,
# and methods to display their unique properties, incorporating inheritance, encapsulation,
# polymorphism, and abstraction.
