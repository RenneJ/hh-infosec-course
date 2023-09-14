# Summary

## Applied Cryptography: Chapter 1: Foundations (Schneier, 2015)

### 1.1 Terminology

**Sender and Receiver**
  - message is sent and it is important that it's sent securely.
 
**Messages and Encryption**
  - message is called plaintext or cleartext (symbol for message *M*, plaintext *P*)
  - hiding the message's information is called encryption (symbol for encryption *E*)
  - encrypted text is called ciphertext (symbol for ciphertext *C*)
  - cryptography = how to keep messages secure
  - cryptanlysis = how to break ciphertext
  - cryptology = field of study (maths) that covers cryptography and cryptanalysis

**Authentication, Integrity, and Nonrepudiation**
  - Authentication: the receiver knows that the sender is who they say they are
  - Integrity: message stays the same all the way to the receiver
  - Nonrepudiation: the sender must not be able to claim that they didn't send the message
 
**Algorithms and Keys**
  - cryptographic algorithm = mathematic function for encrypting and decrypting
  - if algorithm's security depends on its secrecy it is called a restricted algorithm
    - inadequate by modern standards
  - modern algorithms use a key (symbol for key *K*)
    - key is a number
    - the range of numbers where the key is drawn is called the keyspace
    - key is used by encrypting and decrypting functions
    - this way the algorithm can be published and peer reviewed

**Symmetric Algorithms**
  - encrypting key and decrypting are the same or one can be derived form the other
  - also called secret-key algorithms, single-key algorithms, or one-key algorithms
  - sender and receiver need to agree on a key before communications
 
**Public-key Algorithms**
  - also called asymmetric algorithms
  - encrypting key and decrypting are different and one cannot feasibly be derived from the other
  - encrypting key can be published often called public key
  - decrypting key is often called private key

**Cryptanalysis**
- the science of recovering the plaintext without the key or recovering the key itself
- if the key is recovered by a threat actor without cryptanalysis it is called a compromise
- there are 4 main categories of cryptanalysis attack:
  - Ciphertext-only attack, access only to ciphertext
  - Known-plaintext attack, access to ciphertext and plaintext
  - Chosen-plaintext attack, same as above but also access to dictate the plaintext
  - Adaptive-chosen-plaintext attack, same as above but also get feedback of previous encryption
- "Good cryptographers rely on peer review to separate the good algorithms from the bad."

**Security of Algorithms**
- algorithms have varying levels of security
  - sometimes "good enough" works fine, depending on the message
- categories of breaking an algorithm
  - total break, cryptanalyst finds the key
  - global deduction, cryptanalyst finds an alternate working algorithm
  - instance (or local) deduction, cryptanalyst finds the plaintext
  - information deduction, partial infomration about plaintext or key
- most cryptosystems are breakable in a ciphertext-only attack
  - the key can be brute forced
- 

### 1.2 Steganography

### 1.3 Substitution ciphers and transposition ciphers

### 1.4 Simple XOR

### 1.5 One-time pads

### 1.6 Computer algorithms

### 1.7 Large numbers

### Source

Schneier, B. 2015. Applied Cryptography: Protocols, Algorithms and Source Code in C, 20th Anniversary Edition. New York: Wiley.
