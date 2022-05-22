class Dog:
    def __init__(self):
        self.__sound = "Bark"

    def get_sound(self):
        return self.__sound

    def bark(self):
        print(self.get_sound())


class Cat:
    def __init__(self):
        self.__sound = "Meow"

    def get_sound(self):
        return self.__sound

    def meow(self):
        print(self.get_sound())


class Adapter:
    def __init__(self, obj, **kwargs):
        self.__obj = obj
        self.__dict__.update(kwargs)

    def get_obj(self):
        return self.__obj


dog = Dog()
cat = Cat()

objects = []
objects.append(Adapter(dog, sound=dog.get_sound()))
objects.append(Adapter(cat, sound=cat.get_sound()))

for obj in objects:
    print(f"{obj.get_obj().__class__.__name__} makes the sound '{obj.sound}'")

