# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:43:25 2018
@author: Alex Salamah 
Section 404
Ansswer for Exercise 1 part 3

This code asks the user select an action encrypt or decrypt then it prompts 
the user to input the message.  Code can handle / process any input i.e.
it can handle Alpha, numbers, alphanumeric and special charaters.

Per Homework 2 Exercise 1 step 3, this is a cyclic cipher that encrypts 
Alpha entered by the user into a coded message based on the shift key provided
by the user.  This code also uses the modulus operator to encrypt numbers while
keeping the values between 0 and 5. This per requirement of part 3 of the
excersise.   

For example, the inpurt sequence: 012345 will result in an encoded
value of  456789 if we use a simple shift with avalue of 4.  Howver, the
requirement is keep the values between 0 and 5. 
To do this we will use the modulus operator and the result of the operation
will be: 450123

"""

#Caesar Cipher

#the key used in the cipher should be between 1 and 26.
MAX_KEY_SIZE=26

# Capture user input to decide if they want ton encrypt or decrypt 
# if statement validates the input to be one of the following:
# encrypt, e, decrypt or d
def getMode():
      while True:
             print('Do you wish to encrypt or decrypt a message?')
             mode = input().lower()
             if mode in 'encrypt e decrypt d'.split():
                 return mode
             else:
              print('Enter either "encrypt" or "e" or "decrypt" or "d".')

# Ask the user to input the message they want to encrypt or decrypt
def getMessage():
    print('Enter your message:')
    message = input()
    return message

# Ask the user to input the shift key.  Valid values are between 1 & 26
def getKey():
    key = 0
# keep looping until we get a valid key...
# may need a way to exit maybe use a counter?
    while True:
       print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
# make sure we return an integer....       
       key = int(input())
       if (key >= 1 and key <= MAX_KEY_SIZE):
           return key
       

def getTranslatedMessage(mode, message, key):
          translated = ''
          symbol = 0
          num=0

          for symbol in message:
              if symbol.isalpha():
              # convert letters to their ordinal value using the ord function
                  num = ord(symbol)
                  # add the shift key to the ordinal value
                  num += key
                  #print (num)

                  if symbol.isupper():
                      # if the symbol is the letter Z that will cause num to
                      # have an value that does not correspond to a letter
                      # we need to wrap around 
                      if num > ord('Z'):
                          num -= 26
                      elif num < ord('A'):
                          num += 26
                  elif symbol.islower():
                      if num > ord('z'):
                          num -= 26
                      elif num < ord('a'):
                          num += 26
                  translated += chr(num)
              elif symbol.isnumeric():
                  num = int(symbol)
                  num += int(key)
                  num = num%6
                  #print(num)
                  translated += str(num)
              else:
                  translated += symbol
          return translated


# Call the getMode function and catch it's return value
mode = getMode()
# Debug statement keep commented unless we are debugging 
#print('Your Mode is:' + str(mode))
# Call the getMessage function and catch it's return value

message = getMessage()
# Debug statement keep commented unless we are debugging 
#print('Your message is:' + str(message))
# Call the getKey function and catch it's return value

key = getKey()
# Debug statement keep commented unless we are debugging 
#print('Your key is:' + str(key))
 
#if the user wants to decrypt the message, then we need to negate the key i.e.
# make it negative.
if mode[0] == 'd':
          key = -key

#call the encrypt/decrypt function and catch it's return value
decodedmsg= getTranslatedMessage(mode, message, key)
# tell the user the result of the encryption or decryption 
if decodedmsg.isnumeric():
    print ('Your translated number is:' + (decodedmsg))
else:
    print('Your translated text is:' + str(decodedmsg))