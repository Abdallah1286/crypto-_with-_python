import sys
from hashlib import *
from Crypto.Util.number import *

usage = "Usage:\n> python sign.py [firmware]\nexpected output: fw_signature.txt public_key.txt"
if len(sys.argv) < 2:
    print(usage)
    exit()

FirmwareFile = sys.argv[1]
with open(FirmwareFile,"rb") as file:
    firmware = file.read()

hash=sha256()
hash.update(firmware)
hash.digest()
hash_firmware=bytes_to_long(hash.digest())

p = getPrime(1024)
q = getPrime(1024)
n = p * q
phi = (p-1) * (q-1)
e = (2**16)+1
d = pow(e, -1, phi)

signature=pow(hash_firmware,d,n)
output_sign=open("fW_signature.txt",'w')
output_sign.write(str(signature))
with open("public_key.txt","w") as public:
    public.write(str(e)+"\n")
    public.write(str(n))
