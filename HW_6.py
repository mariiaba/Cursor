#
# # **Garden**
# We have only one garden. In the garden can have
# vegetables, fruits and pests.
# Each fruit or vegetable should have a stage of
# maturity (stages: None, Flowering, Green, Red).
# Pests can eat only green and red fruit or vegetable.
# Once pests eat the fruit, it should be removed.
#
# ## There is a Tomato with the following
# characteristics:
# 1. Number of tomatoes (Index)
# 2. Vegetable type
#
# ### A tomato can:
# 1. Grow (move to the next stage of maturation)
# 2. Provide information about your maturity
#
# ### There is a Tomato Bush that:
# 1. Contains a list of tomatoes that grow on it
#
# ### And:
# 1. Grow with tomatoes
# 2. Provide information on the maturity
# of all tomatoes
# 3. Provide harvest
#
# ## There is an Apple with the following
# characteristics:
# 1. Number of apples (Index)
# 2. Fruit type
#
# ### An apple can:
# 1. Grow (move to the next stage of maturation)
# 2. Provide information about your maturity
#
# ### There is an Apple Tree that:
# 1. Contains a list of apples that grow on it
#
# ### And:
# 1. Grow with apples
# 2. Provide information on the maturity of all apples
# 3. Provide harvest
#
# ## And there is also a Gardener who has:
# 1. Name
# 2. The plants he looks after
#
# ### And:
# 1. Take care of the plant
# 2. Poison the pests
# 2. Harvest from it
#
# Homework:
#
# ## And there is also a Pests who have:
# 1. Type
# 2. Quntity
#
# ### And:
# 1. Eat the plants
#
# ### Implement the possibility when pests eat the fruit and vegetable
#
# Your implementation should work with this:
# Please note that this part doesn't include the pests, you need to finish it as well.
# if name == 'main':
#     # Creating list of instances for vegetables and fruits, pests and gardener
#     tomato_bush = TomatoBush(4)
#     apple_tree = AppleTree(3)
#     pests = Pests('worm', 10)
#     tom = StarGardener('Tom', [tomato_bush, apple_tree])
#     # creating only one garden instance with vegetables and fruits
#     garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests, gardener=tom)
#     garden.show_the_garden()
#     state = tom.check_states()
#     # if not state:
#     #     gardener.handling()
#     for i in range(3):
#         tom.handling()
#     tom.harvest()


import dataclasses
from abc import ABC, abstractmethod

VEGETABLES = ["Red_tomato"]
FRUITS = ["Golden"]

states = {'nothing': 0, 'flowering': 1, 'green': 2, 'red': 3, 'rotten': 4}


class GardenMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMetaClass):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener
        self.vegetables_names = [tomato.vegetable_type for tomato in self.vegetables]
        self.fruits_names = [apple.fruits_type for apple in self.fruits]

    def show_the_garden(self):
        print(f'The garden has such vegetables: {self.vegetables_names}')
        print(f'Also garden has such fruits: {self.fruits_names}')
        print(f'And such pests: {self.pests}')
        print(f'The maintainer of the garden is {self.gardener}')


@dataclasses.dataclass()
class PlantsStates:
    nothing: int
    flowering: int
    green: int
    red: int
    rotten: int


