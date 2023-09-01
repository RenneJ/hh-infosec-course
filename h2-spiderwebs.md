# H2: Spiderwebs
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
The only problem I faced was finding ***Sources***-tab from Firefox dev tools. But on Firefox the ***Debugger*** and ***Style Editor*** tabs present the same kind of information.
