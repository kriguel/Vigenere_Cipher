##                     CIFRA DE VIGENERE / VIGENERE'S CIPHER


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
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                "!", "?", "@", "#", "$", "%", "&", " ")

    for i in range(len(txt)):
        # Get a character from the text.
        char = txt[i]
        # Transforms the letter from the keyword in the offset number.
        offset = ord(key[i]) - 65

        # The character is a uppercase letter.
        if char.isupper:
            enc_txt += alphabet[(alphabet.index(char.lower()) + offset) % len(
                alphabet)].upper()

        # Character is anything else.
        else:
            enc_txt += alphabet[(alphabet.index(char) + offset) % len(alphabet)]

    return enc_txt


def cipher_decrypt(txt, kw):
    # Receives the encrypted text and the key to decrypt the text.

    dec_txt = ""
    key = key_generator(txt, kw)
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                "!", "?", "@", "#", "$", "%", "&", " ")

    for i in range(len(txt)):
        # Get a character from the text.
        char = txt[i]
        # Transforms the letter from the keyword in the offset number.
        offset = ord(key[i]) - 65

        # The character is a uppercase letter.
        if char.isupper:
            dec_txt += alphabet[(alphabet.index(char.lower()) - offset) % len(
                alphabet)].upper()

        # Character is anything else.
        else:
            dec_txt += alphabet[(alphabet.index(char) - offset) % len(
                alphabet)]

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
