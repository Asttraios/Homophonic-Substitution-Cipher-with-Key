import random
import json
import string
import os

def generate_key():
    #generowanie klucza
    alfabet = string.ascii_uppercase                 #zmienna alfabet to gotowy string "ABCDEFGHIJKLMNOPQRSTUVWXYZ" - ascii_uppercase czyli wszystkie (wielkie) litery angielskiego alfabetu
    key = {}                                         #zmienna key typu dictionary - sklada sie z par klucz-wartosc (klucz jest "tlumaczony" na wartosc, dziala podobnie jak typowy slownik)
    cipher_letter_value = list(range(100, 1000))     #lista liczb od 100 do 999 - wartosci liter
    random.shuffle(cipher_letter_value)              #losowo zmien kolejnosc liczb
    

    #petla przechodzi przez wszystkie litery alfabetu 
    #kazdej literze alfabetu sa przypiswyane po 3 losowe liczby np "A":[123, 456, 789].
    #Jest tworzona nowa, zastepcza lista cipher_letter_value z liczbami ktore NIE zostaly uzyte do szyfrowania
    for letter in alfabet:                             
        key[letter] = random.sample(cipher_letter_value, 3)
        cipher_letter_value = [num for num in cipher_letter_value if num not in key[letter]]      #list comprehension
    
    return key              #zwrocenie klucza

def encrypt(message, key):      #funkcja szyfrujaca
    
    message = message.upper()           #wszystkie litery w jawnej wiadomosci uzytkownika sa zamieniane na wielkie
    encrypted_message = []              #zaszyfrowana wiadomosc
    
    #petla przechodzi przez wszystkie litery wiadomosci uzytkownika ktora ma byc zaszyfrowana
    #jesli litera w wiadomosci jest w slowniku 'key', to do listy encrypted_message, ktora jest zaszyfrowana wiadomoscia
    #dodawana jest losowo jedna z 3 liczb odpowiadajaca okreslonej literze. W przeciwnym wypadku znak ktorego nie ma 
    # w alfabecie jest przepisywany bez zmian
    for letter in message:          
        if letter in key:
            encrypted_message.append(str(random.choice(key[letter])))
        else:
            continue
            #encrypted_message.append(letter)
    
    return ' '.join(encrypted_message)


    #funkcja deszyfrujaca 
    #zmienna reverse_key jest typu slownik - tutaj odwraca mapowanie klucza szyfrujacego - klucz szyfrujacy mapuje litery na liczby, a klucz deszyfrujacy
    #liczby na litery.
    # 
    # str(letter_value): letter - tworzenie pary klucz-wartosc (liczba-litera). liczba (klucz) jest zmieniana na stringa
    #for letter, numbers in key.items() - zewnetrzna petla iterujaca po parach klucz-wartosc
    #for letter_value in numbers - wewnetrzna petla iterujaca po liczbach przypadajaca na kazda litere
def decrypt(ciphertext, key):
    
    reverse_key = {str(letter_value): letter for letter, numbers in key.items() for letter_value in numbers}      #dictionary comprehension
    decrypted_message = []
    
    #np.
    # '151' : 'A'
    # '165' : 'A'
    # '567' : 'A'
    

    #funkcja split() dzieli stringa 'ciphertext' (zaszyfrowana wiadomosc) na czesci
    #petla iteruje po kazdej czesci (po kazdej liczbie z zakresu 100-999)
    #Jesli jest w kluczu odszyfrowujacym, to tej liczbie przypisywana jest odpowiednia litera
    # w przeciwnym wypadku przepisywany jest znak/liczba bez zmian
    for symbol in ciphertext.split():
        if symbol in reverse_key:
            decrypted_message.append(reverse_key[symbol])
        else:
            decrypted_message.append(symbol)
    
    return ''.join(decrypted_message)


def save_key(key, filename):                    #zapisanie klucza jako plik w folderze programu

    with open(filename, 'w') as file:
        json.dump(key, file)

def load_key(filename):
                                                #wczytanie klucza
    with open(filename, 'r') as file:
        return json.load(file)

def main():
    while True:
        print("Homophonic Substitution Cipher with Key V1.0")
        print("1. Wygeneruj nowy klucz")
        print("2. Zaszyfruj wiadomosc")
        print("3. Odszyfruj wiadomosc")
        print("4. Wyjdz")
        
        choice = input("Wybierz opcje: ")
        
        if choice == '1':
            key = generate_key()
            filename = input("Podaj nazwe klucza, aby zapisac go jako plik: ")
            try:
                save_key(key, filename)
                print(f"Klucz zapisany jako {filename}")
            except:
                print("Nie udalo sie zapisac klucza. Sprobuj ponownie!")
                
        
        elif choice == '2':
            filename = input("Podaj nazwe pliku (klucza): ")
            try:
                key = load_key(filename)
                message = input("Podaj wiadomosc do zaszyfrowania: ")
                encrypted_message = encrypt(message, key)
                print(f"Zaszyfrowana wiadomosc: {encrypted_message}")
            except:
                print("Blad podczas wczytywania klucza. Upewnij sie ze zostal wygenerowany.")
        
        elif choice == '3':
            filename = input("Podaj nazwe pliku (klucza): ")
            try:
                key = load_key(filename)
                ciphertext = input("Podaj zaszyfrowany tekst: ")
                decrypted_message = decrypt(ciphertext, key)
                print(f"Odszyfrowana wiadomosc: {decrypted_message}")
            except:
                print("Blad podczas wczytywania klucza. Upewnij sie ze zostal wygenerowany")                

        elif choice == '4':
            break
        
        else:
            print("Zly wybor.")

