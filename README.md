Push the iDRAC configuration using racadm by creating a temporal file. This script is also used to change the root password and create a customer account. Script requires racadm.
http://en.community.dell.com/techcenter/systems-management/w/wiki/3205.racadm-command-line-interface-for-drac
Usage:
```
usage: configure-idrac.py [-h] [-r RPASSWORD] [-n NPASSWORD] [-p CPASSWORD] -i
                          IP [-u USERNAME] [-c]

iDRAC configuration script. It configures the dracs and change the root
password

optional arguments:
  -h, --help            show this help message and exit
  -r RPASSWORD, --rpassword RPASSWORD
                        Root password, anypassword by default
  -n NPASSWORD, --npassword NPASSWORD
                      New root password, anypassword by default
  -p CPASSWORD, --cpassword CPASSWORD
                        Customer account password
  -i IP, --ip IP        Idrac IP or hostname
  -u USERNAME, --username USERNAME
                        Customer account to be created
  -c, --change          If set it will only modify the password of root user
```

