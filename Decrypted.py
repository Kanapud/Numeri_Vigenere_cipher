def vigenere_decipher(text, key):  # ฟังก์ชันสำหรับถอดรหัสข้อความด้วย Vigenère cipher
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(text):
        key_char = key[i % key_length]
        if char.isdigit():  # ตรวจสอบว่าเป็นตัวเลขหรือไม่
            decrypted_char = str((int(char) - int(key_char)) % 10)  # ถอดรหัสตัวเลข
        else:
            decrypted_char = char  # ไม่ถอดรหัสตัวอักษรอื่นๆ
        decrypted_text += decrypted_char
    return decrypted_text

def load_key(file_path):  # ฟังก์ชันสำหรับโหลดคีย์จากไฟล์
    with open(file_path, 'r') as file:
        return file.read().strip()

# Load keys from files
key_x = load_key('key_x.txt')  # โหลดคีย์สำหรับแกน x
key_y = load_key('key_y.txt')  # โหลดคีย์สำหรับแกน y
key_z = load_key('key_z.txt')  # โหลดคีย์สำหรับแกน z

# Read encrypted OBJ file
with open('Encrypted_Tree.obj', 'r') as file:  # อ่านไฟล์ OBJ ที่เข้ารหัสแล้ว
    encrypted_lines = file.readlines()

# Decrypt vertices for x, y, and z axes
decrypted_lines = []
for line in encrypted_lines:
    if line.startswith('v '):  # ตรวจสอบว่าเป็นบรรทัด vertex หรือไม่
        parts = line.split()
        decrypted_x = vigenere_decipher(parts[1], key_x)  # ถอดรหัสค่า x
        decrypted_y = vigenere_decipher(parts[2], key_y)  # ถอดรหัสค่า y
        decrypted_z = vigenere_decipher(parts[3], key_z)  # ถอดรหัสค่า z
        decrypted_line = 'v ' + decrypted_x + ' ' + decrypted_y + ' ' + decrypted_z + '\n'
        decrypted_lines.append(decrypted_line)
    else:
        decrypted_lines.append(line)

# Save decrypted OBJ file
with open('Decrypted_Tree.obj', 'w') as file:  # บันทึกไฟล์ OBJ ที่ถอดรหัสแล้ว
    for decrypted_line in decrypted_lines:
        file.write(decrypted_line)
