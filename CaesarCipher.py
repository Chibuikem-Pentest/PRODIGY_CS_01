def caesar_cipher(msg, shift, mode):
    result = ""
    if mode.lower() == "decrypt":
        shift = -shift  # Reverse the shift for decryption
    
    for char in msg:
        if char.isalpha():  # Only process alphabetic characters
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char  # Non-alphabetic characters are added as is
    
    return result


# User interaction
while True:
    print("\nCaesar Cipher Tool")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")
    
    if choice == "1":
        message = input("Enter the message to encrypt: ")
        shift_value = int(input("Enter the shift value (e.g., 3): "))
        encrypted = caesar_cipher(message, shift_value, "encrypt")
        print("Encrypted Message:", encrypted)
    
    elif choice == "2":
        message = input("Enter the message to decrypt: ")
        shift_value = int(input("Enter the shift value (e.g., 3): "))
        decrypted = caesar_cipher(message, shift_value, "decrypt")
        print("Decrypted Message:", decrypted)
    
    elif choice == "3":
        print("Exiting the tool. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
