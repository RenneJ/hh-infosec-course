# H2: Spiderwebs
## OWASP 10 2021
### Summary: A05 Security Misconfiguration
Security misconfiguration is a category of 20 mapped CWEs (Common Weakness Enumerations). To my understanding it means that there are 20 different types of exploits or vulnerabilities.
Misconfiguration is a *root cause* type as opposed to *symptom* types such as Denial of Service.

System admins or programmers have left improper permissions for users to access files/directories or error messages contain sensitive information that can be exploited.
Examples:
  - Password in Configuration file (CWE-260)
    - Prevention: Either prevent access to configuration files or encrypt passwords and usernames.
    - This CWE represents a flaw in system architecture or design.
  - Missing Custom Error Page (CWE-756)
    - Prevention: The software needs to be programmed in such a way that the user doesn't get the full stack trace. Configuration files need to enable the custom error page.
    - This CWE represents a flaw in the source code.
   
General preventative measures against Security Misconfiguration weaknesses:
- 
### Summary: A06 Vulnerable and Outdated Components

### Summary: A03 Injection

## WebGoat
### Installation
Following Tero's guide I was able to install Java tools. This was done on Monday 28th. I replaced the older jdk version 
11 with the newer 17 on the installation command. So the command i used was:
- $ sudo apt-get -y install openjdk-17-jre ufw wget bash-completion
- (the guide on terokarvinen.com has since been updated to include the newer version)
### ![Screenshot from 2023-09-01 12-19-17](https://github.com/RenneJ/hh-infosec-course/assets/97522117/cc94ae00-cfc4-4c47-887e-17ac58baf9d4)
Enabling firewall on debian as instructed:
- $ sudo ufw enable

You can check the status of your firewall on debian using the command below:
### ![Screenshot from 2023-09-01 12-29-59](https://github.com/RenneJ/hh-infosec-course/assets/97522117/276b29b7-8013-4917-8027-9ff5c53b87e0)
Continuing Tero's instructions I downloaded and installed WebGoat:
- $ wget https://terokarvinen.com/2020/install-webgoat-web-pentest-practice-target/webgoat-server-8.0.0.M26.jar
### ![Screenshot from 2023-09-01 14-36-27](https://github.com/RenneJ/hh-infosec-course/assets/97522117/abb69fc1-6404-4f6e-9007-c4f497bb51f5)

- $ java -jar webgoat-server-8.0.0.M26.jar

Below the default view of WebGoat after siging in.
### ![Screenshot from 2023-09-01 14-42-28](https://github.com/RenneJ/hh-infosec-course/assets/97522117/66b2b9c7-af98-46bb-b86e-b85530003358)

### DevTools
Athough the instructions were for Google Chrome I completed the WebGoat developer tools challenge with Mozilla Firefox dev tools.
The only problem I faced was finding ***Sources*** tab from Firefox dev tools. But on Firefox the ***Debugger*** and ***Style Editor*** tabs present the same kind of information.

The challenge in this part was to find a randomised number from a specific HTTP request initiated by a click of a button on the html page.
#### Method A: Network tools
I'm guessing this is the intended way to pass the challenge. When you're on the **Try it!** page:
1. Open dev tools (F12 or CTRL +Shift+I or Application Menu -> More Tools -> Web Developer Tools.
2. Open ***Network*** tab. If it's not listed on the top of the tools view click >>.
3. Click **GO** on the html page.
4. Sort All results by File name.
5. Click the result under the name of **network**.
6. A new view under or next to results will pop up (depending on your dev tools display orientation).
7. Copy the value after **networkNum** to the check field on html page.
### ![Screenshot from 2023-09-01 20-03-17](https://github.com/RenneJ/hh-infosec-course/assets/97522117/912f4897-df38-4de1-b61c-ddf9afb06e98)

#### Method B: Inspect the element
This is the method I actually got the right answer in the first place. But I was dissatisfied as I thought this method was not the intended way to come to the right result.
1. On the **Try it!** page open **Inspector** tab of dev tools.
2. Next to the **Inspector** tab there's a button that opens an element picker. Element picker highlights on hover the html element and dev tools will navigate the html document to the corresponding line.
3. Click the field where you would paste the answer to (or anywhere inside the correct element e.g. the submit button).
4. With a quick glance you'll find the tag <input id=networkNumCopy ... value=*RANDOMISED NUMBER*>. You can also spam click **GO** and you should see a value highlighted and changing each click.
5. Copy the number from the dev tools view into the check field.
### ![Screenshot from 2023-09-01 18-42-09](https://github.com/RenneJ/hh-infosec-course/assets/97522117/b49e5190-8504-4aee-9e6b-6663c91b732e)

#### Thoughts/notes on the assignment and challenge
I struggled in the beginning of the challlenge quite much as the Firefox tools differ slightly from Chrome's. After rigorous and frustrating googling I started to tediously go through the Network requests. I must have refreshed the page and not clicked the **GO** button, paused the logging of network requests or I had incorrect filters on because I'm sure I would have checked the log file named **network**.

I stumbled upon the Method B as I was trying to find out the name (or any kind of information) about the request being sent. I got to the "right" method after clearing the network log cache and trying the **GO** button again. It was much simpler to spot the right file when there aren't >100 log entries to sieve through.
