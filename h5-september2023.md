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

# Sources

Schneier, B. 2015. Applied Cryptography: Protocols, Algorithms and Source Code in C, 20th Anniversary Edition. New York: Wiley.
