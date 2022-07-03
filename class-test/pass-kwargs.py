from dataclasses import dataclass


class People:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.tourist_instance = Tourist(name=self.name)

    def __call__(self, *args, **kwargs):
        print("hi, you are calling me")

    def print_self(self):
        print("Printing myself as a Person")
        print(self)
        # <__main__.People object at 0x104898cd0>

    def say_hi(self):
        print("hi")

    def introduce_oneself(self):
        print(f"Hi, I am {self.name}")

    def print_tourist_instance_kwargs(self):
        self.tourist_instance.print_all_kwargs()


@dataclass  # doesnt need __init__
class Tourist:
    name: str

    # def __init__(self, *args, **kwargs):
    #     self.name = kwargs.get("name")

    def print_all_kwargs(self, **kwargs):
        print("Printing kwargs")
        print(kwargs)

    def print_my_name(self):
        print("Printing my name")
        print(self.name)


lulu = People(name="Lulu")
lulu()
# hi, you are calling me

lulu.print_self()
# Printing myself as a Person
# <__main__.People object at 0x100f08ee0>

lulu.say_hi()
# hi

lulu.introduce_oneself()
# Hi, I am Lulu

lulu.print_tourist_instance_kwargs()
# Printing kwargs
# {}

lulu.tourist_instance.print_my_name()
# Lulu

Tourist(name="Lulu").print_all_kwargs()
# Printing kwargs
# {}

