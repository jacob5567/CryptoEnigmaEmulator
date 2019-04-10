# Jacob Faulk


def main():
    plaintext = "hello there"#input("Welcome to the Enigma Machine emulator. Enter plaintext to be encrypted.\n")
    plaintext = plaintext.upper()
    print(plaintext)
    print("The first step in encoding a message in the Enigma involves a plugboard.")
    print("This would be set every day and sent out to the German soldiers in WWII.")
    print("For this example, the plugboard will be set as follows:")
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    plugboard_locations = list("ETWAYDSVFPRCQJXOGUHZNLIMBK")
    plugboard = dict(zip(alphabet, plugboard_locations))
    for key in plugboard.keys():
        print(key + ' ', end='')
    print()
    for value in plugboard.values():
        print(value + ' ', end='')
    print()
    print("In this example, " + alphabet[0] + " corresponds to " + plugboard_locations[0] + ", " + alphabet[1] + " corresponds to " + plugboard_locations[1] + ", and so on.")

    print("The Enigma would convert your first letter, " + plaintext[0] + ", to " + plugboard[plaintext[0]] + ".")

    # Note that the print statements will be expanded on in the future, for this rough draft, I will just work on the internals of the Enigma
    rotor_1 = dict(zip(list("HLKEGUYWRDCNTBFVQIZPMXSAJO"), list("GWHDISFZYJATEPCLVUNXMQRKOB")))
    rotor_2 = dict(zip(list("XRUPTZEFDSHCMNOJQWLYVGIABK"), list("OPTNYFGUERBQSZWAHJMVLKDXIC")))
    rotor_3 = dict(zip(list("THXIJYKMZDAOWVSEQFBPUNRGCL"), list("VYCKSURPTLNQBMJHDEFXOWGZAI")))

    print_rotor(rotor_1)
    rotor_1 = rotate_rotor(rotor_1)
    print_rotor(rotor_1)
    # for character in plaintext:
    #     current = character
    #     print("Current character: " + current)
    #     current = plugboard[current]
    #     print("Turned into " + current + " by the plugboard.")
    #     current = rotor_1[current]
        
        

def rotate_rotor(rotor):
    keys = list()
    values = list()
    for key, value in rotor.items():
        keys.append(key)
        values.append(value)
    
    # rotating the rotor
    first_char = values[0]
    for i in range(len(values) - 1):
        values[i] = values[i + 1]
    values[len(values) - 1] = first_char

    return dict(zip(keys, values))


def print_rotor(rotor):
    for key in rotor.keys():
        print(key + ' ', end='')
    print()
    for value in rotor.values():
        print(value + ' ', end='')
    print()

if __name__ == "__main__":
    main()
