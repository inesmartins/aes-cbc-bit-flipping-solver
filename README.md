# aes-cbc-bit-flipping-solver
AES-CBC Bit Flipping Solver

## Usage

`python decoder.py [ciphertex_in_hex] [known_plaintext] [index_of_char_to_replace] [test_char]`

- [0] known ciphertext in hex format
- [1] the plaintext that corresponds to the ciphertext
- [2] index of the char you need to change in the known plaintext
- [3] char that you want to use to replace the original with

### Example

`python decoder.py "d524b1d6c2485db9b4917c2f1cf4a8b29dfd098a859b8735807a4852bc36b0f8d54546428fc9391fbbfed2d39318c5f3" "logged_username=admin&password=super_secret_pwd" 16 "b"`
