# Summaries

## 7 Things You Should Know About Tor (Quintin 2014)

- Tor can't provide full anonymity if someone is monitoring your traffic and the service's traffic you're trying to communicate with
  - The cryptographic encryptions have probably not been broken
- Not just for criminals
  - Criminals also have a lot of tools to work in the internet (clearnet)
  - Tor can help you protect yourself against criminal tactics such as identity theft
- Truly open source
  - No military backdoors
- It is legal to run a tor relay (node)
  - At least in the USA at the time of the article's publication
- Easy to use
- Slower than clearnet
  - More nodes would make it faster
- It is not foolproof
  - You can identify yourself through tor if you are not careful

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

- The weakest link in tor browser is the user
  - The person using tor browser might turn on geolocation, scripts or other plugins that might compromise their true IP address

# Sources

Shavers, B. & Bair, J. 2016. Hiding behind the keyboard: Uncovering covert communication methods with forensic analysis. Syngress. Ch. 2.

Quintin, C. 2014. 7 Things You Should Know About Tor. Electronic Frontier Foundation. https://www.eff.org/deeplinks/2014/07/7-things-you-should-know-about-tor. Accessed: 2023/09/27
