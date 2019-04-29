# Jacob Faulk

from Rotor import Rotor


def main():
    plaintext = input("Welcome to the Enigma Machine emulator. Enter plaintext to be encrypted.\n")

    plaintext = plaintext.upper()
    print("Plaintext: " + plaintext)

    input()

    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    plugboard = Plugboard()

    print("Plugboard:")
    print(plugboard)
    print()

    rotor1 = Rotor(rotorNumber=1)
    rotor2 = Rotor(rotorNumber=2)
    rotor3 = Rotor(rotorNumber=3)

    reflector = Rotor(list("ZEFUHBDMNIJGACVTQRWYXOSLPK"),
                      list("GBURKVPSFHJTMXAIEZLNWODQYC"))

    final_result = ""
    first_iteration = True

    for character in plaintext:
        if character in alphabet:
            current = character
            print("Current character: " + current)
            if first_iteration:
                input()
            current = plugboard[current]
            print("Turned into " + current + " by the plugboard.")
            if first_iteration:
                input()
            current = rotor1[current]
            print("Turned into " + current + " by the first rotor.")
            if first_iteration:
                input()
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
            if first_iteration:
                input()
            current = rotor3[current]
            print("Turned into " + current + " by the third rotor.")
            if first_iteration:
                input()

            current = reflector[current]
            print("Turned into " + current + " by the reflector.")
            if first_iteration:
                input()

            current = rotor3.getR(current)
            print("Turned into " + current + " by the third rotor.")
            if first_iteration:
                input()
            current = rotor2.getR(current)
            print("Turned into " + current + " by the second rotor.")
            if first_iteration:
                input()
            current = rotor1.getR(current)
            print("Turned into " + current + " by the first rotor.")
            if first_iteration:
                input()
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
        first_iteration = False
        input()

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
