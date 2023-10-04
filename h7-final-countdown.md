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

> sudo apt-get update
