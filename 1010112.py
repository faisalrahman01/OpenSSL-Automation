import os

os.system("clear screen")
print("\nCA CSR generation wizard ")
print("=====================================")

print("\nPlease make sure you are running this script from CA directory.")
curLoc = input("\nAre you in CA directory (Y/N)? ")

if curLoc == 'Y':
    CAKeyFileName = input("Please enter CA key File name with extension: ")
    CSRFileName = input("Please enter CSR file name with extension: ")
    os.system ("openssl req -config openssl.cnf -new -sha256 -key private/" + CAKeyFileName + " -out csr/" + CSRFileName)
    print("Your New CSR named: " + CSRFileName + " is stored at directory csr/" )

elif curLoc == 'N':
    changeDir = input("Please insert CA installation directory: ")
    os.chdir(changeDir)
    print("Your current directory is: " +  str(os.system("pwd")))
    CA1KeyFileName = input("Please enter CA key File name with extension: ")
    CSR1FileName = input("Please enter CSR file name with extension: ")
    os.system ("openssl req -config openssl.cnf -new -sha256 -key private/" + CA1KeyFileName + " -out csr/" + CSR1FileName)
else:
    print("Please try run the program again with valid Y/N options")
    
    
    
    
    
    
    
