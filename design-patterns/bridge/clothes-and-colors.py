from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def print_color(self):
        print('Printing color')


class Orange(Color):
    def print_color(self):
        print("I am orange!")


class Pink(Color):
    def print_color(self):
        print("Pinky")


class Clothes(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def talk(self):
        pass

    def get_color(self):
        print(self.color.print_color())


class Skirt(Clothes):
    def talk(self):
        print("Hi, I am a skirt.")


class Shirt(Clothes):
    def talk(self):
        print("Hello, wear me tomorrow.")


orange = Orange()
orange_shirt = Shirt(orange)
orange_shirt.talk()
orange_shirt.get_color()
