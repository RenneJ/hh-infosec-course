# Summary

## Applied Cryptography: Chapter 1: Foundations (Schneier, 2015)

### 1.1 Terminology
 
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
- encrypting key and decrypting are the same or one can be derived from the other
- also called secret-key algorithms, single-key algorithms, or one-key algorithms
- sender and receiver need to agree on a key before communications
 
**Public-key Algorithms**
- also called asymmetric algorithms
- encrypting key and decrypting are different and one cannot feasibly be derived from the other
- encrypting key can be published and is often called public key
- decrypting key is often called private key

**Cryptanalysis**
- the science of recovering the plaintext without the key or recovering the key itself
- if the key is recovered by a threat actor without cryptanalysis it is called a compromise
- there are 4 main categories of cryptanalysis attack:
  - Ciphertext-only attack, access only to ciphertext
  - Known-plaintext attack, access to ciphertext and plaintext
  - Chosen-plaintext attack, same as above but also access to dictate the plaintext
  - Adaptive-chosen-plaintext attack, same as above but also get feedback of previous encryption
 > "Good cryptographers rely on peer review to separate the good algorithms from the bad."

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
  - only one-time pads are unconditionally secure
- cryptography is more concerned making cryptosystems computationally secure or strong
  - it cannot be broken using available resources

### 1.2 Steganography

Steganography is hiding messages inside other messages (e.g. invisible ink writing in a letter, slight differences in handwriting etc.)

Recently the medium for steganographic messages has been images. Changing choice bits of the image won't impact the look of the image noticably but the receiver will be able to read the hidden message.

### 1.3 Substitution ciphers and transposition ciphers

Ye olde algorithms substituted a character and/or transposed it in a message.

Simple substitution ciphers can be easily broken (especially by a computer). It doesn't hide the frequency of the letters.

Transposition ciphers shuffle the letters of the plaintext.

### 1.4 Simple XOR

XOR is the exclusive-or operator. 
- symbol ⊕ in mathematics
- symbol ^ in C (and many other programming languages e.g. python, java)

XOR is a trivial encryption as it can easily be decrypted without the knowledge of the key. XORing the same value twice returns the original plaintext.

My quick example and let's remember that *EK(P)=C*:

*P* = 00101011

*K* = 11100011

*E* = XOR

*C* = 00110111

### 1.5 One-time pads

The perfect encryption - one-time pad. For a one-time pad:
- the key needs to be securely delivered between the sender and recipient
- the key nor any of it's components must not be used again
- the key must be randomly generated

Following these requirements you can establish impenetrable communications.

Problems:
- the key needs to be the same size as plaintext, so long messages are not necessarily feasible
- randomly generating numbers (or anything) is not as easy as it sounds

What makes one-time pads so great:

> "Since every plaintext message is equally possible, there is no way for the cryptanalyst to determine which plaintext message is the correct one."

### 1.6 Computer algorithms

Three most common cryptographic algorithms:
- DES (Data Encryption Standard) is the most popular computer encryption algorithm. Symmetrical.
- RSA (Rivest, Shamir, Adleman) is the most popular public-key algorithm. Asymmetrical.
- DSA (Digital Signature Algorithm) is a public-key algorithm. Only for signatures, not encyprition. Asymmetrical.

# Frequency distribution

Frequency distribution refers to the occurrence of characters in a language. In English the six most common characters are ETAOIN.

In Finnish: AITNES (Pääkkönen, 1991)

# Password Manager: KeePassXC

### ![h4_keepassxc_intro](https://github.com/RenneJ/hh-infosec-course/assets/97522117/02a433c8-cbc2-4000-8c30-e1f7c3f7cfbb)
> Figure 1. Basic information about KeePassXC

# Sources

Pääkkönen, M. 1991. A:sta Ö:hön. Suomen kielen yleisyystilastoja. Kielikello 1/1991. (In Finnish)

Schneier, B. 2015. Applied Cryptography: Protocols, Algorithms and Source Code in C, 20th Anniversary Edition. New York: Wiley.


