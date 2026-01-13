# LeetCode Pattern Detective

LeetCode Pattern Detective is a Flask-based web application that identifies the **algorithmic pattern** behind LeetCode problems instead of merely presenting solutions.

The project focuses on **pattern recognition and reasoning**, which are the most critical skills evaluated during technical interviews.

---

## Motivation

Most LeetCode repositories consist of lists of solved problems and code snippets.  
However, in real interviews, the primary challenge is not writing code, but:

- Recognizing the correct algorithmic pattern
- Explaining why it is optimal
- Justifying why brute-force approaches are inefficient
- Communicating trade-offs clearly

This project was built to model and demonstrate that thought process.

---

## What the Application Does

For a given LeetCode problem, the application:

1. Analyzes the problem title and constraints  
2. Applies rule-based heuristics to detect algorithmic patterns  
3. Identifies the most appropriate pattern  
4. Explains why the pattern applies  
5. Shows brute-force versus optimized approaches  

---

## Supported Patterns (v1)

- Sliding Window  
- Hash Map  
- Two Pointers  

The design is intentionally extensible to support additional patterns such as Binary Search, Dynamic Programming, and Greedy algorithms.

---

## Example Output

