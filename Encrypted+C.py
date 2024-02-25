import numpy as np

# Vigenère Cipher function
def vigenere_cipher(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        key_char = key[i % key_length]
        if char.isdigit():
            encrypted_char = str((int(char) + int(key_char)) % 10)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

# Function to generate a key
def generate_key():
    return ''.join(str(np.random.randint(0, 9)) for _ in range(12))

# Function to save a key to a file
def save_key_to_file(key, filename):
    with open(filename, 'w') as file:
        file.write(key)

# Function to create a Caesar table (number table)
def create_caesar_table():
    table = np.arange(10)
    np.random.shuffle(table)
    return table

# Function to switch values in the table
def switch_values(table):
    np.random.shuffle(table)

# Function to swap values based on a table
def swap_values(value, table):
    for i, v in enumerate(table):
        if v == value:
            return table[(i + np.random.randint(1, len(table))) % len(table)]
    return value

# Function to encrypt coordinates using Vigenère Cipher and then apply Caesar Cipher
def encrypt_coordinates(coord, key, caesar_table):
    if '.' in coord:
        integer_part, decimal_part = coord.split('.')
        encrypted_integer_part = vigenere_cipher(integer_part, key)
        encrypted_decimal_part = ''.join(str(caesar_table[int(digit)]) for digit in decimal_part)
        encrypted_coord = encrypted_integer_part + '.' + encrypted_decimal_part
    else:
        encrypted_coord = vigenere_cipher(coord, key)
    return encrypted_coord

# Function to encrypt an OBJ file
def encrypt_obj_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    # Generate keys for x, y, and z axes
    key_x = generate_key()
    key_y = generate_key()
    key_z = generate_key()

    # Save keys to files
    save_key_to_file(key_x, 'key_x+C.txt')
    save_key_to_file(key_y, 'key_y+C.txt')
    save_key_to_file(key_z, 'key_z+C.txt')

    # Create a Caesar table (number table)
    caesar_table = create_caesar_table()

    # Shuffle Caesar table
    switch_values(caesar_table)

    # Save Caesar table to a file
    np.savetxt('caesar_table.txt', caesar_table, fmt='%d')

    # Encrypt vertices for x, y, and z axes using Vigenère and Caesar Ciphers
    encrypted_lines = []
    for line in lines:
        if line.startswith('v '):
            parts = line.split()
            encrypted_x = encrypt_coordinates(parts[1], key_x, caesar_table)
            encrypted_y = encrypt_coordinates(parts[2], key_y, caesar_table)
            encrypted_z = encrypt_coordinates(parts[3], key_z, caesar_table)
            encrypted_line = 'v ' + encrypted_x + ' ' + encrypted_y + ' ' + encrypted_z + '\n'
            encrypted_lines.append(encrypted_line)
        else:
            encrypted_lines.append(line)

    # Save encrypted OBJ file
    with open(output_filename, 'w') as file:
        for encrypted_line in encrypted_lines:
            file.write(encrypted_line)

    # Print keys for x, y, and z axes
    print("Key for x-axis:", key_x)
    print("Key for y-axis:", key_y)
    print("Key for z-axis:", key_z)

# Encrypt the OBJ file using both Vigenère and Caesar Ciphers
encrypt_obj_file('technosphere.obj', 'Encrypted_technosphere_C.obj')
