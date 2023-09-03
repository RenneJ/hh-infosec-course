# BROKEN ACCESS CONTROL
### What is access control?
Access control is a security technique used to limit or permit certain system users from accessing data (Lutkevich 
2022). I.e. admins have admin access and customers have customer access etc.

There are two types of access control:
- Physical: limiting access to the spaces where the end-points are, campuses, offices, classrooms etc.
  - Physical barriers: doors and locks, guards
- Logical: limiting access to networks and system files.
  - ID authentication and authorization: passwords, PIN, biometric scans (fingerprints). Multifactor authentication 
  takes into account multiple authentication methods.
  - In an organization admins should only allow access to specific directories or files to persons who really need it to perform their duties.
    - Eg. don't authorize a front desk employee to read/write/execute files regarding employee salaries.
   
Examples of broken acces control from portswigger:

- Unprotected functionality
  - User gains access to admin panel by guessing (or brute forcing) the URL e.g. <span>https</span>://insecure-website.com/admin
 - User role controlled by request parameter
   - Admin panel is login protected but changing cookie **Admin=false** to **Admin=true** works

### Sources:
- Lutkevich, B. 2022. access control. TechTarget. https://www.techtarget.com/searchsecurity/definition/access-control
- https://portswigger.net/web-security/access-control#what-is-access-control
