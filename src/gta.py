
def count_nucs(DNA):
    counts = {'A':0, 'T':0, 'C':0, 'G':0}

    for c in DNA:
        counts[c] += 1
    return counts


# script called directly, not a library call
# run tests
if __name__ == '__main__':
    dna = 'AGATTCACCGTTAGATC'
    c = count_nucs(dna)
    print(dna, "has the following nucleotide counts", c)
