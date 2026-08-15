"""Rosalind EDIT: Edit Distance
Problem

Given two strings, find the minimum number of edit operations needed to transform the first string into the second string.

The allowed operations are:

Insertion: insert a symbol.
Deletion: delete a symbol.
Substitution: replace one symbol with another.

Each operation has a cost of 1.

Sample Dataset"""

def matrix_initialize(seq1, seq2):

    matrix = []

    for i in range(len(seq1) + 1):

        row = []

        for j in range(len(seq2) + 1):

            if i == 0:
                row.append(j)

            elif j == 0:
                row.append(i)

            else:
                row.append(0)

        matrix.append(row)

    return matrix


def fill_matrix(matrix, seq1, seq2):

    for i in range(1, len(seq1) + 1):

        for j in range(1, len(seq2) + 1):

            # Diagonal: Match or Substitution
            if seq1[i - 1] == seq2[j - 1]:

                diagonal = matrix[i - 1][j - 1]

            else:

                diagonal = matrix[i - 1][j - 1] + 1

            # Deletion
            up = matrix[i - 1][j] + 1

            # Insertion
            left = matrix[i][j - 1] + 1

            # Choose minimum edit cost
            matrix[i][j] = min(diagonal, up, left)

    return matrix


def get_edit_distance(matrix):

    return matrix[-1][-1]


def get_input():

    seq1 = input("Enter Sequence 1: ").strip().upper()
    seq2 = input("Enter Sequence 2: ").strip().upper()

    return seq1, seq2


def main():

    seq1, seq2 = get_input()

    matrix = matrix_initialize(seq1, seq2)

    matrix = fill_matrix(matrix, seq1, seq2)

    distance = get_edit_distance(matrix)

    print("\nEdit Distance:", distance)


if __name__ == "__main__":
    main()