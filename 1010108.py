import os

os.system("clear screen")
print("\nNew CA creation wizard ")
print("=====================================")
os.system("pwd")
print("\nThis widzard will help you create Root CA. At the end of this program your root CA will be configured and live")

#Changing execution directory
CADirName = input("\nName of directory /root/<Directory Name>: ")
os.system("mkdir /root/" + CADirName)
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

#create CA key file
os.system("openssl genrsa -aes256 -out private/ca.key.pem 4096")
os.system("chmod 400 private/ca.key.pem")

#Generate CA Certificate
os.system("openssl req -config openssl.cnf -key private/ca.key.pem -new -x509 -days 7300 -sha256 -extensions v3_ca -out certs/ca.cert.pem")

print("\n=========================================================")
print("Root Certificate Authority is created successfully")
