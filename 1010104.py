import os
import io
#import glob

os.system("touch fl1.cnf")
os.system("touch fl2.cnf")
os.system("touch fl3.cnf")
os.system("touch fl4.cnf")
os.system("touch fl5.cnf")
os.system("touch fl6.cnf")
os.system("touch fl7.cnf")
os.system("touch fl8.cnf")
os.system("touch fl9.cnf")

#os.system("NUL > openssl.cnf")

splitFile1 = 'fl1.cnf'
splitFile2 = 'fl2.cnf'
splitFile3 = 'fl3.cnf'
splitFile4 = 'fl4.cnf'
splitFile5 = 'fl5.cnf'
splitFile6 = 'fl6.cnf'
splitFile7 = 'fl7.cnf'
splitFile8 = 'fl8.cnf'
splitFile9 = 'fl9.cnf'

#confFile = 'openssl.cnf'

fl1 = """
# OpenSSL intermediate CA configuration file.
# Copy to `/root/ca/intermediate/openssl.cnf`.

[ ca ]
# `man ca`
default_ca = BDPEER_CA

#[ CA_default ]
[ BDPEER_CA ]
# Directory and file locations.
"""
caDir = input("Please insert destination location of CA: ")
caDirDefault = "dir               = "
fl2 = str(caDirDefault) + str(caDir)

fl3 = """
certs             = $dir/certs
crl_dir           = $dir/crl
new_certs_dir     = $dir/newcerts
database          = $dir/index.txt
serial            = $dir/serial
RANDFILE          = $dir/private/.rand

# The root key and root certificate.
private_key       = $dir/private/ca.key.pem
certificate       = $dir/certs/ca.cert.pem

# For certificate revocation lists.
crlnumber         = $dir/crlnumber
crl               = $dir/crl/ca.crl.pem
crl_extensions    = crl_ext
default_crl_days  = 30

# SHA-1 is deprecated, so use SHA-2 instead.
default_md        = sha256

name_opt          = ca_default
cert_opt          = ca_default
default_days      = 375
preserve          = no
policy            = policy_loose

[ policy_strict ]
# The root CA should only sign intermediate certificates that match.
# See the POLICY FORMAT section of `man ca`.
 street = supplied
 postalCode = supplied
 stateOrProvinceName = optional
 commonName = supplied
 organizationalUnitName = supplied
 organizationName = supplied
 localityName = supplied
 countryName = supplied
 houseIdentifier = supplied

[ policy_loose ]
# Allow the intermediate CA to sign a more diverse range of certificates.
# See the POLICY FORMAT section of the `ca` man page.

street 			= optional
postalCode 		= optional
stateOrProvinceName	= optional
commonName 		= optional
organizationalUnitName 	= optional
organizationName 	= optional
localityName 		= optional
countryName 		= supplied
houseIdentifier 	= optional

[ req ]
# Options for the `req` tool (`man req`).
default_bits        = 2048
distinguished_name  = req_distinguished_name
string_mask         = utf8only

# SHA-1 is deprecated, so use SHA-2 instead.
default_md          = sha256

# Extension to add when the -x509 option is used.
x509_extensions     = v3_ca

[ req_distinguished_name ]
# See <https://en.wikipedia.org/wiki/Certificate_signing_request>.

street 				= Street Address
postalCode 			= Postal Code
commonName 			= Common Name
organizationalUnitName 		= Organizational Unit Name
organizationName 		= Organization Name
localityName 			= Locality Name
countryName 			= Country Name
houseIdentifier 		= House Identifier

# Optionally, specify some defaults.
 street_default = 22 Kemal Ataturk Avenue
 postalCode_default = 1213
 commonName_default = Computer Services CA 2014
 organizationalUnitName_default = Certifying Authority
 organizationName_default = COMPUTER SERVICES LTD
 localityName_default = Dhaka
 countryName_default = BD
 houseIdentifier_default = 12B Ataturk Tower

[ v3_ca ]
# Extensions for a typical CA (`man x509v3_config`).
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:true
keyUsage = critical, digitalSignature, cRLSign, keyCertSign

[ v3_intermediate_ca ]
# Extensions for a typical intermediate CA (`man x509v3_config`).
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints = critical, CA:true, pathlen:0
keyUsage = critical, digitalSignature, cRLSign, keyCertSign

[ usr_cert ]
# Extensions for client certificates (`man x509v3_config`).
basicConstraints = CA:FALSE
nsCertType = client, email
nsComment = "OpenSSL Generated Client Certificate"
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
keyUsage = critical, nonRepudiation, digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth, emailProtection
"""
crlLoc = input("Please insert CRL URL (plain): ")
crlDefault = "crlDistributionPoints = URI:http://"
fl4 = str(crlDefault) + str(crlLoc)
fl5 = """

[ server_cert ]
# Extensions for server certificates (`man x509v3_config`).
basicConstraints = CA:FALSE
nsCertType = server
nsComment = "BDPEER Generated Server Certificate"
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer:always
keyUsage = critical, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth
"""
fl6 = str(fl4)

fl7= """

[ crl_ext ]
# Extension for CRLs (`man x509v3_config`).
"""
fl8 = str(fl4)
fl9 = """

[ ocsp ]
# Extension for OCSP signing certificates (`man ocsp`).
basicConstraints = CA:FALSE
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer
keyUsage = critical, digitalSignature
extendedKeyUsage = critical, OCSPSigning

"""

#Spliting in new files

with open(splitFile1, 'w') as scom1:
    scom1.write(fl1)

with open(splitFile2, 'w') as scom2:
    scom2.write(fl2)

with open(splitFile3, 'w') as scom3:
    scom3.write(fl3)
    
with open(splitFile4, 'w') as scom4:
    scom4.write(fl4)

with open(splitFile5, 'w') as scom5:
    scom5.write(fl5)

with open(splitFile6, 'w') as scom6:
    scom6.write(fl6)

with open(splitFile7, 'w') as scom7:
    scom7.write(fl7)

with open(splitFile8, 'w') as scom8:
    scom8.write(fl8)

with open(splitFile9, 'w') as scom9:
    scom9.write(fl9)




#Concaternating all files in single file
filenames = ['fl1.cnf', 'fl2.cnf', 'fl3.cnf', 'fl4.cnf', 'fl5.cnf', 'fl6.cnf', 'fl7.cnf', 'fl8.cnf', 'fl9.cnf']

with open('openssl.cnf', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

os.system("rm fl1.cnf fl2.cnf fl3.cnf fl4.cnf fl5.cnf fl6.cnf fl7.cnf fl8.cnf fl9.cnf")


    






