import numpy as np

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

def generate_key():
    return ''.join(str(np.random.randint(0, 10)) for _ in range(12))  # Generate key with 12 characters

def save_key_to_file(key, filename):
    with open(filename, 'w') as file:
        file.write(key)

# Read OBJ file
with open('technosphere.obj', 'r') as file:
    lines = file.readlines()

# Generate keys for x, y, and z axes
key_x = generate_key()
key_y = generate_key()
key_z = generate_key()

# Save keys to files
save_key_to_file(key_x, 'key_x.txt')
save_key_to_file(key_y, 'key_y.txt')
save_key_to_file(key_z, 'key_z.txt')

# Encrypt vertices for x, y, and z axes
encrypted_lines = []
for line in lines:
    if line.startswith('v '):
        parts = line.split()
        encrypted_x = vigenere_cipher(parts[1], key_x)
        encrypted_y = vigenere_cipher(parts[2], key_y)
        encrypted_z = vigenere_cipher(parts[3], key_z)
        encrypted_line = 'v ' + encrypted_x + ' ' + encrypted_y + ' ' + encrypted_z + '\n'
        encrypted_lines.append(encrypted_line)
    else:
        encrypted_lines.append(line)

# Save encrypted OBJ file
with open('Encrypted_technosphere.obj', 'w') as file:
    for encrypted_line in encrypted_lines:
        file.write(encrypted_line)

# Print keys for x, y, and z axes
print("Key for x-axis:", key_x)
print("Key for y-axis:", key_y)
print("Key for z-axis:", key_z)
