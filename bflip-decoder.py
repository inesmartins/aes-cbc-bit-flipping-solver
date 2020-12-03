import os
import sys
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

    gp = "logged_username=admin&password=super_secret_pwd"   # known plaintext
    tp = "logged_username=bdmin&password=super_secret_pwd"   # test plaintext (changed 'admin' to 'bdmin')
    ciphertext = aes.encrypt(pad(tp))                  # known ciphertext

    flipped_iv_char = chr(ord(ciphertext[0]) ^ ord("a") ^ ord("b"))
    flipped_ciphertext = flipped_iv_char + ciphertext[1:]
    decrypted = aes.decrypt(flipped_ciphertext)
    decrypted_msg = decrypted[16:]

    print("\nOriginal random iv:      " + iv.encode("hex"))
    print("Original random key:     " + key.encode("hex"))
    print("Original/Goal message:   " + gp)
    print("Original AES ciphertext: " + ciphertext.encode("hex"))
    print("Flipped ciphertext:      " + flipped_ciphertext.encode("hex"))
    print("\nMessage decrypted from flipped ciphertext: " + decrypted_msg)

def main(argv):
    try:
        kc = argv[0].decode("hex")   # known ciphertext in hex format
        gp = argv[1]                 # goal plaintext
        pp = int(argv[2])            # position in goal plaintext that you need to change
        test_char = argv[3]          # char that you want to use to replace original

        original_char = gp[pp]
        pos_in_iv = pp % iv_length % 1 * iv_length
        flipped_iv_char = chr(ord(kc[pos_in_iv]) ^ ord(original_char) ^ ord(test_char))
        flipped_ciphertext = (kc[:pos_in_iv] + flipped_iv_char + kc[pos_in_iv+1:]).encode("hex")
        print("Result: " + flipped_ciphertext)

    except(Exception):
        print("Invalid params")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Please specify the following arguments:")
        print("[0] known ciphertext in hex format")
        print("[1] goal plaintext")
        print("[2] position in goal plaintext that you need to change")
        print("[3] char that you want to use to replace original")
    main(sys.argv[1:])