# Jacob Faulk


class Rotor:  # This is the rotor class. It represents one of the rotors in the orginal Enigma

    def __init__(self, side1=None, side2=None, rotorNumber=0):
        if(side1 == None):
            self.side1 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        else:
            self.side1 = side1

        if(side2 == None):  # The three lists below reflect the historical rotors of the original Enigma machine
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

    # this retrieves the corresponding letter that the rotor would output when given a letter "key" as input
    def __getitem__(self, key):
        key_index = self.side1.index(key)
        return self.side2[key_index]

    def getR(self, key):  # this does the same as __getitem__(), except it does it in reverse, which is useful for the return trip
        key_index = self.side2.index(key)
        return self.side1[key_index]

    # this function is so the program can tell when the rotors need to be rotated
    def in_first_position(self, key):
        return self.side1.index(key) == 0

    def rotate(self):  # this function rotates the rotors
        first_char = self.side2[0]
        for i in range(len(self.side2) - 1):
            self.side2[i] = self.side2[i + 1]
        self.side2[len(self.side2) - 1] = first_char

    def __str__(self):  # this function allows a rotor to be easily printed
        print_this = ""
        for i in self.side1:
            print_this += i + ' '
        print_this += "\n"
        for i in self.side2:
            print_this += i + ' '
        return print_this


class Plugboard:  # this is the internal representation of the Enigma's plugboard
    def __init__(self):
        self.plugs = {  # these plugs would be set every day by German high command
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
        # This code makes sure that the plugboard goes both ways: i.e. 'B' corresponds to 'Q' and 'Q' also corresponds to 'B'
        temp_plugs = {}
        for key, value in self.plugs.items():
            temp_plugs[value] = key
        self.plugs.update(temp_plugs)

    # This function returns the corresponding letter. If the plugs have not been changed for that letter, it returns the letter unchanged.
    def __getitem__(self, key):
        return self.plugs.get(key, key)

    def __str__(self):  # This function allows the plugboard configuration to be printed easily
        print_this = ""
        for key in self.plugs.keys():
            print_this += key + " "
        print_this += "\n"
        for value in self.plugs.values():
            print_this += value + " "
        return print_this


plaintext = "Hello"  # ENTER PLAINTEXT HERE

plaintext = plaintext.upper()  # the plaintext is converted to all caps
print "Plaintext: " + plaintext

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

plugboard = Plugboard()  # this initializes the plugboard using the default settings

print "Plugboard:"
print plugboard
print

# these rotorNumber settings ensure that each rotor is set to its historically accurate settings
rotor1 = Rotor(rotorNumber=1)
rotor2 = Rotor(rotorNumber=2)
rotor3 = Rotor(rotorNumber=3)

reflector = Rotor(list("ZEFUHBDMNIJGACVTQRWYXOSLPK"),
                  list("GBURKVPSFHJTMXAIEZLNWODQYC"))  # this reflector is set randomly

final_result = ""

for character in plaintext:  # This is the main program loop. It goes through every character in the plaintext and translates it into its corresponding character in the ciphertext
    if character in alphabet:  # this line makes sure that all punctuation or spaces are not put through the enigma machine
        current = character
        print "Current character: " + current

        current = plugboard[current]
        print "Turned into " + current + " by the plugboard."
        current = rotor1[current]
        print "Turned into " + current + " by the first rotor."
        rotor1.rotate()  # the first rotor is always rotated every time a letter is typed
        print "First rotor rotated."

        # the second and third rotors are only rotated when the previous rotors are in the correct positions
        # the second rotor would rotate when the first rotor had the letter 'R' in its first position
        if rotor1.in_first_position('R'):
            rotor2.rotate()
            print "Second rotor rotated."

        current = rotor2[current]
        print "Turned into " + current + " by the second rotor."
        # the third rotor would rotate when the second rotor had the letter 'F' in its first position
        if rotor2.in_first_position('F'):
            rotor3.rotate()
            print "Third rotor rotated."

        current = rotor3[current]
        print "Turned into " + current + " by the third rotor."
        # the halfway point, where the signal is reflected
        current = reflector[current]
        print "Turned into " + current + " by the reflector."
        current = rotor3.getR(current)
        print "Turned into " + current + " by the third rotor."
        current = rotor2.getR(current)
        print "Turned into " + current + " by the second rotor."
        if rotor2.in_first_position('F'):
            rotor3.rotate()
            print "Third rotor rotated."
        current = rotor1.getR(current)
        print "Turned into " + current + " by the first rotor."

        rotor1.rotate()
        print "First rotor rotated."
        if rotor1.in_first_position('R'):
            rotor2.rotate()
            print "Second rotor rotated."

        # signal finally goes back through the plugboard
        current = plugboard[current]
        print "Turned into " + current + " by the plugboard."
        print "Final character encryption: " + current + "\n\n"
        final_result += current
    else:
        final_result += character

print "The final result is: " + final_result
