"""Finding a Motif in DNA (SUBS)
Problem

A substring of a string is a contiguous block of symbols contained within the string.

Given two DNA strings s and t, find all locatioTns of t as a substring of s.

In this problem, all locations should be reported, including overlapping occurrences."""

DNA =input("Enter DNA sequence:") #"GATATATGCATATACT"
motif =input("Enter motif:") #"ATAT"


for i in range(len(DNA) - len(motif) + 1):

    if DNA[i:i+len(motif)] == motif:
        print(i+1, end=" ")