class Vegetables(ABC):
    def __init__(self, states, vegetable_type, name):
        self.states = states
        self.vegetable_type = vegetable_type
        self.name = name


    @property
    def vegetable_type(self):
        return self._vegetable_type

    @vegetable_type.setter
    def vegetable_type(self, vegetable_type):
        if vegetable_type in VEGETABLES:
            self._vegetable_type = vegetable_type
            print('all ok')
        else:
            raise Exception(f'There is no such vegetable in the list. Your vegetable: {vegetable_type}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('Your method is not implemented.')


class Fruit(ABC):
    def __init__(self, states, fruits_type, name):
        self.states = states
        self.fruits_type = fruits_type
        self.name = name

    @property
    def fruits_type(self):
        return self._fruits_type

    @fruits_type.setter
    def fruits_type(self, fruits_type):
        if fruits_type in FRUITS:
            self._fruits_type = fruits_type
            print('all ok')
        else:
            raise Exception(f'There is no such fruit in the list. '
                            f'Your fruit {fruits_type} and list {FRUITS}')

    @abstractmethod
    def grow(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('The method is missing.')


class Gardener(ABC):
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    @abstractmethod
    def harvest(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def poison_pests(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def handling(self):
        raise NotImplementedError('The method is missing.')

    @abstractmethod
    def check_states(self):
        raise NotImplementedError('The method is missing.')


class Pests(ABC):
    def __init__(self, pests_type, quantity):
        self.pests_type = pests_type
        self.quantity = quantity

    @abstractmethod
    def eat(self):
        raise NotImplementedError('The method is missing.')


class Tomato(Vegetables):
    def __init__(self, index, vegetable_type, states, name):
        super(Tomato, self).__init__(states, vegetable_type, name)
        self.index = index
        self.vegetable_type = vegetable_type
        self.state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print (f'{self.vegetable_type} {self.index} is {self.state}')

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index, 'Red_tomato', states, 'Cherry') for index in range(0, num - 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        """
        all([True, True, True]) = True
        all([True, True, False]) = False
        :return:
        """
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def provide_harvest(self):
        self.tomatoes = []

    def __call__(self):
        return self.tomatoes

class Apple(Fruit):
    def __init__(self, index, fruits_type, states, name):
        super(Apple, self).__init__(states, fruits_type, name)
        self.index = index
        self.fruits_type = fruits_type
        self.state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def _change_state(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        return f'{self.fruits_type} {self.index} is {self.state}'


class AppleTree:
    def __init__(self, num):
        self.apples = [Apple(index, 'Golden', states, 'King') for index in range(0, num - 1)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        """
        all([True, True, True]) = True
        all([True, True, False]) = False
        :return:
        """
        return all([apple.is_ripe() for apple in self.apples])

    def provide_harvest(self):
        self.apples = []

    def __call__(self):
        return self.apples

class StarGardener(Gardener):
    def __init__(self, name, plants):
        super(StarGardener, self).__init__(name, plants)
        self.name = name
        self.plants = plants

    def harvest(self):
        print('Gardener is harvesting...')
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.provide_harvest()
                print('Harvesting is finished.')
            else:
                print('Too early! Your plants is not ripe.')

    def handling(self):
        print('Gardner is working...')
        for plant in self.plants:
            plant.grow_all()
        print('Gardner is finished')

    def poison_pests(self):
        if pests.quantity == 0:
            print('There is no need to poison pests')

        else:
            if pests.quantity >= 1:
                print ('Fighting pests')
                pests.quantity //=2


    def check_states(self):
        for all_plants in self.plants:
            for plant in all_plants():
                if plant.state == 3:
                    return True
                else:
                    return False

    def __str__(self):
        return f'{self.name}'

class PestsWork (Pests):
    def __init__(self, pests_type, quantity):
        super(PestsWork, self). __init__(pests_type, quantity)
        self.pests_type = pests_type
        self.quantity = quantity

    def eat (self):
        for pests in range (self.quantity):
            apple_tree.apples.pop(-1)
            print('An apple was eaten')
            if len (apple_tree.apples)==0:
                print('There are no apples to eat')
                break

        for pests in range(self.quantity):
            tomato_bush.tomatoes.pop(-1)
            print('A tomato was eaten')
            if len(tomato_bush.tomatoes) == 0:
                print('There are no tomatoes to eat')
                break

    def __str__(self):
        return f'There are {self.quantity} angry pests'

    
if __name__ == '__main__':
    # Creating list of instances for vegetables and fruits, pests and gardener
    tomato_bush = TomatoBush(4)
    apple_tree = AppleTree(3)
    pests = PestsWork('worm', 10)
    tom = StarGardener('Tom', [tomato_bush, apple_tree])
    tom.poison_pests()
    #pests.eat()

    # creating only one garden instance with vegetables and fruits
    garden = Garden(vegetables=tomato_bush.tomatoes, fruits=apple_tree.apples, pests=pests, gardener=tom)
    garden.show_the_garden()
    # state = tom.check_states()
    tom.check_states()
    for i in range(3):
        tom.handling()
    tom.harvest()




