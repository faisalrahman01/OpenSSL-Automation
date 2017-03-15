import os

print("\nPlease make sure you are running this script from CA directory.")
curLoc = input("\nAre you in CA directory (Y/N)? ")

if curLoc == 'Y':
    CAKeyFileName = input("Insert CA key file name with extension (.pem): ")
    CACertFileName = input("Insert CA certificate file name with extension (.pem): ")
    CACrlFileName = input("Insert CA CRL file name with extension (.pem): ")
    CRLFileName = input("Insert CA CRL file name with extension (.crl): ")

    os.system("openssl ca -config openssl.cnf -gencrl -keyfile private/" + CAKeyFileName + " -cert certs/" + CACertFileName + " -out crl/" + CACrlFileName)
    os.system("openssl crl -inform PEM -in crl/" + CACrlFileName + " -outform DER -out crl/" + CRLFileName)
    os.system("rm crl/" + CACrlFileName )

    print("\nNew CRL issued")

elif curLoc == 'N':

    changeDir = input("Please insert CA installation directory: ")
    os.chdir(changeDir)
    print("Your current directory is: ")
    os.system("pwd")
    
    CAKeyFileName = input("Insert CA key file name with extension (.pem): ")
    CACertFileName = input("Insert CA certificate file name with extension (.pem): ")
    CACrlFileName = input("Insert CA CRL file name with extension (.pem): ")
    CRLFileName = input("Insert CA CRL file name with extension (.crl): ")

    os.system("openssl ca -config openssl.cnf -gencrl -keyfile private/" + CAKeyFileName + " -cert certs/" + CACertFileName + " -out crl/" + CACrlFileName)
    os.system("openssl crl -inform PEM -in crl/" + CACrlFileName + " -outform DER -out crl/" + CRLFileName)
    os.system("rm crl/" + CACrlFileName )

    print("\nNew CRL issued")
else:
    print("Please try run the program again with valid Y/N options")

    
    
