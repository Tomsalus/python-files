def generate_key(text, key):
    full_key = ""
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text)):
            full_key += (key[i % len(key)])

    return full_key


def vigenere_encrypt(text, key):
    key = generate_key(text, key)
    encrypted_text = ""
    for i in range(len(text)):
        if text[i] == " ":
            encrypted_text += (" ")
        else:
            x = (ord(text[i].upper()) + ord(key[i].upper())) % 26 + 65
            encrypted_text += chr(x)

    return encrypted_text


def vigenere_decrypt(text, key):
    key = generate_key(text, key)
    decrypted_text = ""
    for i in range(len(text)):
        if text[i] == " ":
            decrypted_text += (" ")
        else:
            x = (ord(text[i].upper()) - ord(key[i].upper())) % 26 + 65
            decrypted_text += chr(x)

    return decrypted_text


def main():
    assert vigenere_encrypt("", "abcd") == ""
    assert vigenere_encrypt(" ", "a") == " "
    assert vigenere_encrypt("abcde", "a") == "ABCDE"
    assert vigenere_encrypt("programming", "c") == "RTQITCOOKPI"
    assert vigenere_encrypt("python", "bcd") == "QAWIQQ"
    assert vigenere_encrypt("PYTHON", "PROGRAMMING") == "EPHNFN"
    assert vigenere_encrypt("Python is fun", "NO") == "CMGVBB WF SIA"
    assert vigenere_encrypt("I shall pass this course "
                            "because I love programming", "hopefully") \
        == "P HLFFW NHGH YBTD JCJVXY MCJOJWJ T JVJT ULZRPHABMSA"

    assert vigenere_decrypt("", "abcd") == ""
    assert vigenere_decrypt(" ", "a") == " "
    assert vigenere_decrypt("abcde", "a") == "ABCDE"
    assert vigenere_decrypt("RTQITCOOKPI", "C") == "PROGRAMMING"
    assert vigenere_decrypt("qawiqq", "bcd") == "PYTHON"
    assert vigenere_decrypt("EPHNFN", "programming") == "PYTHON"
    assert vigenere_decrypt("CMGVBB WF SIA", "no") == "PYTHON IS FUN"
    assert vigenere_decrypt("P HLFFW NHGH YBTD JCJVXY "
                            "MCJOJWJ T JVJT ULZRPHABMSA", "HOPEFULLY") \
        == "I SHALL PASS THIS COURSE BECAUSE I LOVE PROGRAMMING"


if __name__ == '__main__':
    main()