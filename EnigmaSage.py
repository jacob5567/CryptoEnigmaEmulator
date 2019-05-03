# Jacob Faulk

class Rotor:

    # alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def __init__(self, side1=None, side2=None, rotorNumber=0):
        if(side1 == None):
            self.side1 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        else:
            self.side1 = side1

        if(side2 == None):
            if rotorNumber == 1:
                self.side2 = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
            elif rotorNumber == 2:
                self.side2 = list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
            elif rotorNumber == 3:
                self.side2 = list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
            else:
                self.side2 = list("ESOVPZJAYQUIRHXLNFTGKDCMWB")
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

    # def copy(self):
    #     return Rotor(self.side1.copy(), self.side2.copy())

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


class Plugboard:
    def __init__(self):
        self.plugs = {
            "B": "Q",
            "C": "R",
            "D": "I",
            "E": "J",
            "K": "W",
            "M": "T",
            "O": "S",
            "P": "X",
            "U": "Z",
            "G": "H"
        }
        # add reversed settings
        temp_plugs = {}
        for key, value in self.plugs.items():
            temp_plugs[value] = key
        self.plugs.update(temp_plugs)

    def __getitem__(self, key):
        return self.plugs.get(key, key)

    def __str__(self):
        print_this = ""
        for key in self.plugs.keys():
            print_this += key + " "
        print_this += "\n"
        for value in self.plugs.values():
            print_this += value + " "
        return print_this


def main():
    plaintext = raw_input(
        "Welcome to the Enigma Machine emulator. Enter plaintext to be encrypted.\n")

    plaintext = plaintext.upper()
    print "Plaintext: " + plaintext

    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    plugboard = Plugboard()

    print "Plugboard:"
    print plugboard
    print 

    rotor1 = Rotor(rotorNumber=1)
    rotor2 = Rotor(rotorNumber=2)
    rotor3 = Rotor(rotorNumber=3)

    reflector = Rotor(list("ZEFUHBDMNIJGACVTQRWYXOSLPK"),
                      list("GBURKVPSFHJTMXAIEZLNWODQYC"))

    final_result = ""

    for character in plaintext:
        if character in alphabet:
            current = character
            print "Current character: " + current

            current = plugboard[current]
            print "Turned into " + current + " by the plugboard."
            current = rotor1[current]
            print "Turned into " + current + " by the first rotor."
            rotor1.rotate()
            print "First rotor rotated."

            if rotor1.in_first_position('R'):
                rotor2.rotate()
                print "Second rotor rotated."
                if rotor2.in_first_position('F'):
                    rotor3.rotate()
                    print "Third rotor rotated."

            current = rotor2[current]
            print "Turned into " + current + " by the second rotor."
            current = rotor3[current]
            print "Turned into " + current + " by the third rotor."
            current = reflector[current]
            print "Turned into " + current + " by the reflector."
            current = rotor3.getR(current)
            print "Turned into " + current + " by the third rotor."
            current = rotor2.getR(current)
            print "Turned into " + current + " by the second rotor."
            current = rotor1.getR(current)
            print "Turned into " + current + " by the first rotor."

            rotor1.rotate()
            print "First rotor rotated."
            if rotor1.in_first_position('R'):
                rotor2.rotate()
                print "Second rotor rotated."
                if rotor2.in_first_position('F'):
                    rotor3.rotate()
                    print "Third rotor rotated."

            current = plugboard[current]
            print "Turned into " + current + " by the plugboard."
            print "Final character encryption: " + current + "\n\n"
            final_result += current
        else:
            final_result += character

    print "The final result is: " + final_result


if __name__ == "__main__":
    main()
