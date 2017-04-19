dna_strings='''ACATAACCTCCACCAGGATCCAAGTGTATCTAGTTTGCCTCGGCTAGGAAACGGTTATGCTCGTCGGCTTTGCCGAGTGAATCTGGGGTCAACACGCTGCTATACGGGCCATCACTTTACTATTCTCTGACATGGGGGACATAGTGAACTAGGTATGTATGTCCCTTCGCAATCGTTATATTAGCTTCGCACATCGACACCTCTCTTAAGAACACAACTAAACATCAAAATCGAAACTACACGATTTATCTCGGACTACTCATGTCGGCAAATTCTCACTGCCAGCCACATTCGCTAACGACTACCTACCACCTGGCACTGCCCGCGCCGTAGTTCTAGCGACACTCGGACTGACTTCCGGTTAACCAATAGTTAGCTGGGCTGATTCATATACGCAAGACGTTTTTGCCATCTACGGGCAGCAAAAACTTTTGATTCGAGGGTTCCATCACAGGCCCCGCAGGTGCACTTTAATTGTCGACCTTCTATATCGAGAAAAGTGGAGTACGACTACAAATCGAAGGGAGGGTAGCGTGTGAACCGGTGAGATAGTAGGGCTCTCACAGCCTTTACTGACGAAACGTGTTGATTGCCATCAACATGGACGAATTAACGACTCCGCCCGGCCGCAGAGGTGTCCCAGTCGTCCCTTGTGTTCCTACAGTGACTGGTCTGTATTTGATTGAAAGCGAGTTAGCGACAATCATGTCACCTTCGAACGGTTCTTGAAGTTTTTAGCTTTGGCCGTTAAAACCTAATGATGTACACCAGGTAGGTTGTCTATTCTGGTTGCTCCCCTACGTAACCGATCTCTCATTAACCGGAATACGTTCACCGTAATTACGTTCCACGAACAGTTCAAACTTAGCCCGCACATGACTGGTCTCGTGGTATACCACATTATACACGTGGCATCCAGGCACGTGGTTTAGCATCCAAGTTCTCATACTAAATAGCGTTCTCGTAGAACA
ACCAAAAACTCACTAGGATAAGATCCATTCCGGCTAGCATACAAACGTCGCTCCTATTGCTGGAACTCAGGGGGGTTTTACTCTTGGGTGTATTTTCCTATAGATGTCCGCCAAATGCTATAGCGGCCGACAAGGGCGCGGGACGTGATTCGTTCAGCCGGTCTTTCAGAGGTCCTCCAAACACCTTATCATATCAATTCCGCTCGAGAGTGGTCTAACAGGGCTCCGTTCTGGAAATTCCTCCGCACTCCCCTACTACACATGTGCTCACACCCTGTCATTCCTCCAAAGATGGTATCGCCCAACCATTACCCTACACGGCACAGGCAGTGGATCGTACGCCACTCGTACCCTCTATCTGTGTAAAAACAATTGCCAAGGATTCTGCATCCATACCTGCCGTTGTCGCCCGCTAGGTGCAGTAGCTACTGCATAAACTGCGGGTCCTTGTTAAGTGCAAGCGGTGGCCTCAAATAGACCCCTTAGCCGCCAGATAACACTGGAGTCCGTGGTTGCATCACAAGCAGTAGAACATGTGCATCGATGACAGCGTATGGGTGATCCACCCGAGACGTACGCAACGTGTGGATATGGTTCCACACGAAGGCTCAAAACTCTCAGATCGTATTGAGACCCCAGGCCCAATTCCCCTACATGTACACATTATCTGCTTGGAATTTTTTTCAGTCCGAGTTAGCTAAAAAAGGGTTGACACCGGGCCCTTCTCGAAATTGCTATATTCGGCCGAAAACACCCACTTATCAGGACCAGGTATCTTGACAGCTGTGATTGCTACATTCCGCTATCGATCAGTCACTAAATCGGATTGTTACCCCATACGAATGCTCAACGTAAAGCTAAGCATGTGCCCTGCAATGAGTCTTGACTTGAGATGCCAGGATGTACACGTTGACTTCAGCCATCAGTTTCTGTATAAGGCTTAATTGACTAATACTCTTGCTCGGGGCTCA
'''

dna_1 = dna_strings.splitlines()[0]
dna_2 = dna_strings.splitlines()[1]
hamming_distance = 0

for i in range (0, len(dna_1)):
    if dna_1[i] != dna_2[i]:
        hamming_distance += 1

print hamming_distance

print len(dna_strings)
print len(dna_1), len(dna_1), len(dna_1)+len(dna_2)
