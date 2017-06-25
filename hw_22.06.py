class Animal(object):
    """
    Creating Animal class to describe animals
    """
    def __init__(self, is_alive, is_big, is_wild):
        self.alive = is_alive
        self.big = is_big
        self.wild = is_wild

    def voice(self):
        raise NotImplementedError("This animal is voiceless")


class Cat(Animal):
    """
    sadsdsad
    """
    def voice(self):
        return "Meow"
class Tiger(Animal):
    """
    asdasdasd
    """
    def voice(self):
        return "Agrrrr"

class Cow(Animal):
    """
    dsfsdfsdf
    """
    def voice(self):
        return "Moooooooo"
class Dog(Animal):
    """
    asdsada
    """
    pass
    # def voice(self):
    #     return "Gav-gav"

cat = Cat("alive", "little", "domestic")
tiger = Tiger("alive", "big", "wild")
cow = Cow("dead", "big", "domestic")
dog = Dog("alive", "big", "domestic")


print("Tiger is ", tiger.alive, tiger.big, tiger.wild, "animal, His voice is", tiger.voice())
print("Cat is ", cat.alive, cat.big, cat.wild, "animal, His voice is", cat.voice())
print("Cow is ", cow.alive, cow.big, cow.wild, "animal, His voice is", cow.voice())
print("Dog is ", dog.alive, dog.big, dog.wild, "animal, His voice is", dog.voice())

#bonus 7
def gen(num):
    for i in range(0, 100):
        if i % num == 0:
            yield i

data = gen(3)
for i in data:
    print(i)

#bonus 8
data = [num for num in range(0, 100) if num % 3 == 0]
print(data)






