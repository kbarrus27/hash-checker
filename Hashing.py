'''
Written for a CTF to try to figure out which hash type was used given text and a key. Unfortunately it didn't help me much :(
This sample code from https://docs.python.org/3/library/hashlib.html#constructors was really helpful in writing this code:

h = hashlib.new('sha256')
h.update(b"Nobody inspects the spammish repetition")
h.hexdigest()

Output: '031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'

'''

import hashlib
hashes = hashlib.algorithms_guaranteed
input_text = input("What is the text to be hashed? ")
hash_to_check = input("What is the hashed version of the text? ")

for hash in hashes:
    h = hashlib.new(hash)
    h.update(bytes(input_text, "utf-8"))
    print("Testing hash type: " + hash)
    if "shake" in hash:
        for i in range(0,256):
            print("Hashed password: " + h.hexdigest(i))
            if h.hexdigest(i) == hash_to_check:
                print("I found it! This password was hashed using ", hash, " with length ", i)
                exit()
            else:
                print("Hmm...no luck here.")
    else:
        print("Hashed password: " + h.hexdigest())
        if h.hexdigest() == hash_to_check:
            print("I found it! This password was hashed using ", hash)
            exit()
        else:
            print("Hmm...no luck here.")