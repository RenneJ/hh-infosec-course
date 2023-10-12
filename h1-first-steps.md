# [H1 First Steps](https://terokarvinen.com/2023/information-security-2023-autumn/#h1-first-steps) (Karvinen 2023)
## Summary
## Darknet Diaries Ep. 113: Adam (Rhysider, J. 2022)
- story of Adam - a young man who turned to crime
- despite his earlier crime record Adam got a job in IT support for a school in the UK, referred to as the Academy
- during his first week on the job Adam noticed serious problems regarding the organizations password policies
- Adam noticed that local admin passwords followed a simple pattern
- same pattern was true for the global domain admin
- as a new employee Adam was unsure how to proceed
- Adam's previous criminal record was only discussed with his supervisor and after a few months said record was used as grounds for termination
- Adam is not happy, gets a new job in IT learns a lot of new skills
- years go by
- Adam gets stressed and frustrated at his job, spends late nights playing video games and reading hacker forums
- out of curiosity Adam proceeds to check if they have changed the passwords from before when he worked for the Academy
- no, they hadn't, he easily gains access
- Adam spirals deeper and deeper into the Academy's systems, brute forces through VPN (guesses the password)
- he realises that he hasn't covered his tracks at all and knows that he will be easily identified through his IP address
- these are examples of lateral movement, after getting into a system he hops onto a different computer gaining more privileged access each hop
- Adam ends up getting access to domain and server controllers, just from knowing the domain name and slightly altering his old password
- in a fear of getting caught or as an act of vengeance against his former employer or both Adam wipes everything clear, what he wipes cannot be even booted again
- gets caught

Moral of the story is: don't anger a haXXor lol jk take care of your passwords. Change them regularly, don't form patterns and change passwords again when someone with admin level leaves or is let go from the organization! I think that Adam's story reminds aspiring white hats to be careful and mindful of themselves when hacking, you don't want to cause harm even accidentally.
# Summary
## Intrusion Kill Chain and Courses of Action (Hutchins et al 2011, chapters 3.1 and 3.2)
- key aspect of Intrusion Kill Chain is understanding the adversaries' actions
- it is important to understand the steps (or links) of the Kill Chain in order to take the correct countermeasure
- I think that:
  1. the defenders always need to be able to detect the intruder
  2. do your best to deny access or
  3. at least make the intruders efforts costly and/or tedious
# Debian running on VirtualBox
![Screenshot from 2023-08-25 18-26-26](https://github.com/RenneJ/hh-infosec-course/assets/97522117/77e276df-c36f-4202-9fb7-bd04b508ca8a)

## Sources

Hutchins et al, 2011. Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains. Lockheed Martin.
Karvinen, T. 2023. Information Security 2023 Autumn. https://terokarvinen.com/2023/information-security-2023-autumn/#h1-first-steps Accessed: 2023/10/12
Rhysider, J., 2022. EP 113: Adam. Darknet Diaries. https://darknetdiaries.com/episode/113/ Accessed: 2023/10/12
