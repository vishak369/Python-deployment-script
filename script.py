import os
import sys
import shutil
import os.path
import glob
import datetime
class b:
    W = '\033[95m'
    BLUE = '\033[94m'
    OK = '\033[92m'
    END = '\033[0m'
    FAIL = '\033[91m'
    white = '\033[1m'
    y = '\033[93m'
os.system("sudo /bin/su - tomcat8")
os.system("systemctl stop tomcat")
os.chdir("/root/folder1")
for file in glob.glob("*.war"):
    s=os.path.splitext(file)[0]
    os.chdir("/opt/tomcat/webapps")
    os.system("rm -rf " + s )
s = datetime.datetime.now().strftime('%d-%m-%Y:%H:%M:%S')
os.mkdir("/root/python/backup-" + s )
for file in os.listdir("/root/folder1/"):
    os.chdir("/opt/tomcat/webapps/")
    if os.path.exists(file):
        dn="/home/ec2-user/backup/" + s
        shutil.move(file, dn)
        print(b.BLUE+"Backup of " + file+" taken"+b.END)
    else:
        print("No " + file + " for taking  backup")

    os.chdir("/root/folder1")
    os.system("cp -rf " + file + " /opt/tomcat/webapps")
    os.chdir("/opt/tomcat/webapps")
    os.system("chown -R redhat.redhat " + file )
    print(b.OK+ file +" Deployed"+b.END)
    print("--------------------------------------------------------------------------------------------")
os.system("systemctl restart tomcat")
print(b.OK+"Deployment successfully Completed....")
c=input(b.W+"To view live logs press '1' or press '2' to end the process : "+b.END)
if c==1:
    os.system("tail -fn 100 /opt/tomcat/logs/catalina.out")
else:
    pass
