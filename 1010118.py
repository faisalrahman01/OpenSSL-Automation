import os

os.system("clear screen")
print("\nCA Certificate Revoke wizard ")
print("=====================================")

print("\nPlease make sure you are running this script from CA directory.")
curLoc = input("\nAre you in CA directory (Y/N)? ")

if curLoc == 'Y':
    CertName = input("Certificate file name to revoke (.pem): ")
    os.system("openssl ca -config openssl.cnf -revoke certs/" + CertName)
    print ("Certificate is revoked.")
    
elif curLoc == 'N':
    changeDir = input("Please insert CA installation directory: ")
    os.chdir(changeDir)
    print("Your current directory is: ")
    os.system("pwd")

    CertName = input("Certificate file name to revoke (.pem): ")
    os.system("openssl ca -config openssl.cnf -revoke certs/" + CertName)
    print("Certificate is revoked.")
    

    
