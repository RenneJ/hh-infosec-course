# Summaries

## [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) (Braiterman et al., 2020)

Threat modeling = the process of identifying dangers to a system's security or privacy

Key questions to ask when threat modeling:

1. What are we working on?
2. What can go wrong?
3. What are we going to do about it?
4. Did we do a good enough job?

I think the above questions form the essence of threat modeling and should be repeated throughout any project one participates in.

Threat modeling enables you to perceive the risks in the system and helps you identify them so that proper decisions can be made.

### Do:

- systematic approach
- allow creativity along scientific approach
- varied viewpoints (diverse subject matter experts)
- use proper tools
- implement theory into practice

### Don't:

- think threat modeling is for the few, it is for all
- admire the problem, you need to find practical solutions
- overfocus
- try to create a perfect representation, there is no single ideal view, aim to create many representations to light different problems

## [World's Shortest Threat Modeling Course](https://www.youtube.com/playlist?list=PLCVhBqLDKoOOZqKt74QI4pbDUnXSQo0nf) (Shostack, 2022)

1. Do threat modeling early when it is inexpensive to deal with the problems that might rise.
2. Threat modeling is asking yourself (or your team) the four key questions: **What are we working on? What can go wrong? What are we going to do about it? Did we do a good enough job?**
3. Collaboration is important! Use white boards or equivalent drawing tools to figure out **what are we working on?**
4. Sketching is important to express individual thoughts to others.
5. Keep a record of what you're doing. It is beneficial to format it to be professionally presented.
6. Diagrams should be uniform so that everybody understands them.
7. Remember question 2: **what can go wrong?** Pay attention to answers.
8. STRIDE Mnemonic: **Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privileges**. Think about these types of attacks when threat modeling.
9. Track your work!
10. Threat modeling is used to manage risks by informing about possible threats.
11. Would you recommend a colleague to threat model? If yes: good job! Else: keep working on it!

## [Threat Modeling: Designing for Security. Chapter 1: Dive In and Threat Model!](https://www.oreilly.com/library/view/threat-modeling-designing/9781118810057/9781118810057c01.xhtml#c1) (Shostack 2014)

- Everyone should threat model.
- Modeling helps you distinguish the big picture.
- It helps you find issues in things you haven't built yet.
- It allows you to anticipate future threats.
- Effective threat modeling takes time and requires practice.

## [Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) (CheatSheets Series Team, 2021)

When creating threat models:
- document data flows
- document all the threats to the system
- document security controls, things that mitigate threats' likelihood and impact

### Terminology

**Threat agent** - baddie/baddies, an actor who is capable of carrying out an attack.

**Impact** - how much damage is done by an actualised threat.

**Likelihood** - chance of a threats actualisation.

**Controls** - actions the defenders take to avoid, detect, counteract, or minimize potential threats.

**Preventions** - controls the defenders use to completely nullify a threat.
    
**Mitigations** - controls the defenders use to reduce the likelihood and/or impact of a threat.

**Data Flow Diagram** - depiction of your system. It shows all the places where data is stored.

**Trust Boundary** - part of Data Flow Diagram where data changes its level of trust.

### Decompose and Model the System

Define Business Objectives. You need to know relevant regulations regarding your systems.

Identify application design. This is where drawing Data Flow Diagrams comes in handy. You need to understand how data flows within the system so that you can pinpoint the locations where threats might take place. Read pre-existing documentation. If there is none this is the opportunity to create design documentation. There are many ways to create design documents. The 4+1 model takes into account multiple views: 

- Logical view for designers. Consists of functional requirements.
- Implementation view for programmers. Consists of software components.
- Process view for integrators. Consists of non-functional requirements (concurrency and synchronization).
- Deployment view for deployment managers. Consists of topology (mapping of software to hardware)
- Use-Case view for all stakeholders including end users.

Define and evaluate assets (in the context of information systems it is probably data). Evaluate them using the CIA model (confidentiality, integrity, availability). Data in rest (i.e. not being transmitted) is often considered to be less vulnerable and more sought after by threat agents than data in transit. Differences in the state of data creates variance in methods used protecting it.

