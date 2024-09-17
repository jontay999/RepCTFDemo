"""
basic setup (can use virtual environments / conda if you know how)

python3 -m pip install pwntools
python3 -m pip install pycryptodome
python3 -m pip install libnum

"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Keys need to be 16 bytes
key = b"this_is_a_key"

# so we pad it to be 16 bytes
BLOCK_SIZE = 16
padded_key = pad(key,BLOCK_SIZE)
print(padded_key)

# Creates a AES cipher that uses the given key to encrypt or decrypt
cipher = AES.new(padded_key, mode=AES.MODE_ECB)

# my secret message that I encrypted beforehand
# secret_message = b"XXXXXXXXXXXXXX"
# encrypted_text = cipher.encrypt(pad(secret_message, BLOCK_SIZE))
# print((encrypted_text).hex())

encrypted_text = "e4d0d5a7add6c8ce09588a34f2e133ec4ca81cf96883ae3ba945c2e8c5ed4f2a"

"""
EXERCISE:

WHAT DOES THE ENCRYPTED_TEXT SAY?
"""

# decrypted_text = ?????


