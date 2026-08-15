"""Rosalind Problem: Consensus and Profile (CONS)
Problem

A collection of DNA strings having the same length is often represented by a profile matrix.

The profile matrix gives the number of times each nucleotide appears at each position in the DNA strings.

The consensus string is formed by taking the most common nucleotide at each position."""
def consensus(profile_matrix):

    consensus_string = ""

    for counts in profile_matrix:

        max_nucleotide = max(counts, key=counts.get)

        consensus_string += max_nucleotide

    return consensus_string

def profile(motif):
    n=len(motif[0])
    count=[]
    for i in range(n):
        counts={'A':0,'T':0,'G':0,'C':0}
        for m in motif:
            counts[m[i]]+=1
        count.append(counts)

    return count
motif=["ATCCAGCT",
"GGGCAACT",
"ATGGATCT",
"AAGCAACC",
"TTGGAACT",
"ATGCCATT",
"ATGGCACT"]

count=profile(motif)
print("The Profile:")
print(count)
print("The consensus string is:")
print(consensus(count))