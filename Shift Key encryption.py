# Shift Key encryption and Decryption


while True:
    Encrypt_or_Decrypt = input("Encrypt or Decrypt: ")
    Encrypt_or_Decrypt = Encrypt_or_Decrypt.capitalize()
    if (Encrypt_or_Decrypt) == "Encrypt":
        Letter_to_Encrypt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                                "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                                "S", "T", "U", "V", "W", "X", "Y", "Z"]

        # User input
        to_Encrypt = input("What to encrypt: ")
        to_Encrypt = to_Encrypt.upper()
        shiftKey = int(input("Shift Key amount: "))

        # Functions
        totalEncrypted = []

        # Cipher Logic
        for char in to_Encrypt:
            if (Letter_to_Encrypt.__contains__(char)):
                charPos = Letter_to_Encrypt.index(char)
                Encrypted = shiftKey + int(charPos)
                Encryption = Letter_to_Encrypt[Encrypted]
                totalEncrypted.append(Encryption)
            elif (char.isnumeric()):
                number = int(char) + shiftKey
                totalEncrypted.append(number)

        # Result
        print(totalEncrypted)
        break

    print("\033[91mError:\033[0m encrypt or decrypt")