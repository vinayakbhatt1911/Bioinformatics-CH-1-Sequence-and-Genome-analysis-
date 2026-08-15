"""Rosalind Problem: Overlap Graphs (GRPH)
Problem

A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row contains the two node labels corresponding to a unique edge.

A directed graph is formed by connecting string s to string t if there is a length k suffix of s that matches a length k prefix of t, where s ≠ t.

Construct the overlap graph of a collection of DNA strings.

For this problem, use:"""

dNA_1=input("Enter seq 1:")
dNA_2=input("Enter seq 2:")
dNA_3=input("Enter Seq 3:")
dNA_4=input("Enter Seq 4:")

dna=[dNA_1,dNA_2,dNA_3,dNA_4]
for i in dna:
    for j in dna:
        if([i]!=[j]):# DNA sequence should not get compare with itself
            if(i[-3:]==j[:3]):
                print(i,"-->",j)



