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

    # TODO make plugboard historically accurate
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    plugboard_locations = list("ETWAYDSVFPRCQJXOGUHZNLIMBK")
    plugboard = dict(zip(alphabet, plugboard_locations))

    plugboard = Rotor(alphabet, plugboard_locations)

    print(plugboard)

    print("In this example, " + plugboard.side1[0] + " corresponds to " + plugboard.side2[0] +
          ", " + plugboard.side1[1] + " corresponds to " + plugboard.side2[1] + ", and so on.\n")

    # Rotor(list("HLKEGUYWRDCNTBFVQIZPMXSAJO"), list("GWHDISFZYJATEPCLVUNXMQRKOB"))
    rotor1 = Rotor(rotorNumber=1)
    # Rotor(list("XRUPTZEFDSHCMNOJQWLYVGIABK"), list("OPTNYFGUERBQSZWAHJMVLKDXIC"))
    rotor2 = Rotor(rotorNumber=2)
    # Rotor(list("THXIJYKMZDAOWVSEQFBPUNRGCL"), list("VYCKSURPTLNQBMJHDEFXOWGZAI"))
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

            # now the letter is reflected back through the same rotors
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

            # TODO make reverse version of the plugboard
            current = plugboard.getR(current)
            print("Turned into " + current + " by the plugboard.")
            print("Final character encryption: " + current + "\n\n")
            final_result += current
        else:
            final_result += character

    print("The final result is: " + final_result)
    # TODO final presentation of the ciphertext


if __name__ == "__main__":
    main()
