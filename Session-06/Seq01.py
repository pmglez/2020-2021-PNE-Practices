import termcolor

def generate_seqs(pattern, number):
    # A, 3
    list_seq = []
    for i in range(0, number):
                                # A i = 0 -> A
                                # A i = 1 -> AA
                                # A i = 2 -> AAA
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if Seq.is_valid_sequence_2(strbases):
            print("New sequence created!")
            self.strbases = strbases
        else:
            self.strbases = "Error"
            print("INCORRECT Sequence detected")

    @staticmethod
    def is_valid_sequence_2(bases):
        for ch in bases:
            if ch != "A" and ch != "C" and ch != "G" and ch != "T":
                return False
        return True

    def is_valid_sequence(self):
        for ch in self.strbases:
            if ch != "A" and ch != "C" and ch != "G" and ch != "T":
                return False
        return True

    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            print("Sequence", i, ": (Length:", list_sequences[i].len(), ")", list_sequences[i])

    @staticmethod
    # For printing in colours
    def print_seqs_2(list_sequences):
        for i in range(0, len(list_sequences)):
            text = "Sequence " + str(i) + ": ( Length: " + str(list_sequences[i].len()) + " ) " + str(list_sequences[i])
            termcolor.cprint(text, "blue")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)
