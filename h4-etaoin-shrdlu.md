# Summary

## Applied Cryptography: Chapter 1: Foundations (Schneier, 2015)

### 1.1 Terminology
 
**Messages and Encryption**
- message is called plaintext or cleartext (symbol for message *M*, plaintext *P*)
- hiding the message's information is called encryption (symbol for encryption *E*)
- encrypted text is called ciphertext (symbol for ciphertext *C*)
- cryptography = how to keep messages secure
- cryptanalysis = how to break ciphertext
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
> Figure 1. Basic information about KeePassXC. Src: https://keepassxc.org/

KeePassXC offers protection against password attacks. Especially brute-force and dictionary attacks.

With KeePassXC you can generate safe passwords to all your different accounts. This helps securing your other accounts if one gets compromised.

You still need to be aware of phishing attempts. KeePassXC doesn't do the critical thinking that humans are capable of.

KeePassXC encrypts the database of your passwords with AES256 or Twofish block cipher. The master password (your database password) is strengthened by key transformations. Also the key file may be filled with arbitrary number of bytes or YubiKey to increase security. Further reading:
- AES256 https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
- Twofish https://en.wikipedia.org/wiki/Twofish
- YubiKey https://docs.yubico.com/hardware/yubikey/datasheet/_static/YubiKey_technical_data_sheet.pdf

KeePassXC is licensed under GPLv3 (GNU General Public License). This means users can use it how they want, change it how they want, share it and share the changes on the condition that you don't change the license and you provide clear access to the source code.

### ![h4_gpl](https://github.com/RenneJ/hh-infosec-course/assets/97522117/d118419a-be03-4c28-a998-c6a3cb814c99)
> Figure 2. GPL Foundations. Src: https://www.gnu.org/licenses/quick-guide-gplv3.html

All the data encrypted by KeePassXC is stored locally. When creating a KeePass database the UI prompts you to specify the location. It will be stored with **.kdbx** extension.

If you wish to use KeePassXC on different platforms and devices you can upload the database to cloud yourself or use any method of file sharing you see fit (e.g. USB memory device).

# Decrypting substitution cipher

What's given:
- sender's identity is known
- ciphertext is substitution cipher
- message is in English (ETAOIN SHRDLU mnemonic is valid)

Initial assumptions:
- the last substring (when substring separator is whitespace) is most likely an URL
- the domain extension is .com (.org is unlikely because the characters O and G would not be substituted in the message)

