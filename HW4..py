# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

#2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def seating_capacity(self):
        return self.seating_capacity

# # 3. Determine which class a given Bus object belongs to (Check type of an object)

bus_1 = Bus(180, 800, 40)

print(type( bus_1 ))

# Output:
# <class '__main__.Bus'>

#  4. Determine if School_bus is also an instance of the Vehicle class

 print(isinstance(School_bus, Vehicle))

# Output
#NameError: name 'Bus' is not defined

# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students

    def get_school_id(self):
        return self.school_id

#6 *. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color

class SchoolBus(School, Bus):
    def __init__(self, school_id, max_speed, mileage, seating_capacity, bus_school_color):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.__bus_school_color = bus_school_color

    def bus_school_color(self):
        return self.__bus_school_color

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.

class Bear:

    def make_sound(self):
        return ("Buu")

class Wolf:

    def make_sound(self):
        return ("Woo")

bear = Bear()
wolf = Wolf()
for animal in (bear, wolf):
    print("Animal makes sound: ", animal.make_sound())

# Output:
#     Animal makes sound: Buu
#     Animal makes sound: Woo

# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

        def __new__(cls, name, population):
            instance = super(City, cls).__new__(cls)
            if population > 1500:
                return instance
            else:
                return "Your city is too small"

# 9. Override a printable string representation of the City class and return: The population of the city {name} is {population}

   def __str__(self):
       return f'The population of the city {self.name} is a {self.population}'

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.

class Count :
    def __init__(self, count):
     self.count = count

    def __add__(self, other):
         if self.count > 10 or other.count > 10:
             total_count = self.count * other.count
         else:
             total_count = self.count + other.count
         return Count(total_count)

    def __str__(self):
        return f'Count: {self.count}'

a = Count(50)
b = Count (5)
c = a + b
print (c)

a1 = Count(100)
b1 = Count(200)
c1 = a1 + b1
print (c1)

#Output:
# Count: 250
# Count: 20000


# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.

class Addition:
    def __call__(self, a, b):
        return a + b


sum1 = Sum()
print(sum1(30, 50))

#Output
#80

# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer


    def __bool__(self):
        if len(self.cart) == 0:
            return False
        else:
            return True

order1 = MyOrder (['milk', 'bread', 'sugar'], "Anna")
order2 = MyOrder ([], "Marian")

print(bool(order1))
print(bool(order2))

# Output:
# True
# False