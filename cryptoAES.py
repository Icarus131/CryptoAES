from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import time
 
start = time.time()

key = b'mysecretpassword'

cipher = AES.new(key, AES.MODE_CBC)

plaintext = b'falkensmaze'

ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

time.sleep(1)

print(cipher.iv)

end = time.time()  


print(f"Runtime is {end - start}")