> *C* = (HDMH'B TH. KWU'YI AWR WSSTOTMJJK M OWQINYIMLIY! MB KWU BII, BTGPJI BUNBHTHUHTWA OTPDIYB OMA NI NYWLIA RTHD SYIEUIAOK MAMJKBTB. BII KWU MH DHHP://HIYWLMYCTAIA.OWG)

> *D* = frequency analysis({'H': 11, 'D': 4, 'M': 10, 'B': 10, 'T': 10, 'K': 6, 'W': 10, 'U': 6, 'Y': 8, 'I': 16, 'A': 8, 'R': 2, 'S': 3, 'O': 6, 'J': 4, 'Q': 1, 'N': 4, 'L': 3, 'G': 2, 'P': 3, 'E': 1, 'C': 1})

First run using initial assumptions yields the following:

> *P* = (THMT'B TT. KOU'YI AOR OSSTCTMJJK M COQINYIMLIY! MB KOU BII, BTMPJI BUNBTTTUTTOA CTPHIYB CMA NI NYOLIA RTTH SYIEUIACK MAMJKBTB. BII KOU MT HTTP://TIYOLMYCTAIA.COM)

Using the mnemonic ETAOIN (where T has already been mapped to *C*(H) one can substitute the most frequent letter *C*(I) with E and third most frequent letter *C*(M) with A (10 occurrences *C*(M), *C*(B) and *C*(T); *C*(W) has been mapped in the initial assumption). The result: 

> *P* = THAT'B TT. KOU'YE AOR OSSTCTAJJK A COQENYEALEY! AB KOU BEE, BTMPJE BUNBTTTUTTOA CTPHEYB CAA NE NYOLEA RTTH SYEEUEACK AAAJKBTB. BEE KOU AT HTTP://TEYOLAYCTAEA.COM

From here a person who knows English and knows who the sender is can substitute remaining charcters easily and very likely correctly. E.g. first word is THAT'S and the URL at the end is TEROKARVINEN.COM.

I wrote a short program to help me with the decrypting. The code serves more as a documentation of workflow rather than a functioning program. It sped the trials of individual substitutions. It's provided in the main branch of this repo ([h4_code.py](https://github.com/RenneJ/hh-infosec-course/blob/main/h4_code.py))

# Password manager demo: KeePassXC

I chose KeePassXC because of Tero's recommendation. Furthermore KeePassXC uses no clouds, no 3rd parties and is open source. These things make it more trustworthy in my eyes.

I began working on this demo on my home desktop (Win11). My goal is to synchronise my password database with my laptop (Ubuntu 22.04) as well.

Before any computer processes I read through the KeePassXC [Starting Guide](https://keepassxc.org/docs/KeePassXC_GettingStarted). I also referred to the more detailed [User Guide](https://keepassxc.org/docs/KeePassXC_UserGuide) many times throughout the steps of this demo.

### 1. Download and install (Win11)

I downloaded the latest KeePassXC version (2.7.6) from the official organisation webpage. In figure 3 the PGP Signature and SHA-256 Digest refer to verification of the downloaded software's authenticity and integrity. KeePassXCTeam assures that it's not necessary to verify signatures if you used the official website to download the program. I chose to believe them and proceeded with installation.

### ![h4_keepass_dl](https://github.com/RenneJ/hh-infosec-course/assets/97522117/5ff0ea6f-ad10-4e34-9da9-e627f70a7227)
> Figure 3. View of KeePassXc download page. Src: https://keepassxc.org/download/#windows

The installation was effortless with the installation wizard. The only things requiring user input was determining the installation path and agreeing to GPLv3. As an added security feature KeePassXC GUI becomes hidden when you try to take screenshot. For the purpose of this demo I set it off. Let's just be careful with what we take screenshots of!

### ![h4_keepassxc_start](https://github.com/RenneJ/hh-infosec-course/assets/97522117/2a2a833b-5d82-42b8-aa10-084ecd84a33a)
> Figure 4. View of KeePassXC application GUI startup. No databases are done yet.

### 2. Creating a new database

Let's start by clicking *Create new database*. You can name your database and a description to it. Description is not manadatory, default name is *Passwords*. After naming you are prompted to set your encryption preferences (figure 5). It is not recommended to make changes to these settings. Increasing the Decryption Time slider increases the level of security but also increses the time it takes to open the database.

Again I trust the guidance of KeePassXC Team. I keep the default settings.

### ![h4_keepassxc_encrypt_set](https://github.com/RenneJ/hh-infosec-course/assets/97522117/495aacc2-8d73-43bf-9c58-be392cb7ff5f)
> Figure 5. View of default Encryption Settings.

 After clicking *Continue* you are presented with an **IMPORTANT PART**. Either choose carefully your own master password or use a random generated password (by clicking the die symbol next to the eye symbol). If this password is lost you might lose access to your *Passwords* database for good. It is recommended that you make note of your password. I'm not telling what I chose to do. What would you do?

### ![h4_keepassxc_db_creds](https://github.com/RenneJ/hh-infosec-course/assets/97522117/fce19554-3ca2-4aaf-b71f-e77ba9d9d43d)
> Figure 6. View of Database Credentials input window.

### 3. Browser extension

After setting up the database navigate to your browser's extension/addon store and install KeePassXC-Browser. Checking the publisher name, download count and reviews gives you good indication that you are installing the right extension. Add the extension to your browser.

Then open your KeePassXC and go to Tools > Setting and on the sidebar Browser Integration (figure 7). I followed the KeePassXC [Getting Started Guide](https://keepassxc.org/docs/KeePassXC_GettingStarted#_setup_browser_integration). Choose your browser and tick the boxes. Restart your browser and establish connection between browser and database. You are prompted to name the connection. Using an existing name for the connection overwrites it.

### ![h4_keepassxc_browser_integration](https://github.com/RenneJ/hh-infosec-course/assets/97522117/06fdfc0e-641a-48e0-afd9-2148e3aff0ba)
> Figure 7. View of Browser Integration.

### 4. Let's try it!

For this demo I'll make a new account to reddit.com using KeePassXC browser extension.

First I created a new username (valid for the website) and after that I opened KeePassXC > New Entry. There I filled relevant fields and generated a new password which I copied to reddit webpage sign-up window. After creating a new entry and a new account I log off of reddit. Then I use the KeePassXC-browser extension's integration and can simply click the KeePassXC icon durin sign in. It will prompt you to select allowed details for the current URL. Detailed steps are [here](https://keepassxc.org/docs/KeePassXC_GettingStarted#_adding_an_entry).

### ![h4_keepassxc_aybabtu](https://github.com/RenneJ/hh-infosec-course/assets/97522117/eadca115-841f-476a-a0cc-1aa486c642bd)
> Figure 8. Reddit's log in view with KeePassXC auto-fill used.

# Sources

Smith, B. 2022. A Quick Guide to GPLv3. https://www.gnu.org/licenses/quick-guide-gplv3.html. Read: 2023/09/15

KeePassXC Team 2023. Documentation and FAQ. https://keepassxc.org/docs/. Read: 2023/09/15

Pääkkönen, M. 1991. A:sta Ö:hön. Suomen kielen yleisyystilastoja. Kielikello 1/1991. (In Finnish)

Schneier, B. 2015. Applied Cryptography: Protocols, Algorithms and Source Code in C, 20th Anniversary Edition. New York: Wiley.


