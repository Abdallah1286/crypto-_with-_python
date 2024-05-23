import sys
from hashlib import *
from Crypto.Util.number import *

usage = "Usage:\n> python verify.py [firmware] [signature] [pubkey]"
if len(sys.argv) < 2:
    print(usage)
    exit()

FirmwareFile=sys.argv[1]
with open(FirmwareFile,"rb") as file :
    firmware_main = file.read()

hash=sha256()
hash.update(firmware_main)
hash.digest()
hash_firmware=bytes_to_long(hash.digest())

sign_file= sys.argv[2]
with open(sign_file,'rb') as file:
    sign_file2=int(file.read().decode())

pub_key= sys.argv[3]
with open(pub_key,'rb') as file:
    e=file.readline()
    n=file.readline()
e=int(e.decode())
n=int(n.decode())
calc_sign=pow(sign_file2,e,n)

# verification
if calc_sign == hash_firmware:
    print("verified")
else:
    print("failed")