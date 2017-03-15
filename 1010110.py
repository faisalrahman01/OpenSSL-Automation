import os

os.system("clear screen")
print("\nNew Subordinate CA creation wizard ")
print("=====================================")
os.system("pwd")

CADirName = input("Name of directory /root/<Directory Name>: ")
os.system("mkdir /root/" + CADirName)
#os.system("cp openssl.cnf /root/" + CADirName)
os.chdir("/root/" + CADirName)
os.system("pwd")

#Copy configuration file
ConfFileDir = input("OpenSSL Custom configuration file location (path details with filename & extension): ")
os.system("cp " + ConfFileDir + " /root/" +CADirName)

#Creating file structure
os.system("mkdir certs crl csr newcerts private")
os.system("chmod 700 private")
os.system("touch index.txt")
os.system("echo 1000 > serial")
os.system("echo 1000 > crlnumber")

#create intermediate keys
os.system("openssl genrsa -aes256 -out private/ca.key.pem")
os.system("chmod 400 private/ca.key.pem")

print ("\nNow please check CA directory: /root/" + CADirName)

#Generate CSR from Intermediate Key
os.system("openssl req -config openssl.cnf -new -sha256 -key private/ca.key.pem -out csr/ca.csr.pem")

print("\nYour CSR is generated as in csr/ca.csr.pem. ")
CSRchangeName = input("Do you want to change in different name? (Y/N)")

#Renaming default CSR file name
if CSRchangeName == 'Y':
	newName = input("\nRenamed CSR file name: ")
	os.system("cp csr/ca.csr.pem csr/" + newName)
	print("\nRenamed CSR file name is: /csr/" + newName)
elif CSRchangeName == 'N':
	print("Exiting application. Your CSR file name is: csr/ca.csr.pem")
else:
	print("Invalid perameter. Exiting application. no change made.")


