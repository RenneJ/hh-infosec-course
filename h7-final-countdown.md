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

I will be using SSH on the next assignment so let's leave it enabled.

# OpenSSH

OpenSSH is a tool used in Linux systems to establish SSH communications. On Windows machines you can use PuTTY.

Let's start again with:

       $ sudo apt-get update

Installing OpenSSH:

       $ sudo apt-get install ssh

I will skip this part as I have already done installing OpenSSH. To check your version of OpenSSH (V is uppercase):

       $ ssh -V

To check if OpenSSH is already running you can use:

       $ systemctl | grep ssh

If the above command yields no output OpenSSH is not running.

The command systemctl alone will give you an output of all running system processes. The grep ssh command will filter the output so that it will only show processes that have the string ssh in it.

### ![image](https://github.com/RenneJ/hh-infosec-course/assets/97522117/0670111f-ee0d-44c9-a6f4-4f7afaa44424)
> Image 3. Checking if ssh is already running.

To start OpenSSH:

       $ sudo systemctl start ssh

To stop OpenSSH:

       $ sudo systemctl stop ssh
       $ sudo systemctl disable ssh

Then to generate key pairs:

       $ ssh-keygen

This command generates two keys. A public key and a private key. After this we run:

       $ ssh-copy-id renne@localhost

This installs the key as an authorized key.

Now I can establish an ssh connection between two users so let's make a new user.

       $ adduser test01

Use a strong password when prompted. The other fields can be left empty (name, email etc.).

### ![image](https://github.com/RenneJ/hh-infosec-course/assets/97522117/41f908b8-d156-46fc-b611-cc618450727c)
> Figure 4. Ssh connection established.

# Sources

SSH, 2023. SSH Academy. https://www.ssh.com/academy. Accessed: 2023/10/04

Ubuntu Documentation, 2013. Firewall. https://help.ubuntu.com/community/Firewall. Accessed: 2023/10/04
