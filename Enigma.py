# Jacob Faulk

from Rotor import Rotor
from Plugboard import Plugboard


def main():
    plaintext = input(
        "Welcome to the Enigma Machine emulator. Enter plaintext to be encrypted.\n")

    plaintext = plaintext.upper()
    print("Plaintext: " + plaintext)

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


if __name__ == "__main__":
    main()
