import os

os.system("clear screen")
print("\nCreate CA configuration set ")
print("=====================================")
os.system("pwd")

print("\nThis widzard will help creating CA configuration file.")
confFile = input("\nInsert default configuration file name: ")
caName = input("Insert CA name: ")
caDir = input("Insert CA directory name: ")


os.system("sed -i.bak s/default_ca = CSLD_CA/" + caName + "/g " + confFile)
os.system("sed -i.bak s/dir               = /root/CSLCA-script/" + caDir + "/g " + confFile)

print("Configuration file is re-configured")

