# Function to create a Caesar cipher
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Handle shifts greater than 26
            if char.islower():  # Handle lowercase letters
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:  # Handle uppercase letters
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char  # Keep non-alphabet characters unchanged
    return encrypted_text

# Function to decode a Caesar cipher
def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)  # Decoding is the same as encoding with a negative shift

# Example usage
original_text = input("message:")
shift_amount = int(input("shift amount:"))

# Encrypt the text
encrypted_text = caesar_cipher(original_text, shift_amount)
print("Encrypted Text:", encrypted_text)

# Decrypt the text
decrypted_text = caesar_decipher(encrypted_text, shift_amount)
print("Decrypted Text:", decrypted_text)
