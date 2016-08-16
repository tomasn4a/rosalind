f = open('rosalind_dna.txt', 'r')
s = f.readline()

print(s.count("A"), s.count("C"), s.count("G"), s.count("T"))
