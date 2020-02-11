def cesar_encryption():
    # Read file
    txtFile = open('message.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    # Replace returns by spaces
    plain_text = ""
    for fc in fileContent:
        plain_text += fc.replace("\n", " ").upper()

    print("\n\n========== Plain text ==========\n\n", plain_text)

    # Alphabet
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
    # Scroll key
    key = int (input("\n---------- Cesar's key: "))
    
    if key > 0 and key <= 37:
        # Encrypted text variable
        encrypted_text = ""
        
        # Cesar encryption method
        for pt in plain_text:
            if pt in alphabet:
                    encrypted_text += alphabet[((alphabet.index(pt) + key) % (len(alphabet)))]
            else:
                if pt == " ":
                    encrypted_text += pt
                else:
                    encrypted_text += ""
        
        # Print encrypted text
        print("\n\n========== Text encrypted by cesar ==========\n\n",encrypted_text)

        # Create output file
        outputFile = open('message_encrypt.txt','w')
        outputFile.write(encrypted_text)
        outputFile.close() 
        print("\n\n========== Check message_encrypt.txt file ==========\n\n") 
        
    
    else:
        print("Key out of range")

def cesar_decryption():
    # Read file
    txtFile = open('message_encrypt.txt','r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    # Replace returns by spaces
    encrypted_text = ""
    for fc in fileContent:
        encrypted_text += fc.replace("\n", " ").upper()

    print("\n\n========== Encrypted text ==========\n\n", encrypted_text)

    # Alphabet
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
    
    # Scroll key
    key = int (input("\n---------- Cesar's key: "))

    if key > 0 and key <= 37:
        # Decrypted text variable
        decrypted_text = ""
        
        # Cesar Decrypt method
        for et in encrypted_text:
            if et in alphabet:
                    decrypted_text += alphabet[((alphabet.index(et) - key) % (len(alphabet)))]
            else:
                if et == " ":
                    decrypted_text += et
                else:
                    decrypted_text += ""

        print("\n\n========== Plain text decrypted ==========\n\n")
        print(decrypted_text)
        print("\n\n")
        
    else:
        print("Key out of range")


def main():
    
    option = int (input("\n\n========== Choose an option ==========\n1) Encrypt \n2) Decrypt\n\n"))

    if option == 1:
        cesar_encryption()
    elif option == 2:
        cesar_decryption()
    else:
        print("Incorrect option")

if __name__ == "__main__":
    main()