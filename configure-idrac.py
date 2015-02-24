#!/usr/bin/env python
"""
Push the iDRAC configuration using racadm by creating a temporal file. This script is also used to change the root password and create a customer account. 

Script requires racadm 

"""
import argparse
import logging
from subprocess import call
import tempfile

#logging configuration
logging.basicConfig(format='%(asctime)s  %(message)s', level=logging.INFO)

class Main(object):
    def __init__(self):
        opt=argparse.ArgumentParser(description="iDRAC configuration scripti. It configures the dracs and change the     root password")
        opt.add_argument('-r', '--rpassword', help = "Root password, calvin by default",default='calvin')
        opt.add_argument('-n', '--npassword', help = "New root password, anypassword by default",default='anypassword')
        opt.add_argument('-p', '--cpassword', help = "Customer account password")
        opt.add_argument('-i', '--ip', help = "Idrac IP or hostname",required=True)
        opt.add_argument('-u', '--username', help = "Customer account to be created") 
        opt.add_argument('-c', '--change',action='store_true', help = "If set it will only modify the password of root user",default=False)
        args = opt.parse_args()
        #logging configuration
        logging.info("----Starting----")
        if args.change:
            # it changes only the root p:assword
            self.change_root_password(args.ip,args.rpassword,args.npassword)
        else:
            if not args.username:
                raise ValueError("You need to provide a username for the customer account -u ")    
            file = self.create_file_config(args.npassword,args.username, args.cpassword)
            self.configure_drac(file,args.ip,args.rpassword)

    def configure_drac(self,file,ip,rpassword):
        #Convert file string  into a temp file
        temp = tempfile.NamedTemporaryFile()
        temp.write(file)
        logging.info("----Connecting to %s racadm----"%ip)
        if call(["racadm","-r","%s"%ip, "-u","root","-p","%s"%rpassword,"config","-f","%s"%temp.name]) !=0:
            raise IOError ("racadm failed to configure the iDrac")
        temp.close()
        logging.info("----iDrac successfully configured-----")
    def change_root_password(self,ip,rpassword,npassword):
        logging.info("---- Changing iDRAC root password in  %s ----"%ip)
        if call("racadm","-r",  "%s"%ip,"-u","root","-p","%s"%rpassword,"config","-g","cfgUserAdmin","-o","cfgUserAdminPassword","-i","2","%s"%npassword)!=0:
            raise IOError ("Failed to change the password")

    def create_file_config(self,npassword,username,cpassword):
         idrac= """

         [idRacInfo]
        # idRacType=16
        # idRacProductInfo=Integrated Dell Remote Access Controller
        # idRacDescriptionInfo=This system component provides a complete set of remote management functions for Dell PowerEdge Servers
        # idRacVersionInfo=1.57.57
        # idRacBuildInfo=04
        # idRacName=idrac-CZ56032

            [cfgUserAdmin]
            # cfgUserAdminIndex=2
            cfgUserAdminUserName=root
            cfgUserAdminPassword=%s
            cfgUserAdminEnable=1
            cfgUserAdminPrivilege=0x000001ff
            cfgUserAdminIpmiLanPrivilege=4
            cfgUserAdminIpmiSerialPrivilege=4
            cfgUserAdminSolEnable=1

            [cfgUserAdmin]
             cfgUserAdminIndex=3
             cfgUserAdminUserName=%s
             cfgUserAdminPassword=%s
             cfgUserAdminEnable=1
             cfgUserAdminPrivilege=0x000001f3
             cfgUserAdminIpmiLanPrivilege=15
             cfgUserAdminIpmiSerialPrivilege=15
             cfgUserAdminSolEnable=1

             [cfgSessionManagement]
             cfgSsnMgtWebserverTimeout=1920
             [cfgRacTuning]
             cfgRacTunePlugintype=1

             [cfgIpmiLan]
             cfgIpmiLanEnable=1

            # cfgUserDomainIndex=12
            #cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=13
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=14
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=15
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=16
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=17
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=18
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=19
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=20
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=21
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=22
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=23
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=24
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=25
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=26
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=27
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=28
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=29
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=30
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=31
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=32
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=33
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=34
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=35
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=36
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=37
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=38
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=39
            cfgUserDomainName=

            [cfgUserDomain]
            # cfgUserDomainIndex=40
            cfgUserDomainName=



            [cfgSmartCard]
            cfgSmartCardLogonEnable=0
            cfgSmartCardCRLEnable=0



            [cfgServerInfo]
            cfgServerBootOnce=1
            cfgServerFirstBootDevice=No-Override



            [cfgSensorRedundancy]
            # cfgSensorRedundancyIndex=1
            cfgSensorRedundancyPolicy=Not Redundant
            # cfgSensorRedundancyCapabilities=Not Redundant
            # cfgSensorRedundancyStatus=4



            [cfgLanNetworking]
            cfgNicEnable=1
            cfgNicIPv4Enable=1
            cfgNicIpAddress=10.87.40.138
            cfgNicNetmask=255.255.252.0
            cfgNicGateway=10.87.40.1
            cfgNicUseDhcp=1
            # cfgNicMacAddress=B0:83:FE:C3:39:92
            cfgNicVLanEnable=0
            cfgNicVLanID=1
            cfgNicVLanPriority=0
            cfgNicSelection=1
            cfgDNSServersFromDHCP=Enabled
            cfgDNSServer1=10.87.0.1
            cfgDNSServer2=0.0.0.0
            cfgDNSRacName=idrac-CZ56032
            cfgDNSDomainName=
            cfgDNSDomainNameFromDHCP=Disabled
            cfgDNSRegisterRac=0
            cfgNicFailoverNetwork=None



            [cfgStaticLanNetworking]
            cfgNicStaticEnable=1
            cfgNicStaticIPv4Enable=1
            cfgNicStaticUseDhcp=1
            cfgNicStaticIpAddress=192.168.0.120
            cfgNicStaticNetmask=255.255.255.0
            cfgNicStaticGateway=192.168.0.1
            cfgDNSStaticServersFromDHCP=Enabled
            cfgDNSStaticServer1=0.0.0.0
            cfgDNSStaticServer2=0.0.0.0
            cfgDNSStaticDomainNameFromDHCP=Disabled
            cfgDNSStaticDomainName=



            [cfgNetTuning]
            #cfgNetTuningNic100MB=2
            cfgNetTuningNicFullDuplex=1
            cfgNetTuningNicMtu=1500
            cfgNetTuningNicAutoneg=1



            [cfgIPv6LanNetworking]
            cfgIPv6Enable=0
            cfgIPv6Address1=::
                cfgIPv6Gateway=::
                cfgIPv6PrefixLength=64
                cfgIPv6AutoConfig=1
                # cfgIPv6LinkLocalAddress=::
                # cfgIPv6Address2=::
                # cfgIPv6Address3=::
                # cfgIPv6Address4=::
                # cfgIPv6Address5=::
                # cfgIPv6Address6=::
                # cfgIPv6Address7=::
                # cfgIPv6Address8=::
                # cfgIPv6Address9=::
                # cfgIPv6Address10=::
                # cfgIPv6Address11=::
                # cfgIPv6Address12=::
                # cfgIPv6Address13=::
                # cfgIPv6Address14=::
                # cfgIPv6Address15=::
                cfgIPv6DNSServersFromDHCP6=Disabled
                cfgIPv6DNSServer1=::
                cfgIPv6DNSServer2=::



            [cfgIPv6StaticLanNetworking]
             cfgIPv6StaticEnable=0
            cfgIPv6StaticAutoConfig=1
             cfgIPv6StaticAddress1=::
            cfgIPv6StaticGateway=::
            cfgIPv6StaticPrefixLength=64
            cfgIPv6StaticDNSServersFromDHCP6=Disabled
            cfgIPv6StaticDNSServer1=::
            cfgIPv6StaticDNSServer2=::


             [cfgIPv6URL]
            # cfgIPv6URLString=""" %(npassword,username,cpassword)
         return idrac

if __name__ == "__main__":
    main = Main()


