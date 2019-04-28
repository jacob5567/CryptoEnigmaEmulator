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
    plugboard_locations = list("ETWAYDSVFPRCQJXOGUHZNLIMBK")
    plugboard = dict(zip(alphabet, plugboard_locations))

    plugboard = Rotor(alphabet, plugboard_locations)

    print(plugboard)

    print("In this example, " + plugboard.side1[0] + " corresponds to " + plugboard.side2[0] +
          ", " + plugboard.side1[1] + " corresponds to " + plugboard.side2[1] + ", and so on.\n")

    print("The Enigma would convert your first letter, " +
          plaintext[0] + ", to " + plugboard[plaintext[0]] + ".\n\n")

    # Note that the print statements will be expanded on in the future, for this rough draft, I will just work on the internals of the Enigma
    rotor_1 = Rotor(list("HLKEGUYWRDCNTBFVQIZPMXSAJO"),
                    list("GWHDISFZYJATEPCLVUNXMQRKOB"))
    rotor_2 = Rotor(list("XRUPTZEFDSHCMNOJQWLYVGIABK"),
                    list("OPTNYFGUERBQSZWAHJMVLKDXIC"))
    rotor_3 = Rotor(list("THXIJYKMZDAOWVSEQFBPUNRGCL"),
                    list("VYCKSURPTLNQBMJHDEFXOWGZAI"))

    rotor_1_backup = rotor_1.copy()
    rotor_2_backup = rotor_2.copy()
    # rotor_3_backup = rotor_3.copy()

    reflector = Rotor(list("ZEFUHBDMNIJGACVTQRWYXOSLPK"),
                      list("GBURKVPSFHJTMXAIEZLNWODQYC"))

    final_result = ""

    for character in plaintext:
        if character in alphabet:
            current = character
            print("Current character: " + current)
            current = plugboard[current]
            print("Turned into " + current + " by the plugboard.")
            current = rotor_1[current]
            print("Turned into " + current + " by the first rotor.")
            rotor_1.rotate()
            print("First rotor rotated.")

            # this rotates the other rotors when the first one makes a complete rotation
            if rotor_1 == rotor_1_backup:
                rotor_2.rotate()
                print("Second rotor rotated.")
                if rotor_2 == rotor_2_backup:
                    rotor_3.rotate()
                    print("Third rotor rotated.")

            current = rotor_2[current]
            print("Turned into " + current + " by the second rotor.")
            current = rotor_3[current]
            print("Turned into " + current + " by the third rotor.")

            # now the letter is reflected back through the same rotors
            current = reflector[current]
            print("Turned into " + current + " by the reflector.")

            # TODO make reverse versions of the rotors
            current = rotor_3.getR(current)
            print("Turned into " + current + " by the third rotor.")
            current = rotor_2.getR(current)
            print("Turned into " + current + " by the second rotor.")
            current = rotor_1.getR(current)
            print("Turned into " + current + " by the first rotor.")
            rotor_1.rotate()
            print("First rotor rotated.")  # TODO see if this is accurate
            if rotor_1 == rotor_1_backup:
                rotor_2.rotate()
                print("Second rotor rotated.")
                if rotor_2 == rotor_2_backup:
                    rotor_3.rotate()
                    print("Third rotor rotated.")

            # TODO make reverse version of the plugboard
            current = plugboard[current]
            print("Turned into " + current + " by the plugboard.")
            print("Final character encryption: " + current + "\n\n")
            final_result += current
        else:
            final_result += character

    print("The final result is: " + final_result)
    # TODO decryption
    # TODO final presentation of the ciphertext


if __name__ == "__main__":
    main()
