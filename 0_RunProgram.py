import os

os.system("clear screen")
print("\nCA Operation center version: 1.0.0 | Developed by DevOps, BDPEER LTD. ")
print("====================================================================================")
print("\n")
options = ['1. Create new Subordinate CA', '2. Create new CA', '3. Create new CSR for existing CA', '4. Issue Certificate', '5. Revoke certificate', '6. Issue new CRL', '7. Configure CA for new deployment']

for option in options:
	print(option)

print("\n=======================================================")

popMsg = input("\nSelect an option from above (0/1/2...): ")

if popMsg == '1':
	os.system("python3 1010110.py")
elif popMsg == '2':
	os.system("python3 1010108.py")
elif popMsg == '3':
	os.system("python3 1010112.py")
elif popMsg == '4':
	os.system("python3 1010116.py")
elif popMsg == '5':
	os.system("python3 1010118.py")
elif popMsg == '6':
	os.system("python3 1010114.py")
elif popMsg == '7':
	os.system("python3 1010104.py")
else:
	print("\nPlease select a valid option.")



