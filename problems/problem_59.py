"""
XOR decryption
--------------

Each character on a computer is assigned a unique code and the preferred standard is ASCII
(American Standard Code for Information Interchange). For example, uppercase A = 65,
asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte
with a given value, taken from a secret key. The advantage with the XOR function is that using the
same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is
made up of random bytes. The user would keep the encrypted message and the encryption key in
different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a
password as a key. If the password is shorter than the message, which is likely, the key is
repeated cyclically throughout the message. The balance for this method is using a sufficiently
long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII
codes, and the knowledge that the plain text must contain common English words, decrypt the
message and find the sum of the ASCII values in the original text.
"""

from utils.timer import time_it
from itertools import product, cycle

from string import ascii_lowercase

#-------------------------------------------------------------------------------------------------

def get_bytes_from_file():
    with open(r'resources\problem_059_cipher.txt') as f:
        for line in f:
            return [int(x) for x in line.split(',')]

@time_it
def problem_59():

    common_english_words = ['the', 'of', 'be', 'to', 'and', 'in', 'that', 'have']

    for password in product(ascii_lowercase, repeat=3):
        password = [ord(c) for c in password]

        decrypted_bytes = list(i^p for i, p in zip(get_bytes_from_file(), cycle(password)))
        text = ''.join(chr(i) for i in decrypted_bytes)

        if len([1 for word in common_english_words if word in text]) > 5:
            print(text)
            print('\n{}'.format(sum(decrypted_bytes)))
            print('\n{}'.format(''.join(chr(i) for i in password)))
            break

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_59()
