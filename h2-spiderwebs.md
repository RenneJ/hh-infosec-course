# [H2: Spiderwebs](https://terokarvinen.com/2023/information-security-2023-autumn/#h2-spiderwebs) (Karvinen 2023)

## OWASP 10 2021

### Summary: A05 Security Misconfiguration (https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)

Security misconfiguration is a category of 20 mapped CWEs (Common Weakness Enumerations). It means that there are 20 different types (or subcategories) of exploits or vulnerabilities.
Misconfiguration is a *root cause* type as opposed to *symptom* types such as Denial of Service.

System admins or programmers have left improper permissions for users to access files/directories or error messages contain sensitive information that can be exploited.

Examples:

- Password in Configuration file (CWE-260)
  - Prevention: Either prevent access to configuration files or encrypt passwords and usernames.
  - This CWE represents a flaw in system architecture or design.
- Missing Custom Error Page (CWE-756)
  - Prevention: The software needs to be programmed in such a way that the user doesn't get the full stack trace. Configuration files need to enable the custom error page.
  - This CWE represents a flaw in the source code.

General preventative measures and best practices against Security Misconfiguration vulnerabilities:

- Development, quality assurance (i.e. testing) and production environments need to be configured identically with different credentials. This can and should be automated.
- Don't ship anything unnecessary. Remove or don't install unused features and frameworks.
- During patch management review and update the configurations appropriate to all security notes, updates, and patches.
- Segmented architecture. It is safer to keep different parts separated.
- Sending security directives to clients.
- Verify the effectiveness of configurations.

### Summary: A06 Vulnerable and Outdated Components (https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)

Vulnerable and Outdated Components is a category of 3 mapped CWEs (2 of them being former TOP10 categories).  This category was placed #2 on the OWASP survey. There are no CVEs (Common Vulnerability and Exposure) mapped to A06 whereas the above summary of A05 has 789 CVEs.

Vulnerable and Outdated Components refer to any OS, web/app servers, APIs, libraries etc. that an information system (personal or organizational) uses. What this means is that it should be avoided to use components that are not maintained anymore or have a newer version available. Don't use components or their dependencies with unknown versions.

Recognizing vulnerabilities:

- Know your system. You need to know the components and their dependencies in your system.
- Scan regularly for vulnerabilities and subscribe to security bulletins regarding the components you use.
- Test for compabilities of updated components.

Prevention:

- Remove unused components.
- Meticulous monitoring of components' updates.
- Obtain components from official sources over secure links.

I find it interesting that the recognition and prevention are very similar. Why do you think that is so?

### Summary: A03 Injection (https://owasp.org/Top10/A03_2021-Injection/)

Injections are an attacker's attempts to manipulate commands sent in an application to interpreter. A system is vulnerable when:

