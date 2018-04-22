# -*- coding: utf-8 -*-
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 13
print ("Encode or Decode")
answer = input()
def Encode(encrypted_message1):
 message = input('Please enter a phrase in lowercase: ')
 for character in message:
  position = alphabet.find(character)
  new_position = (position + key) % 26
  new_character = alphabet [new_position]
  encrypted_message1 += new_character
  encrypted_message = encrypted_message1.split()
 if len(encrypted_message) < 10:
  encrypted_message.insert(0,"σα")
  encrypted_message.insert(3,"geo")
  encrypted_message.insert(4,"lfg")
  encrypted_message.insert(2,"πς")
  encrypted_message.insert(7,"αs")
  encrypted_message.insert(9,"sqπ")
  encrypted_message.insert(5,"χψασ")
  encrypted_message2 = ''.join(encrypted_message)
  print (encrypted_message2)
 else:
    print ("Too big")
def Decode(new_message):
 message1 = input('Please enter a message to decode: ')
 if len(message1) == 20:
     m = message1[2]
 elif len(message1) == 21:
     m = message1[2:3]
 elif len(message1) == 22:
     m = message1[2:4]
 elif len(message1) == 23:
     m = message1[2:5]
 elif len(message1) == 24:
     m = message1[2:6]
 elif len(message1) == 25:
     m = message1[2:7]
 elif len(message1) == 26:
     m = message1[2:8]
 elif len(message1) == 27:
     m = message1[2:9]
 elif len(message1) == 28:
     m = message1[2:10]
 elif len(message1) == 29:
     m = message1[2:11]
 elif len(message1) == 30:
     m = message1[2:12]
 for character in m:
  position = alphabet.find(character)
  new_position = (position - key) % 26
  new_character = alphabet [new_position]
  new_message += new_character
 print (new_message)
if answer == "Encode":
    Encode('')
elif answer == "Decode":
    Decode('')
