#                     CIFRA DE VIGENERE / VIGENERE'S CIPHER


def key_generator(txt, kw):
    # Matches the key lenght to the text lenght and returns the key with
    # all characters in uppercase.

    # Tranforms the string with the keyword in a list.
    k = list(kw)

    # Repeats the keyword characters enough times to match the lenght of the
    # text.
    for j in range((len(txt)-len(kw)+1)):
        k.append(kw[j])

    key = "".join(k)
    return key.upper()


def cipher_encrypt(txt, kw):
    # Receives a text and a key to encrypt the text.

    enc_txt = ""
    key = key_generator(txt, kw)

    for i in range(len(txt)):
        # Get a character from the text.
        char = txt[i]
        # Transforms the letter from the keyword in the offset number.
        offset = ord(key[i]) - 65

        # Character is uppercase.
        if char.isupper():
            enc_txt += chr((ord(char) + offset - 65) % 26 + 65)
        # Character is lowercase.
        elif char.islower():
            enc_txt += chr((ord(char) + offset - 97) % 26 + 97)
        # Character is a space.
        elif char == " ":
            enc_txt += char

    return enc_txt


def cipher_decrypt(txt, kw):
    # Receives the encrypted text and the key to decrypt the text.

    dec_txt = ""
    key = key_generator(txt, kw)

    for i in range(len(txt)):
        # Get a character from the text.
        char = txt[i]
        # Transforms the letter from the keyword in the offset number.
        offset = ord(key[i]) - 65

        # The character is uppercase.
        if char.isupper():
            dec_txt += chr((ord(char) - offset - 65) % 26 + 65)
        # The character is lowercase.
        elif char.islower():
            dec_txt += chr((ord(char) - offset - 97) % 26 + 97)
        # The character is a space.
        elif char == " ":
            dec_txt += char

    return dec_txt


action = input("Press 'E' to encrypt or 'D' to decrypt: ")

# User select Encrypt.
if action.upper() == "E":
    text = input("Text that will be encrypted: ")
    keyword = input("Enter the key: ")

    # Tests for a valid key.
    if keyword.isalpha():
        print(f"Encrypted text:\n {cipher_encrypt(text, keyword)}")

    else:
        print(f"Invalid key. The key must have only characters from 'A-Z' "
              f"or from 'a-z'.")

# User selected Decrypt.
elif action.upper() == "D":
    text = input("Text that will be decrypted: ")
    keyword = input("Enter the key: ")

    # Tests for a valid key.
    if keyword.isalpha():
        print(f"Decrypted text:\n {cipher_decrypt(text, keyword)}")

    else:
        print(f"Invalid key. The key must have only characters from 'A-Z' "
              f"or from 'a-z'.")