- User submitted data isn't validated or filtered.
- There's no context-aware escaping.
  - ![Screenshot from 2023-09-02 16-20-17](https://github.com/RenneJ/hh-infosec-course/assets/97522117/93c2ea72-73e2-4122-a52d-e8b38fb32738)

  Image 1. Screenshot from a StackOverflow exchange. Answered by user: jmaloney.

- *Hostile data is used within object-relational mapping (ORM) search parameters to extract additional, sensitive records.* (I am unsure what this means)
- User input is used directly or is concatenated. Eg. user can input malicious SQL query into the application and it's interpreted as is.

Prevention:

- Use trusted APIs to avoid using interpreter altogether (remember safe usage regarding components).
- Use positive server-side input validation. Check that the user's input is correct on the server instead of on the client. (Is there negative input validation? Quick googling yielded no appropriate hits.) 
- Use SQL controls like LIMIT to prevent massive outputs data.

Example (CWE-1287: Improper Validation of Specified Type of Input):

- A child of CWE-20: Improper Input Validation
- When an app's certain functionality is built to handle a specific type of data it is important to validate the user input to be the right type
  - If not: the attacker might be able to cause unexpected errors or trigger unwanted events
- This type of attack is more prevalent against products with type-unsafe languages (eg. PHP) or in languages that support casting (eg. C)

Mitigation:

- Assume all input is malicious.
- Accept only predetermined "good" input, if user input doesn't adhere to the specifications don't accept it
- Take into consideration length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules.

## WebGoat

### Installation (Karvinen 2023)

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

1. Open dev tools (F12 or CTRL +Shift+I or Application Menu -> More Tools -> Web Developer Tools).
2. Open ***Network*** tab. If it's not listed on the top of the tools view click >>.
3. Click **GO** on the html page.
4. Sort All results by File name.
5. Click the result under the name of **network**.
6. A new view under or next to results will pop up (depending on your dev tools display orientation).
7. Copy the value after **networkNum** to the check field on html page.

### ![Screenshot from 2023-09-01 20-03-17](https://github.com/RenneJ/hh-infosec-course/assets/97522117/912f4897-df38-4de1-b61c-ddf9afb06e98)

#### Method B: Inspect the element

This is the method I actually got the right answer in the first place. But I was dissatisfied as I thought this method was not the intended way to get the right result.

1. On the **Try it!** page open **Inspector** tab of dev tools.
2. Next to the **Inspector** tab there's a button that opens an element picker. Element picker highlights on hover the html element and dev tools will navigate the html document to the corresponding line.
3. Click the field where you would paste the answer to (or anywhere inside the correct element e.g. the submit button).
4. With a quick glance you'll find the tag <input id=networkNumCopy ... value=*RANDOMISED NUMBER*>. You can also spam click **GO** and you should see a value highlighted and changing each click.
5. Copy the number from the dev tools view into the check field.

### ![Screenshot from 2023-09-01 18-42-09](https://github.com/RenneJ/hh-infosec-course/assets/97522117/b49e5190-8504-4aee-9e6b-6663c91b732e)

#### Thoughts/notes on the assignment and challenge

I struggled in the beginning of the challenge quite much as the Firefox tools differ slightly from Chrome's. After rigorous and frustrating googling I started to tediously go through the Network requests. I must have refreshed the page and not clicked the **GO** button, paused the logging of network requests or I had incorrect filters on because I'm sure I would have checked the log entry with file named **network**.

I stumbled upon the Method B as I was trying to find out the name (or any kind of information) about the request being sent. I got to the "right" method after clearing the network log cache and trying the **GO** button again. It was much simpler to spot the right file when there aren't >100 log entries to sieve through.

## Updating apps and OS on debian

$ sudo apt update
$ sudo apt upgrade 

## SQLZoo

SQL Zoo was down when I tried to do the assignment.

### ![Screenshot from 2023-09-03 13-11-25](https://github.com/RenneJ/hh-infosec-course/assets/97522117/49689f28-7aa2-4ea3-8cd1-6caf1c0cb11f)


## Portswigger

### SQL injection

I had to check the solution to the challenge due to time limitations (I forgot that the homework needs to be sent 24h before the class on Monday). I successfully got the solution after looking the hints on the challenge page.

### ![Screenshot from 2023-09-03 12-50-33](https://github.com/RenneJ/hh-infosec-course/assets/97522117/fb993267-799c-4292-82b2-31dea4a4d2b3)

Afterwards I tried to come to the same result via different method.

### ![image](https://github.com/RenneJ/hh-infosec-course/assets/97522117/dff0af94-d28d-4827-a0f2-938a4dc86203)

SUCCESS! What sort of solutions did you come up with?

## Sources

Karvinen, T. 2023. Information Security 2023 Autumn. https://terokarvinen.com/2023/information-security-2023-autumn/#h2-spiderwebs Accessed: 2023/10/12

StackOverflow. What are context aware variables?. https://stackoverflow.com/questions/28142771/what-are-context-aware-variables Accessed: 2023/10/12
