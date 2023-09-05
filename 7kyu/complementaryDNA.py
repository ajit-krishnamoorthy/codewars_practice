#In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
def DNA_strand(dna):
    newDna = dna.replace("A", "temp")
    newDna = newDna.replace("T", "A")
    newDna = newDna.replace("temp", "T")
    newDna = newDna.replace("C", "temp")
    newDna = newDna.replace("G", "C")
    newDna = newDna.replace("temp", "G")
    return newDna