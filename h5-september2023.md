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

### What is phishing?

- Phishing is a practise of sending emails to a target/targets in an attempt to get sensitive data that can be exploited to attacker's benefit
  - The data the attacker seeks can be login credentials, personal information or other sensitive information
  - Phsishing emails can contain links to malicious sites or harmful attachments

### Why people click phishing links?

According to Benenson, Gassman and Landwirth (2016):

- 34% out of curiosity
- 27% message fit expectations
- 16% thought they knew the sender

### Protection mechanisms and how to bypass them

**Sender Policy Framework (SPF)** 🛡️

- Email validation system
  - Receiving mail server checks if the sender's IP is allowed to send emails
  - A lot of organisations have misconfigured SPF records
    - Attacker could present themself as a member of that organisation

**DomainKeys Identified Mail (DKIM)** 🛡️

- Email validation system
  - Sending mail server attaches a digital signature to email header
  - Recipient can validate that the email hasn't been altered during transit

**Domain Message Authentication, Reporting & Conformance (DMARC)** 🛡️

- Built on top of SPF and DKIM
- Policy and reporting protocol
 - Notifies if someone is trying to abuse your email (e.g. impersonating as a member of your organisation)

**Filtering** 🛡️

- Malware/spam filtering
- Protection against (poorly made) malicious attachments
- URL whitelisting / Web filtering
  - Only specific domains are allowed
    - There are bypasses to appear more legitimate

**Site Cloning** 🗡️

- Effective for spear-phishing (targeted phishing attacks)
  - Usually goal is to get user credentials
- Using only HTTPS is an effective protection against clone sites

**IDN Homograph Attack** 🗡️

- Use similar looking characters to bypass detection e.g. cyrillic A looks similar to latin A but has different encoding
 
### What usually works in phishing?

- Package delivery message
  - "You have a package at... tracking code xyz123"
- Mail from IT/Service desk
- LinkedIn, Gmail, Dropbox...
  - Well-known, reputable organisations
- Information related to current events within organisation

### What to do?

- Implement aforementioned protocols (marked with 🛡️)
- Keep your domains safe
  - Register similar domains to yourself
- Educate and train users
- Secure infrastructure
  - Properly configured and separated networks within the organisation

### My notes

I was surprised by the numbers presented in the video. The amount of people who clicked the links (in studies and controlled cases) was greater than I expected. Also, it is becoming apparent that faking a legitimate looking site doesn't take much technical skill.

# Cracking Hashes

## Install Hashcat

I did this exercise as a demonstration during class. For this assignment I'm replicating and documenting the process on a Win11 Desktop.

### Download and unpack

Download hashcat from the official website (https://hashcat.net/hashcat/).

Check that the fingerprints match. Download PGP Signature and check that it is the same as in the highlighted area (figure 1). I used Kleopatra to verify the signature (figure 2).

- Open Kleopatra
- Click Decrypt/Verify
- Choose the file (that ends in .asc)
- Open audit log to see ouput more clearly
- Do the fingerprints match?

### ![h5_hashcat_dl](https://github.com/RenneJ/hh-infosec-course/assets/97522117/ee7008a9-a24f-44b1-94ab-69ffb215e8dc)
> Figure 1. Hashcat download page.

### ![h5_hashcat_sig_verify](https://github.com/RenneJ/hh-infosec-course/assets/97522117/2730ec3b-e62a-4de7-b96f-ee412fba5d82)
> Figure 2. Kleopatra verification audit log.

After this you can unpack/extract the hashcat .7z file. Use 7-Zip File Manager. It's recommended to extract it to a location other than \Downloads. Downloads folder is often cleared so you don't want to have to install hashcat again.

### Using hashcat

Let's first download a wordlist. I downloaded the rockyou.txt raw file from GitHub (https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz) and unpacked it (figure 3).

### ![h5_hashcat_wordlist](https://github.com/RenneJ/hh-infosec-course/assets/97522117/e7a43c10-62f8-49d3-9241-33a8dd9de0b9)
> Figure 3. Unpacking rockyou.

Note that you need to unpack twice to get the .txt file that hashcat can utilise!

Open Command Prompt (on windows 11 I always type cmd to search and press Enter). Then navigate to the location you unpacked hashcat to. You know you're in the right folder when the prompt in cmd says hashcat-[version.number]. From this point forward I use Tero's instructions with slight modifications to commands (https://terokarvinen.com/2022/cracking-passwords-with-hashcat/).

### ![h5_hashcat_example_crack](https://github.com/RenneJ/hh-infosec-course/assets/97522117/487a6804-fd4e-45c7-b30c-e16980ae6c38)
> Figure 4. View from Command Prompt.

In fiure 4 I have started the hashcat password cracking. I faced a few problems. Firstly: I had to extract the rockyou wordlist another time and I also had to alter the command to match my directory specifications. Secondly: I got an error noting me about token length (figure 5) which was fixed by leaving the single quotes out.

### ![h5_hashcat_error_01](https://github.com/RenneJ/hh-infosec-course/assets/97522117/826a5d71-fe73-48b9-b5c2-b03af548c720)
> Figure 5. Hashcat token length exception.

# Sources

Benenson, Z., Gassmann, F., & Landwirth, R. 2016. Exploiting curiosity and context: How to make people click on a dangerous link despite their security awareness

Schneier, B. 2015. Applied Cryptography: Protocols, Algorithms and Source Code in C, 20th Anniversary Edition. New York: Wiley.

Särökaari, N. 2018. Disobey 2018 - Phishing through email - Niklas Särökaari. Disobey. Video. URL: https://www.youtube.com/watch?v=m9YFJGSHYtY. Accessed: 2023/09/22.

