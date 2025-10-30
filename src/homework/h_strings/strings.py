def get_hamming_distance(dna1: str, dna2: str) -> int:
    if len(dna1) != len(dna2):
        raise ValueError("DNA strings must be of equal length.")
    distance = 0
    i = 0
    n = len(dna1)
    while i < n:
        if dna1[i] != dna2[i]:
            distance += 1
        i += 1
    return distance


def get_dna_complement(dna: str) -> str:
    rev_comp = ""
    i = 0
    n = len(dna)
    while i < n:
        ch = dna[i]
        if ch == 'A':
            comp = 'T'
        elif ch == 'T':
            comp = 'A'
        elif ch == 'C':
            comp = 'G'
        elif ch == 'G':
            comp = 'C'
        else:
            raise ValueError(f"Invalid DNA symbol: {ch}")
        rev_comp = comp + rev_comp
        i += 1
    return rev_comp
