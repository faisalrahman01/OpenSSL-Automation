import os

os.system("clear screen")
print("\nCA Certificate generation wizard ")
print("=====================================")

print("\nPlease make sure you are running this script from CA directory.")
curLoc = input("\nAre you in CA directory (Y/N)? ")

if curLoc == 'Y':
    Cert_type = input("Certificate type(v3_ca, server_cert, user_cert): ")
    Validity = input("Validity period (days): ")
    CSR_FileName = input("CSR file name: ")
    Cert_FileName = input("Certificate file name: ")

    os.system("openssl ca -config openssl.cnf -extensions " + Cert_type +" -days "+ Validity + " -notext -md sha256 -in csr/" + CSR_FileName + " -out cert/" + Cert_FileName)
    os.system("openssl x509 -noout -text -in " + Cert_FileName)

elif curLoc == 'N':
    changeDir = input("Please insert CA installation directory: ")
    os.chdir(changeDir)
    print("Your current directory is: ")
    os.system("pwd")

    Cert_type = input("\nCertificate type(v3_intermediate_ca, server_cert, user_cert): ")
    Validity = input("Validity period (days): ")
    CSR_FileName = input("CSR file name: ")
    Cert_FileName = input("Certificate file name: ")

    os.system("openssl ca -config openssl.cnf -extensions " + Cert_type +" -days "+ Validity + " -notext -md sha256 -in csr/" + CSR_FileName + " -out certs/" + Cert_FileName)
    os.system("openssl x509 -noout -text -in certs/" + Cert_FileName)



