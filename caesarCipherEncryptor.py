# Author : Ondřej Maceška 
# Date : 25.6.2022
# Task : https://www.algoexpert.io/questions/caesar-cipher-encryptor

# O(n) time, O(n) space 
def caesar_cipher_encryptor(string, key):
    """ encrypts a string using a caesar cipher
        
    Args:
        string (string) : string we want to encrypt
        key (int) : key we want to apply to the string

    Returns:
        string: encoded string
    """
    alphabet = [char for char in "abcdefghijklmnopqrstuvwxyz"]
    print(alphabet)
    encoded = ""
    for char in string:
        char_index = alphabet.index(char)
        new_index = (char_index + key) % len(alphabet)
        encoded += alphabet[new_index]
    return encoded
