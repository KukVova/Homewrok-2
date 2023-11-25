class Dog:
    height = 0
    born = 0
    age = 0
    name = ''
    happiness = 100
    tiredness = 0
    sleep = 100
    species = ''

    def eat(self):
        self.happiness += 10
        self.tiredness += 3
    def sleep(self):
        self.tiredness -= 10
        self.happiness += 10
        self.sleep += 5
    def play(self):
        self.happiness += 20
        self.tiredness += 15
        self.sleep -= 10
    def walk(self):
        self.happiness += 15
        self.tiredness += 20
        self.sleep -= 15
    def bark(self):
        self.tiredness += 10
        self.happiness -= 10
    def train(self):
        self.tiredness += 10
        self.happiness += 5
        self.sleep -= 10

dog1 = Dog()
dog2 = Dog()

dog1.height = 60, 'см'
dog2.height = 50, 'см'
dog1.age = 5
dog2.age = 3
dog1.name = 'John'
dog2.name = 'Bob'
dog1.species = 'brown'
dog2.species = 'orange'
dog1.born = '2018', '07', '20'
dog2.born = '2020', '09', '26'
print(dog1.height)
print(dog2.height)
print(dog1.age)
print(dog2.age)
print(dog1.name)
print(dog2.name)
print(dog1.species)
print(dog2.species)
print(dog1.born)
print(dog2.born)
print(dog1.happiness,dog1.tiredness,dog1.sleep)
print(dog2.happiness,dog2.tiredness,dog2.sleep)
