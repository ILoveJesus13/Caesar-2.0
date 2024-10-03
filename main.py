secret_message = "Hello World 123"
number =  36

def caesar_cipher(text: str, shift: int):
    result = ""
    
    for char in text:
        if char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.isnumeric():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        else:
            result += char

    return result


  

def caesar_decipher(secret_message, shift):
    result = ""
    
    for char in secret_message:
        if char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.isnumeric():
            result += chr((ord(char) - shift - 48) % 10 + 48)
        else:
            result += char

    return result

hidden_message = caesar_cipher(secret_message, number)
deciphered = caesar_decipher(hidden_message, number)
print(hidden_message)
print(deciphered)