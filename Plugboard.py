# Jacob Faulk


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
