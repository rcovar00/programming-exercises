def caesar_cipher(string, rotation):
    cipher_string = ''
    for s in string:
        if s == ' ':
            cipher_string += s
            continue
        cipher_string += chr(ord(s) + rotation)

    return cipher_string


print caesar_cipher("Attack me", 1)
print caesar_cipher("Fight", 5)
