import os
import sys
import argparse
from Crypto.Cipher import AES

iv_length = 16
key_length = 16

def pad(msg):
    pad_size = AES.block_size - (len(msg) % AES.block_size)
    return msg + chr(pad_size) * pad_size

def test_mode():
    key = os.urandom(key_length)
    iv = os.urandom(iv_length)
    aes = AES.new(key, AES.MODE_CBC, iv)

    kp = "logged_username=admin&password=super_secret_pwd"   # known plaintext
    tp = "logged_username=bdmin&password=super_secret_pwd"   # test plaintext (changed 'admin' to 'bdmin')
    ciphertext = aes.encrypt(pad(tp))                        # ciphertext resulting from AES encryption

    flipped_iv_char = chr(ord(ciphertext[0]) ^ ord("a") ^ ord("b"))
    flipped_ciphertext = flipped_iv_char + ciphertext[1:]
    decrypted = aes.decrypt(flipped_ciphertext)
    decrypted_msg = decrypted[16:]

    print("\nOriginal random iv:      " + iv.encode("hex"))
    print("Original random key:     " + key.encode("hex"))
    print("Original/Goal message:   " + kp)
    print("Original AES ciphertext: " + ciphertext.encode("hex"))
    print("Flipped ciphertext:      " + flipped_ciphertext.encode("hex"))
    print("\nMessage decrypted from flipped ciphertext: " + decrypted_msg)

# parses arguments
parser = argparse.ArgumentParser(description='AES-CBC Bit Flipping Solver')
parser.add_argument('-k', '--known-ciphertext', 
					dest='kc', 
					help='Known ciphertext in hex format', 
					type=str, required=True)
parser.add_argument('-p', '--known-plaintext', 
					dest='kp', 
					help='Known plaintext', 
					type=str, required=True)
parser.add_argument('-i', '--index', 
					dest='index', 
					help='Index of char you need to change in the known plaintext', 
					type=int, required=True)
parser.add_argument('-c', '--char', 
					dest='char', 
					help='Char that you want to replace the original with', 
					type=str, required=True)
args = parser.parse_args()

kc = args.kc.decode("hex")   # known ciphertext in hex format
kp = args.p                  # known plaintext
char_index = args.index      # index of the char you need to change in the known plaintext
test_char = args.char[0]     # char that you want to use to replace the original with

original_char = kp[char_index]
pos_in_iv = char_index % iv_length % 1 * iv_length
flipped_iv_char = chr(ord(kc[pos_in_iv]) ^ ord(original_char) ^ ord(test_char))
flipped_ciphertext = (kc[:pos_in_iv] + flipped_iv_char + kc[pos_in_iv+1:]).encode("hex")
print("Result: " + flipped_ciphertext)
