import numpy as np

# Function to encrypt text using the Vigenère cipher
def vigenere_cipher(text, key):  # ฟังก์ชันสำหรับเข้ารหัสข้อความด้วย Vigenère cipher
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        key_char = key[i % key_length]
        if char.isdigit():  # ตรวจสอบว่าเป็นตัวเลขหรือไม่
            encrypted_char = str((int(char) + int(key_char)) % 10)  # เข้ารหัสตัวเลข
        else:
            encrypted_char = char  # ไม่เข้ารหัสตัวอักษรอื่นๆ
        encrypted_text += encrypted_char
    return encrypted_text

# Function to generate a random key with 12 digits
def generate_key():  # ฟังก์ชันสำหรับสร้างคีย์แบบสุ่มที่มีตัวเลข 12 ตัว
    return ''.join(str(np.random.randint(0, 10)) for _ in range(12))

# Function to save a key to a file
def save_key_to_file(key, filename):  # ฟังก์ชันสำหรับบันทึกคีย์ลงไฟล์
    with open(filename, 'w') as file:
        file.write(key)

# Read the OBJ file
with open('Tree.obj', 'r') as file:  # อ่านไฟล์ OBJ ชื่อ "Tree.obj"
    lines = file.readlines()

# Generate keys for x, y, and z axes
key_x = generate_key()  # สร้างคีย์สำหรับแกน x
key_y = generate_key()  # สร้างคีย์สำหรับแกน y
key_z = generate_key()  # สร้างคีย์สำหรับแกน z

# Save keys to files
save_key_to_file(key_x, 'key_x.txt')  # บันทึกคีย์ x ลงไฟล์ "key_x.txt"
save_key_to_file(key_y, 'key_y.txt')  # บันทึกคีย์ y ลงไฟล์ "key_y.txt"
save_key_to_file(key_z, 'key_z.txt')  # บันทึกคีย์ z ลงไฟล์ "key_z.txt"

# Encrypt vertices for x, y, and z axes
encrypted_lines = []
for line in lines:
    if line.startswith('v '):  # ตรวจสอบว่าเป็นบรรทัด vertex หรือไม่
        parts = line.split()
        encrypted_x = vigenere_cipher(parts[1], key_x)  # เข้ารหัสค่า x
        encrypted_y = vigenere_cipher(parts[2], key_y)  # เข้ารหัสค่า y
        encrypted_z = vigenere_cipher(parts[3], key_z)  # เข้ารหัสค่า z
        encrypted_line = 'v ' + encrypted_x + ' ' + encrypted_y + ' ' + encrypted_z + '\n'
        encrypted_lines.append(encrypted_line)
    else:
        encrypted_lines.append(line)

# Save encrypted OBJ file
with open('Encrypted_Tree.obj', 'w') as file:  # บันทึกไฟล์ OBJ ที่เข้ารหัสแล้ว
    for encrypted_line in encrypted_lines:
        file.write(encrypted_line)

# Print keys for x, y, and z axes
print("Key for x-axis:", key_x)  # แสดงคีย์สำหรับแกน x
print("Key for y-axis:", key_y)  # แสดงคีย์สำหรับแกน y
print("Key for z-axis:", key_z)  # แสดงคีย์สำหรับแกน z