Use proper tools to draw data flow diagrams. Make your diagram in the context of MVC software architecture (model, view, controller).

Define:

- data flows
- trust boundaries
- trust levels
- roles (user's role, admin role etc.)
- app entry points (interfaces which threat agent can use)

### Identify threat agents and ALL possible threats.

Map threat agents to entry points.

Draw attack vectors and attack trees (I consider attack vectors to be similar to known exploits. But are specific to your system. Refer to OWASP10 for detailed descriptions).

Map abuse cases to use cases.

Re-define attack vectors.

### Write your Threat traceability matrix

Define impact and probability for each threat, enumerate risks.

Rank them based on their probability and impact.

### Determine countermeasures and mitigation

Identify the risk owners and come up with the solution to mitigate or eliminate the risk (or do nothing).

# Security Hygiene

Ask yourself: what sort of information about myself am I willing to share with strangers or risk losing? Then take appropriate steps to secure whatever it is that you value highly.

For example I don't take special safety precautions to secure my vacation photographs from 2015 but I do take backups of my school assignments.

Below are listed best practices regarding security hygiene. I have put my evaluations in parentheses.

### Best practices for users: [(Irei, 2022)](https://www.techtarget.com/searchsecurity/definition/cyber-hygiene)

- Backups (individual discretion based on the information is advised for everyone)
- Education (for everyone)
- Encryption (not for everyone)
- Firewalls (for everyone, but understanding them needs education)
- Password hygiene (for everyone)
- Patch management (for everyone)
- Online discretion (for everyone)
- Security software (not for everyone)

What do you think? Do you agree with my list? Or do you think there's something wrong or missing?

# Make-believe boogeyman - a threat model for a company

## The Taxi Company

The Taxi Company (referred to as TC) is a traditional provider of taxi services that employs roughly 30 persons. It forwards customers' requests to independent contractors - taxi drivers. TC operates in Finland. Customers can order a taxi via TC app or by calling the centre. The app can also be used to pay the fare.


Even though the independent contractors (drivers) are the source of revenue in this business model I don't refer to them as customers. The word customer is being used to refer to the person using the service to order a taxi.

Business plan in nutshell:
- Customer orders a taxi to their location.
- Ride takes place.
- Payment either via app or cash/card directly to driver.
- A portion of the payment goes to TC.

## What are we working on?

### Assets

TC's assets that need to be secured are:
- The company premises: the call centre and office
- Database, in cloud: IaaS, infrastructure as a service
    - Customer data (names, phone numbers, addresses, credit/debit card numbers etc.)
    - Employee data
    - Contractor/driver data
    - Business data (sales and marketing data, investment plans etc.)
 

### ![image](https://github.com/RenneJ/hh-infosec-course/assets/97522117/02191733-043f-46de-8043-a62dc00db772)

> Figure 1. Basic taxi order DFD

In figure 1 I illustrate the basic situation of ordering a taxi through the app. Worth noting here are the two trust boundaries. The inner trust boundary represents the IaaS infrastructure for the database. In TC the database infrastructure is acquired through a cloud service. That means that the hardware side of data storage is handled by an external actor. The management of data transfer and upkeep is done by TC IT department.

### ![image](https://github.com/RenneJ/hh-infosec-course/assets/97522117/9b09e9d8-3397-45c6-b9fa-f2e433eef7c1)

> Figure 2. Current office network diagram.

### Prioritisation of assets

1. Customer data
    - EU wide GDPR sets high standards for handling customer data, risk of facing legal consequences (fines or other regulatory actions)
    - Damages to customer data can have catastrophic effects to business continuity (not only reputation but also increased costs in maintaining a functioning database)
2. Contractor/driver data
    - Similar risks as in customer data. If contractor data is jeopardized the impact to reputation will affect the contractor's willingness to continue partnership.
    - If data regarding the contractor's fees leak then it could be exploited by a competitor.
3. 
