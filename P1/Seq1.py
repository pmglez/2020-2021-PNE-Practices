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
    NULL_SEQUENCE = "NULL"  # Upper cases because it is a constant
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, strbases=NULL_SEQUENCE):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == Seq.NULL_SEQUENCE:
            print("NULL Seq created")
            self.strbases = strbases
        else:
            if Seq.is_valid_sequence_2(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = Seq.INVALID_SEQUENCE
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
            print("Sequence", i, ": ( Length:", list_sequences[i].len(), " )", list_sequences[i])

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
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return a, c, g, t
        else:
            for ch in self.strbases:
                if ch == "A":
                    a += 1
                elif ch == "C":
                    c += 1
                elif ch == "G":
                    g += 1
                elif ch == "T":
                    t += 1
            return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        return {"A": a, "C": c, "G": g, "T": t}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            return self.strbases[:: -1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            complement = ""
            for ch in self.strbases:
                if ch == "A":
                    complement += "T"
                elif ch == "C":
                    complement += "G"
                elif ch == "G":
                    complement += "C"
                elif ch == "T":
                    complement += "A"
            return complement


def test_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid sequence")
    return s1, s2, s3
