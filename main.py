
from alphabet import letters
import art

def encrypt(message, shift):
    encrypted_msg = ""
    for i in message:
        if i in letters:
            updated = letters.index(i) + shift
            if updated >= 26:
                updated %= 26
            encrypted_msg += letters[updated]
        else:
            encrypted_msg += i
    print(f"Encrypted Text: {encrypted_msg}")
    
def decrypt(message, shift):
    decrypted_msg = ""
    for i in message:
        if i in letters:
            updated = letters.index(i) - shift
            if updated < 0:
                updated += 26
            decrypted_msg += letters[updated]
        else:
            encrypted_msg += i
    print(f"Decrypted Text: {decrypted_msg}")
        
print("===== WELCOME TO CIESER CIPHER =====\n")

print(f"{art.logo}")

action = input("Type \"ENCODE\" to Encrypt or \"DECODE\" to Decrypt\n").lower()
message = input("Type your message\n").lower()
shift = int(input("Type your shift number\n"))

if action == "encode":
    encrypt(message, shift)
elif action == "decode":
    decrypt(message, shift)
else:
    print("You have not put a valid input")
