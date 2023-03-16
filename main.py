import sys
from args import getArguments
from tridigital import tridigital_decipher
from atbash import decrypt_atbash
from vigenere import vigenere_cipher
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s | %(message)s")

options = getArguments(sys.argv[1:])

tridigital = tridigital_decipher(options.second, options.middle, options.bottom, int(options.indicators))
atbash = decrypt_atbash(options.encrypted)
vig = vigenere_cipher(atbash, tridigital)
logging.info(f"Final result: {vig}")