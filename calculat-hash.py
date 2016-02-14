#!/usr/bin/env python

"""
Ahod Alghuried, D15123616
Mobile Forinsic, Lab #2


This Python program has been desined to check the integrity of files. It is calculate the hash code for SHA-1, SHA256 ,SHA512 , SHA3_256 and SHA3_384.

To get SHA-3 you might have to download (pip python) from this link https://pypi.python.org/pypi . After download get-pip.py . Open terminal and write this command " pip install pysha3".
Then you will be able to import sha3.



"""


import sys
import getopt
import hashlib
import sha3
from sha3 import sha3_256, sha3_384


try: 
    hash_get = sys.argv[1]
except:
    print "*** You have to enter file ***"




def SHA1(filePath):
# To make a hash object 
   h = hashlib.sha1()
 # open file for reading in binary mode
   with open(filePath,'rb') as fh:

# loop till the end of the file
       chunk = 0
       while chunk != b'':
# read only 1024 bytes at a time
           chunk = fh.read(1024)
           h.update(chunk)
 # return the hex representation of digest
   return h.hexdigest()

  
def SHA256(filePath):
   h = hashlib.sha256()
# open file for reading in binary mode
   with open(filePath,'rb') as fh:
# loop till the end of the file
       chunk = 0
       while chunk != b'': 
           chunk = fh.read(1024)
 # read only 1024 bytes at a time
           h.update(chunk)
  # return the hex representation of digest
   return h.hexdigest()



def SHA512(filePath):
   h = hashlib.sha512()
# open file for reading in binary mode
   with open(filePath,'rb') as fh:
# loop till the end of the file
       chunk = 0
       while chunk != b'':
           chunk = fh.read(1024)
 # read only 1024 bytes at a time
           h.update(chunk)
  # return the hex representation of digest
   return h.hexdigest()



def SHA3_256(filePath):
   h = sha3.sha3_256()
 # open file for reading in binary mode
   with open(filePath,'rb') as fh:
  # loop till the end of the file
       chunk = 0
       while chunk != b'':
 # read only 1024 bytes at a time
           chunk = fh.read(1024)
           h.update(chunk)
 # return the hex representation of digest
   return h.hexdigest()





def SHA3_384(filePath):
 # make a hash object
   h = sha3.sha3_384()
   with open(filePath,'rb') as fh:
  # loop till the end of the file
       chunk = 0
       while chunk != b'':
 # read only 1024 bytes at a time
           chunk = fh.read(1024)
           h.update(chunk)
# return the hex representation of digest
   return h.hexdigest()



if hash_get:
   
    print('The SHA1 is', SHA1(hash_get))
    print('The SHA256 is', SHA256(hash_get))
    print('The SHA512 is', SHA512(hash_get))
    print('The SHA3_256 is', SHA3_256(hash_get))
    print('The SHA3_384 is', SHA3_384(hash_get))

