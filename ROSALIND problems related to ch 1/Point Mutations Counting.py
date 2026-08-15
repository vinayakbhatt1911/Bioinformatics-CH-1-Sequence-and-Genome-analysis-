"""Rosalind: Counting Point Mutations (HAMM)
Problem

Given two DNA strings s and t of equal length, compute the Hamming Distance between them.

The Hamming Distance is the number of corresponding symbols that differ between two strings."""

DNA1=input("Enter DNA seq 1:")
DNA2=input("Enter DNA seq 2:")
count=0
for i in range(len(DNA1)):
        if(DNA1[i]!=DNA2[i]):
            count+=1
print("Hamming distance is :",count)