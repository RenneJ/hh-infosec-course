# Link to assignment submissions

https://github.com/RenneJ/hh-infosec-course

# Cross-evaluations

Cross-evaluations are submitted to Haaga-Helia Moodle.

# Firewall

Before installing or upgrading packages in Linux environment it is important to update the sources so that you get the right packages.

The following paragraph is from apt-get documentation (man apt-get).

       update
           update is used to resynchronize the package index files from their
           sources. The indexes of available packages are fetched from the
           location(s) specified in /etc/apt/sources.list. For example, when
           using a Debian archive, this command retrieves and scans the
           Packages.gz files, so that information about new and updated
           packages is available. An update should always be performed before
           an upgrade or dist-upgrade. Please be aware that the overall
           progress meter will be incorrect as the size of the package files
           cannot be known in advance.

So the first step is:

       $ sudo apt-get update

Then we can install the wanted package with apt-get. Ufw stands for Uncomplicated Firewall. Actually, ufw is the front end of a database called iptables which can be used to configure the rules of network traffic in Linux systems. Ufw makes setting the firewall rules easier. (Ubuntu Documentation, 2013)

       $ sudo apt-get install ufw

I skipped this step as I already had installed ufw before. But I reset the configurations to install defaults with the following command:

       $ sudo ufw reset

### ![image](https://github.com/RenneJ/hh-infosec-course/assets/97522117/4c860a9e-6a52-48ad-84dd-e20a81f609f6)
> Image 1. View of ufw status in terminal after resetting.

After installing (or resetting in my case) we can start making rules to the firewall.

       $ sudo ufw allow 22/tcp

This command makes a new rule which allows traffic through the port number 22 using TCP (Transmission Control Protocol). Port 22 is a reserved port which is only used for SSH (Secure Shell) and protocols derived from it such as SCP and SFTP (SSH Copy and SSH File Transfer Protocol).

Finally let's turn on the changes:

       $ sudo ufw enable

### ![image](https://github.com/RenneJ/hh-infosec-course/assets/97522117/950d87d3-55e5-4c8b-8eb9-b9265d48d9ec)
> Image 2. View of ufw status in terminal after enabling a new rule.

# Sources

Ubuntu Documentation, 2013. Firewall. https://help.ubuntu.com/community/Firewall. Accessed: 2023/10/04
