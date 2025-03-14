class Dog:
    def __init__(self,name,age,weight):
        self.name=name 
        self.age=age
        self.weight=weight
        
    def bark(self):
        return f"{self.name} is work"
    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} wins the fight"
        elif my_power < other_power:
            return f"{other_dog.name} wins the fight"
        else:
            return "It's a tie"
dog1 = Dog("kalinx", 5, 17)
dog2 = Dog("noby", 4, 13)
dog3 = Dog("farinx", 6, 18)
print(dog1.bark())
print(dog2.run_speed())
print(dog3.fight(dog1))
print(dog2.fight(dog3))