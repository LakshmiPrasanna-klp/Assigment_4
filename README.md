# CS5710 Machine Learning - Homework 2 Solutions

This repository contains solutions to Homework-4 for **CS5710 Machine Learning**.  


---
##  Student Info
- Name: Lakshmi Prasanna Komirisetty
- Student ID : 700772585
- Course: CS5710 Machine Learning
- Semester: Fall 2025

---

## Contents
- `Homework-4__Solutions.docx` → Full written solutions
Part A - Calculations  answers attached in pdf file format
Part B — Short Answer
Q1.
a) Agglomerative Hierarchical Clustering:
This is a bottom-up clustering approach. Each data point starts as its own cluster, and in each iteration, the two most similar clusters are merged based on a chosen distance metric until all points belong to one cluster. The hierarchy can be represented using a dendrogram.
b) Divisive Hierarchical Clustering:
This is a top-down approach. All data points start in one large cluster, which is recursively split into smaller clusters until each data point is in its own cluster.
c) Which one is more commonly used and why:
Agglomerative clustering is more commonly used because it is simpler to implement and computationally more efficient than divisive clustering. Divisive methods require exploring many possible ways to split clusters, which is computationally expensive.
Q2.
a) Inter-cluster distance:
Inter-cluster distance should be maximized to ensure clusters are well-separated from each other, meaning that different clusters are distinct and not overlapping.
b) Intra-cluster distance:
Intra-cluster distance should be minimized to ensure that points within the same cluster are close together, making each cluster compact and cohesive.
Q3.
a) Definitions:
• Single Link: Distance between the closest pair of points in two clusters.
• Complete Link: Distance between the farthest pair of points in two clusters.
• Average Link: Average distance between all pairs of points from two clusters.
b) Strength and Weakness of Single-Link Clustering:
• Strength: Can detect clusters of arbitrary shape and handle noise well.
• Weakness: Can suffer from the 'chaining effect,' where clusters become long and thin due to single connections between distant points.
Q4.
a) Role of Tokenization:
Tokenization is the process of breaking text into smaller units called tokens (e.g., words, punctuation). Example: 'I love apples' → ['I', 'love', 'apples'].
b) Stemming vs Lemmatization:
• Stemming: Faster but less accurate; it removes word suffixes without understanding context (e.g., 'running' → 'run').
• Lemmatization: Slower but more accurate; it uses vocabulary and morphological analysis to return the base form of a word.
Q5.
a) Word Sense Ambiguity:
Occurs when a word has multiple meanings depending on context. Example: The word 'bank' can mean a financial institution or the side of a river.
b) Pronoun Reference Ambiguity:
Happens when it's unclear which noun a pronoun refers to. For example, in 'John met Alex and he smiled,' it's ambiguous whether 'he' refers to John or Alex, which can confuse NLP models.
Q6.
a) Dependency in POS Tagging:
NLP tasks like POS tagging cannot be solved by predicting each token independently because the part of speech of a word often depends on its context and neighboring words.
b) Example of Mutual Dependency:
In the sentence 'They can fish,' the word 'can' could be a verb or a noun depending on 'fish'. The correct interpretation of each word depends on the other.


# part-c Code Execution
Requirements
Python 3.10 or higher is required, along with the spaCy library. Install spaCy with:
1)pip install spacy
2)python -m spacy download en_core_web_sm






