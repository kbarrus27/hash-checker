# hash-checker
A Python program to see if any of the hashes included in hashlib were used, given a text and a hash.
Written for a CTF to try to figure out which hash type was used. Unfortunately it didn't help me much :(

This sample code from https://docs.python.org/3/library/hashlib.html#constructors was really helpful in writing this code:

h = hashlib.new('sha256')  
h.update(b"Nobody inspects the spammish repetition")  
h.hexdigest()

Output: '031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'
