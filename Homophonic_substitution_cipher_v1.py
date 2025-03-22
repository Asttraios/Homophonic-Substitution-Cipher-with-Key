import random
import json
import string
import os

def GenerateKey():
    # Generate the cipher key
    alphabet = string.ascii_uppercase                       # Uppercase English letters: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}                                                # Dictionary to store letter-number mappings
    cipher_letter_value = list(range(100, 1000))            # List of numbers from 100 to 999
    random.shuffle(cipher_letter_value)                     # Shuffle the numbers randomly

    # Assign each letter 3 unique random numbers
    for letter in alphabet:
        key[letter] = random.sample(cipher_letter_value, 3)

        # Remove used numbers from the list - avoid repetition. Eacch letter must have 3 unique numbers
        cipher_letter_value = [num for num in cipher_letter_value if num not in key[letter]]
    
    return key

def Encrypt(message, key):
    # Convert message to uppercase
    message = message.upper()
    encrypted_message = []
    
    # Replace each letter in the message with a randomly chosen corresponding number (1 of 3)
    for letter in message:
        if letter in key:
            encrypted_message.append(str(random.choice(key[letter])))
        else:
            continue  # Ignore characters that are not in the alphabet
    
    return ' '.join(encrypted_message)

def Decrypt(ciphertext, key):
    # Reverse the key mapping: map numbers back to their corresponding letters
    # Dictionary comprehension
    # str(letter_value): letter - create a dictionary with number as key and letter as value
    # for letter, numbers in key.items() - iterate over the key dictionary
    # for letter_value in numbers - iterate over the list of numbers for each letter
    reverse_key = {str(letter_value): letter for letter, numbers in key.items() for letter_value in numbers}
    decrypted_message = []
    
    # Split the encrypted text into numbers and convert them back to letters
    for symbol in ciphertext.split():
        if symbol in reverse_key:
            decrypted_message.append(reverse_key[symbol])
        else:
            decrypted_message.append(symbol)  # Keep any unrecognized symbols unchanged
    
    return ''.join(decrypted_message)

def SaveKey(key, filename):
    # Save the cipher key as a JSON file
    with open(filename, 'w') as file:
        json.dump(key, file)

def LoadKey(filename):
    # Load the cipher key from a JSON file
    with open(filename, 'r') as file:
        return json.load(file)

def main():
    while True:
        print("Homophonic Substitution Cipher with Key V1.0")
        print("1. Generate a new key")
        print("2. Encrypt a message")
        print("3. Decrypt a message")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            key = GenerateKey()
            filename = input("Enter a filename to save the key: ")
            try:
                SaveKey(key, filename)
                print(f"Key saved as {filename}")
            except:
                print("Failed to save the key. Please try again!")
                
        elif choice == '2':
            filename = input("Enter the key filename: ")
            try:
                key = LoadKey(filename)
                message = input("Enter the message to Encrypt: ")
                encrypted_message = Encrypt(message, key)
                print(f"Encrypted message: {encrypted_message}")
            except:
                print("Error loading the key. Make sure it has been generated.")
        
        elif choice == '3':
            filename = input("Enter the key filename: ")
            try:
                key = LoadKey(filename)
                ciphertext = input("Enter the encrypted text: ")
                decrypted_message = Decrypt(ciphertext, key)
                print(f"Decrypted message: {decrypted_message}")
            except:
                print("Error loading the key. Make sure it has been generated.")

        elif choice == '4':
            break
        
        else:
            print("Invalid choice.")
