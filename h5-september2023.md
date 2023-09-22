# Summaries

## Applied Cryptography: Chapter 2: Protocol Building Blocks (Schneier, 2015)

### 2.3 One-way Functions

- Easy to compute and very hard to reverse
  - Hard = it would take millions of years using all current computers
- Example:
  - It's easy to break a plate and very hard to put it back together
- There is no mathematical proof for the existence of one-way functions
- **Trapdoor one-way functions** have secret that can be used to reverse the function
- Example:
  - To disassemble a watch is easy but hard to put back together without a guide (i.e. the secret)

### 2.4 One-way Hash Functions

- Also called:
  - Compression function
  - Contraction function
  - Message digest
  - Fingerprint
  - Cryptographic checksum
  - Message Integrity Check (MIC)
  - Manipulation Detection Code (MDC)
- Is a part of many protocols
- It takes a variable-length input string (**pre-image**) and converts it to fixed-length output string (**hash value**)
- The point is to compare and to validate a candidate pre-image to previously established (real) pre-image
  - It's easy to compute a hash value but hard to reverse it and it's hard to compute a different pre-image with the same hash value as the original
  - A good one-way function is called collision-free
    - Simple XOR is NOT a good one-way function
- Hashes (or fingerprints, checksums etc.) are a good way to validate the authenticities of files

## Phishing through emails (Särökaari, 2018)



# Sources

Schneier, B. 2015. Applied Cryptography: Protocols, Algorithms and Source Code in C, 20th Anniversary Edition. New York: Wiley.

Särökaari, N. 2018. Disobey 2018 - Phishing through email - Niklas Särökaari. Disobey. Video. URL: https://www.youtube.com/watch?v=m9YFJGSHYtY. Accessed: 2023/09/22.
