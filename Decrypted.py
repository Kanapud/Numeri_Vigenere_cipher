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

def load_key(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Load keys from files
key_x = load_key('key_x.txt')
key_y = load_key('key_y.txt')
key_z = load_key('key_z.txt')

# Read encrypted OBJ file
with open('Encrypted_Helmet.obj', 'r') as file:
    encrypted_lines = file.readlines()

# Decrypt vertices for x, y, and z axes
decrypted_lines = []
for line in encrypted_lines:
    if line.startswith('v '):
        parts = line.split()
        decrypted_x = vigenere_decipher(parts[1], key_x)
        decrypted_y = vigenere_decipher(parts[2], key_y)
        decrypted_z = vigenere_decipher(parts[3], key_z)
        decrypted_line = 'v ' + decrypted_x + ' ' + decrypted_y + ' ' + decrypted_z + '\n'
        decrypted_lines.append(decrypted_line)
    else:
        decrypted_lines.append(line)

# Save decrypted OBJ file
with open('Decrypted_Helmet.obj', 'w') as file:
    for decrypted_line in decrypted_lines:
        file.write(decrypted_line)
