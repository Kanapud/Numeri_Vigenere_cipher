import numpy as np

# Function to decrypt coordinates using Vigenère Cipher and then reverse Caesar Cipher
def decrypt_coordinates(coord, key, caesar_table):
    if '.' in coord:
        integer_part, decimal_part = coord.split('.')
        decrypted_integer_part = vigenere_decipher(integer_part, key)
        decrypted_decimal_part = ''.join(str(caesar_table.tolist().index(int(digit))) for digit in decimal_part)
        decrypted_coord = decrypted_integer_part + '.' + decrypted_decimal_part
    else:
        decrypted_coord = vigenere_decipher(coord, key)
    return decrypted_coord

# Function to decrypt an OBJ file
def decrypt_obj_file(input_filename, output_filename, caesar_table_x, caesar_table_y, caesar_table_z):
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    # Read keys from files
    with open('key_x+C.txt', 'r') as file:
        key_x = file.read().strip()
    with open('key_y+C.txt', 'r') as file:
        key_y = file.read().strip()
    with open('key_z+C.txt', 'r') as file:
        key_z = file.read().strip()

    # Decrypt vertices for x, y, and z axes using Vigenère and Caesar Ciphers
    decrypted_lines = []
    for line in lines:
        if line.startswith('v '):
            parts = line.split()
            decrypted_x = decrypt_coordinates(parts[1], key_x, caesar_table_x)
            decrypted_y = decrypt_coordinates(parts[2], key_y, caesar_table_y)
            decrypted_z = decrypt_coordinates(parts[3], key_z, caesar_table_z)
            decrypted_line = 'v ' + decrypted_x + ' ' + decrypted_y + ' ' + decrypted_z + '\n'
            decrypted_lines.append(decrypted_line)
        else:
            decrypted_lines.append(line)

    # Save decrypted OBJ file
    with open(output_filename, 'w') as file:
        for decrypted_line in decrypted_lines:
            file.write(decrypted_line)

# Function to decrypt using Vigenère Cipher
def vigenere_decipher(text, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        key_char = key[i % key_length]
        if char.isdigit():
            decrypted_char = str((int(char) - int(key_char)) % 10)
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

# Decrypt the encrypted OBJ file
caesar_table_x = np.loadtxt('caesar_table.txt', dtype=int)
caesar_table_y = np.loadtxt('caesar_table.txt', dtype=int)
caesar_table_z = np.loadtxt('caesar_table.txt', dtype=int)
decrypt_obj_file('Encrypted_technosphere_C.obj', 'Decrypted_technosphere_C.obj', caesar_table_x, caesar_table_y, caesar_table_z)
