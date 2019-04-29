# Jacob Faulk

from Rotor import Rotor


def main():
    # plaintext = input("Welcome to the Enigma Machine emulator. Enter plaintext to be encrypted.\n")

    # Enter plaintext here
    plaintext = "Hello"  # Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    plaintext = plaintext.upper()
    print("Plaintext: " + plaintext)

    print("The first step in encoding a message in the Enigma involves a plugboard.")
    print("This would be set every day and sent out to the German soldiers in WWII.")
    print("For this example, the plugboard will be set as follows:")

    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    plugboard = Plugboard()

    print(plugboard)

    rotor1 = Rotor(rotorNumber=1)
    rotor2 = Rotor(rotorNumber=2)
    rotor3 = Rotor(rotorNumber=3)

    reflector = Rotor(list("ZEFUHBDMNIJGACVTQRWYXOSLPK"),
                      list("GBURKVPSFHJTMXAIEZLNWODQYC"))

    final_result = ""

    for character in plaintext:
        if character in alphabet:
            current = character
            print("Current character: " + current)
            current = plugboard[current]
            print("Turned into " + current + " by the plugboard.")
            current = rotor1[current]
            print("Turned into " + current + " by the first rotor.")
            rotor1.rotate()
            print("First rotor rotated.")

            if rotor1.in_first_position('R'):
                rotor2.rotate()
                print("Second rotor rotated.")
                if rotor2.in_first_position('F'):
                    rotor3.rotate()
                    print("Third rotor rotated.")

            current = rotor2[current]
            print("Turned into " + current + " by the second rotor.")
            current = rotor3[current]
            print("Turned into " + current + " by the third rotor.")

            # TODO make the reflector settable and historically accurate
            current = reflector[current]
            print("Turned into " + current + " by the reflector.")

            current = rotor3.getR(current)
            print("Turned into " + current + " by the third rotor.")
            current = rotor2.getR(current)
            print("Turned into " + current + " by the second rotor.")
            current = rotor1.getR(current)
            print("Turned into " + current + " by the first rotor.")
            rotor1.rotate()
            print("First rotor rotated.")
            if rotor1.in_first_position('R'):
                rotor2.rotate()
                print("Second rotor rotated.")
                if rotor2.in_first_position('F'):
                    rotor3.rotate()
                    print("Third rotor rotated.")

            current = plugboard[current]
            print("Turned into " + current + " by the plugboard.")
            print("Final character encryption: " + current + "\n\n")
            final_result += current
        else:
            final_result += character

    print("The final result is: " + final_result)


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


if __name__ == "__main__":
    main()
