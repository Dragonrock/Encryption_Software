# -*- coding: utf-8 -*-
import random
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 13
extra_letters = ["α","σ","δ","φ","γ","η","ξ","κ","λ","ς","ε","ρ","τ","υ","θ","ι","ο","π","ζ","χ","ψ","ω","β","ν","μ","a","s","d","f","g","h","j","k","l","q","w","e","r","t","y","u","i","o","p","z","x","c","v","b","n","m"]
def Encode(encrypted_message1):
 message = input('Please enter a phrase in lowercase: ')
 for character in message:
  position = alphabet.find(character)
  new_position = (position + key) % 26
  new_character = alphabet [new_position]
  encrypted_message1 += new_character
  encrypted_message = encrypted_message1.split()
 if len(message) <= 10:
  encrypted_message.insert(0,random.choice(extra_letters))
  encrypted_message.insert(3,random.choice(extra_letters))
  encrypted_message.insert(4,random.choice(extra_letters))
  encrypted_message.insert(2,random.choice(extra_letters))
  encrypted_message.insert(7,random.choice(extra_letters))
  encrypted_message.insert(9,random.choice(extra_letters))
  encrypted_message.insert(5,random.choice(extra_letters))
  encrypted_message2 = ''.join(encrypted_message)
  print (encrypted_message2)
  main()
 else:
    print ("Too big")
    main()
def Decode(new_message):
 message1 = input('Please enter a message to decode: ')
 if len(message1) == 8:
     m = message1[1]
 elif len(message1) == 9:
     m = message1[1:3]
 elif len(message1) == 10:
     m = message1[1:4]
 elif len(message1) == 11:
     m = message1[1:5]
 elif len(message1) == 12:
     m = message1[1:6]
 elif len(message1) == 13:
     m = message1[1:7]
 elif len(message1) == 14:
     m = message1[1:8]   
 elif len(message1) == 15:
     m = message1[1:9]
 elif len(message1) == 16:
     m = message1[1:10]
 elif len(message1) == 17:
     m = message1[1:11]
 elif len(message1) == 18:
     m = message1[2:12]
 for character in m:
  position = alphabet.find(character)
  new_position = (position - key) % 26
  new_character = alphabet [new_position]
  new_message += new_character
 print (new_message)
 main()
def Keychange():
 key = input('Chose a key 1-23:')
 answer1 = input('Encode or Decode:')
 if answer1 == "Encode":
  Encode('')
 elif answer1 == "Decode":
  Decode('')
 main()
def Help():
 print ("This app was made for fun and the creator is not responsible for its misuse")
 print ("This is an encrytpion algorithm which uses greek and english letters to encode a message(in Enlgish).There is also a decoder which reverses the algorithm to reveal the hidden message in an ecrypted phrase made with this programm.")
 main()
def main():
 print ("Encode  Decode  Keychange Help")
 answer = input()
 if answer == "Encode":
    Encode('')
 elif answer == "Decode":
    Decode('')
 elif answer == "Keychange":
    Keychange()
 else:
  Help()
if __name__ == "__main__":
 main()