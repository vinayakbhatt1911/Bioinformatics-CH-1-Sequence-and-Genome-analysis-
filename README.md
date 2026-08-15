# 🧬 Sequence Alignment Algorithms

A collection of classical sequence alignment algorithms and bioinformatics analyses implemented and studied using Python.

This repository covers Dynamic Programming based sequence alignment, Rosalind problems related to sequence comparison, real-world alignment tools, and substitution matrix concepts.

---

## 📚 Topics Covered

### 1. Sequence Alignment Algorithms

- Dot Matrix Method
- Longest Common Subsequence (LCS)
- Needleman-Wunsch Algorithm
- Smith-Waterman Algorithm

These algorithms demonstrate different approaches to comparing biological sequences and identifying similarities between them.

---

### 2. Rosalind Problems

The repository contains Rosalind problems related to sequence comparison and alignment, including:

- Counting Point Mutations (HAMM)
- Profile and Consensus String (CONS)
- Position Weight Matrix (PWM)
- Edit Distance (EDIT)

More alignment-related Rosalind problems will be added as the chapter progresses.

---

### 3. Real Tool Analysis

Practical analysis of real bioinformatics sequence alignment tools:

- EMBOSS Needle
- EMBOSS Water

The same biological sequences were analyzed using real alignment tools to understand the practical application of global and local sequence alignment.

---

### 4. HBB Gene Comparison

Comparative analysis of the **HBB gene** from:

- Human
- Chimpanzee
- Gorilla

Multiple Sequence Alignment was performed using **Clustal Omega** to observe sequence conservation and similarities between the species.

---

### 5. Substitution Matrices

Theory and analysis of protein substitution matrices:

- Substitution Matrix
- PAM
- BLOSUM
- PAM vs BLOSUM

These matrices are important for scoring amino-acid substitutions during protein sequence alignment.

---

# 🧠 Algorithms

## Dot Matrix

A visual method for comparing two sequences by identifying matching positions between them.

## Longest Common Subsequence (LCS)

A Dynamic Programming based method for finding the longest subsequence common to two sequences.

## Needleman-Wunsch

A Dynamic Programming algorithm for **global sequence alignment**.

The algorithm aligns sequences across their complete lengths using match, mismatch and gap scores.

## Smith-Waterman

A Dynamic Programming algorithm for **local sequence alignment**.

It identifies the highest-scoring similar region between two sequences.

---

# 🔬 Global vs Local Alignment

| Feature | Needleman-Wunsch | Smith-Waterman |
|---|---|---|
| Alignment | Global | Local |
| Purpose | Overall sequence similarity | Best similar region |
| Matrix | Scoring matrix | Scoring matrix with zero |
| Traceback starts | Bottom-right cell | Highest-scoring cell |
| Traceback stops | Beginning of matrix | Score = 0 |

---

# 🛠 Technologies & Tools

### Programming

- Python

### Bioinformatics Tools

- Clustal Omega
- EMBOSS Needle
- EMBOSS Water
- Rosalind

---
🧬 Biological Application

Sequence alignment is widely used in:

Comparative genomics
Molecular evolution
Homology detection
Gene analysis
Protein analysis
Mutation analysis
Bioinformatics research

The HBB gene comparison provides a practical example of sequence conservation across primates.

🚀 Future Additions

Planned additions include:

More Rosalind sequence alignment problems
Additional alignment examples
Further real-tool analysis
Protein sequence alignment experiments

👨‍💻 Author

Vinayak Bhatt

B.Tech Biotechnology

Interested in Bioinformatics, Computational Biology and AI/ML applications in Biology.

📌 References
Rosalind
EMBL-EBI EMBOSS Tools
Clustal Omega
