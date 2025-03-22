# Homophonic Substitution Cipher with Key V1.0

## Description
This Python program implements a homophonic substitution cipher. It allows you to generate a random cipher key, encrypt messages by replacing each letter with one of three corresponding numeric values, and decrypt messages by reversing the substitution. The cipher key is saved as a file for later use.

## Features
✅ **Key Generation**: Automatically creates a cipher key where each uppercase letter (A–Z) is mapped to 3 unique numbers from 100 to 999.<br/>
✅ **Encryption**: Converts a plaintext message into a sequence of numbers by substituting each letter with a random choice from its corresponding numbers.<br/>
✅ **Decryption**: Reverses the process by mapping the numbers back to their corresponding letters.<br/>
✅ **Key Persistence**: Save and load cipher key into a file.<br/>
✅ **Command-Line Interface**: Interactive menu for generating keys, encrypting and decrypting messages.<br/>

## Installation
1. **Prerequisites**:  
   - Ensure you have [Python 3](https://www.python.org/downloads/) installed.
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/Asttraios/Homophonic-Substitution-Cipher-with-Key.git
3. **Navigate to the project directory**:
```bash
cd Homophonic-Substitution-Cipher-with-Key
```
4. **Usage**
To run the program, simply execute:
```bash
python run.py
```
This will start the command-line interface where you can:
- Generate a new key
- Encrypt a message
- Decrypt a message
- Exit the application

## **How does it work?**
Encryption:
- The input message is converted to uppercase.
- For each letter in the message, the program randomly selects one of the three numbers associated with that letter.
- The numbers are joined (separated by spaces) to form the encrypted message.

Decryption:

- The encrypted message (a string of numbers separated by spaces) is split into individual numeric tokens.
- A reverse mapping of the cipher key is created to map each number back to its corresponding letter.
- The numbers are then replaced by their respective letters to reconstruct the original message.
