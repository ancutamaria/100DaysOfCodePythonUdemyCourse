class Animal:

    def __init__(self):
        self.number_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        print()
        super().breathe()
        print("doing this under water.")
        print()

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.number_eyes)
