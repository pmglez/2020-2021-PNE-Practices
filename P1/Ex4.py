from Seq1 import Seq

print("-----| Practice 1, Exercise 4 |------")

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print("Sequence " + str(1) + ": ( Length: " + str(s1.len()) + " ) " + str(s1))
print("Sequence " + str(2) + ": ( Length: " + str(s2.len()) + " ) " + str(s2))
print("Sequence " + str(3) + ": ( Length: " + str(s3.len()) + " ) " + str(s3))
