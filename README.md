# aes-cbc-bit-flipping-solver
AES-CBC Bit Flipping Solver

## Usage

```
python decoder.py -h
usage: decoder.py [-h] -k KC -p KP -i INDEX -c CHAR

AES-CBC Bit Flipping Solver

optional arguments:
  -h, --help            show this help message and exit
  -k KC, --known-ciphertext KC
                        Known ciphertext in hex format
  -p KP, --known-plaintext KP
                        Known plaintext
  -i INDEX, --index INDEX
                        Index of char you need to change in the known
                        plaintext
  -c CHAR, --char CHAR  Char that you want to replace the original with
```

### Example

```
python decoder.py -k "d524b1d6c2485db9b4917c2f1cf4a8b29dfd098a859b8735807a4852bc36b0f8d54546428fc9391fbbfed2d39318c5f3"
                  -p "logged_username=admin&password=super_secret_pwd" 
                  -i 16 
                  -c "b"
```
