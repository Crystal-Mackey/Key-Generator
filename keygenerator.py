import hashlib
import secrets
import random

# https://pynative.com/python-secrets-module/   --- source to figure out how to do it

def generate_key():
    bits = secrets.randbits(256) 
    bits_hex = hex(bits)
    global gen_key
    gen_key = bits_hex[3:]
    print(gen_key)
    print(len(gen_key))

generate_key()

def validate_key(gen_key):
    guess = input('Key is 63 characters, a mix of letters and numbers. Guess:')
    print(secrets.compare_digest(gen_key, guess))

validate_key(gen_key)