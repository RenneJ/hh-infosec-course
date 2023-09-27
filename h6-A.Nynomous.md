# Summaries

## 7 Things You Should Know About Tor (Quintin 2014)

- Tor can't provide full anonymity if someone is monitoring your traffic and the service's traffic you're trying to communicate with
  - The cryptographic encryptions have probably not been broken
- Not just for criminals
  - Criminals also have a lot of tools to work in the internet (clearnet)
  - Tor can help you protect yourself against criminal tactics such as identity theft
- Truly open source
  - No military backdoors
- It is legal to run a Tor relay (node)
  - At least in the USA at the time of the article's publication
- Easy to use
- Slower than clearnet
  - More nodes would make it faster
- It is not foolproof
  - You can identify yourself through Tor if you are not careful

## Hiding Behind the Keyboard. Chapter 2: The Tor Browser (Shavers & Bair 2016)

### Introduction

- Tor = The Onion Router
- Tor browser hides your IP address
- It is not the only technology to hide user's identity online but it is the simplest

### History and Intended Use of The Onion Router

- Allows the people to use the whole internet despite restrictions/censorship by oppressive governments
- Allows whistleblowers to communicate with officials
- Allows people and businesses to communicate in private manner
- Can be used to conduct criminal activities

### How The Onion Router Works

- Tor randomly selects a route through tor nodes between sender and recipient
- The data is encrypted with elliptic curve cryptography
- Each node stips a "layer" of encryption and the data is in its original from to the recipient
  - The last relay (exit node - recipient) is unencrypted
- None of the nodes "know" anything about the whole communication chain
  - A node knows only where the message came from and where to send it next

### Tracking Criminals Using Tor

- The weakest link in Tor browser is the user
  - The person using Tor browser might turn on geolocation, scripts or other plugins that might compromise their true IP address
 
## Installing I2P

I have already installed Tor browser on my Ubuntu laptop and Windows desktop. So instead of doing it the third time I will install I2P.

### ![h6_i2p_installsteps](https://github.com/RenneJ/hh-infosec-course/assets/97522117/e3bd2c11-875e-4b75-bfcc-6f7f286d0a49)
> Figure 1. Installing steps. Src: https://geti2p.net/en/download/windows

1. Installing Java
- First I checked if I already have JRE installed (Java Runtime Environment).
  - I just had JDK (Java Development Kit) so I downloaded JRE (https://www.java.com/en/download/manual.jsp)
- Then I ran the installation wizard and I was done

2. Installing I2P
- I navigated to I2P download page (figure 2)
- I chose the correct OS and used the stable release installer (not the beta version which doesn't require JRE)
- I didn't make changes to default settings during installation

### ![h6_i2p_geti2p](https://github.com/RenneJ/hh-infosec-course/assets/97522117/d3e2a6ef-ce39-4ba4-97f5-675442837e17)
> Figure 2. I2P download page. Src: https://geti2p.net/en/

### ![h6_i2p_postinstall](https://github.com/RenneJ/hh-infosec-course/assets/97522117/7d29df8f-5981-4cea-bfb6-e1af3eeac061)
> Figure 3. Excerpt of I2P postinstall instructions. Src: https://geti2p.net/en/download/2.3.0/clearnet/https/download.i2p2.no/i2pinstall_2.3.0_windows.exe/download

3. Installing better browser
- I already have Firefox and Tor browser so I skipped this step
- I do however need to install a Firefox user profile for I2P
  - The detailed instructions for Firefox configuration can be accessed at https://geti2p.net/en/download/2.3.0/clearnet/https/download.i2p2.no/I2P-Easy-Install-Bundle-2.3.0.exe/download#firefox


# Sources

Shavers, B. & Bair, J. 2016. Hiding behind the keyboard: Uncovering covert communication methods with forensic analysis. Syngress. Ch. 2.

Quintin, C. 2014. 7 Things You Should Know About Tor. Electronic Frontier Foundation. https://www.eff.org/deeplinks/2014/07/7-things-you-should-know-about-tor. Accessed: 2023/09/27
