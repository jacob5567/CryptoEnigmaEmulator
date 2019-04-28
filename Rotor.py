# Jacob Faulk

from random import shuffle

class Rotor:

    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def __init__(self, side1=None, side2=None):
        if(side1 == None):
            self.side1 = Rotor.alphabet.copy()
            shuffle(side1)
        else:
            self.side1 = side1
        if(side2 == None):
            self.side2 = Rotor.alphabet.copy()
            shuffle(side2)
        else:
            self.side2 = side2

    def __getitem__(self, key):
        key_index = self.side1.index(key)
        return self.side2[key_index]

    def getR(self, key):
        key_index = self.side2.index(key)
        return self.side1[key_index]

    def in_first_position(self, key):
        return self.side1.index(key) == 0

    def rotate(self):
        first_char = self.side2[0]
        for i in range(len(self.side2) - 1):
            self.side2[i] = self.side2[i + 1]
        self.side2[len(self.side2) - 1] = first_char

    def copy(self):
        return Rotor(self.side1.copy(), self.side2.copy())

    def __eq__(self, value):
        return self.side1 == value.side1 and self.side2 == value.side2

    def __str__(self):
        print_this = ""
        for i in self.side1:
            print_this += i + ' '
        print_this += "\n"
        for i in self.side2:
            print_this += i + ' '
        return print_this
