'''

Task-01      : Caesar Cipher Implementation
File Name    : Prasunet_CS_01
Organization : Prasunet Pvt.Ltd. Company

'''

#Function to perform Caesar Cipher encryption or decryption.
def caesar_cipher(text, shift, mode):
  
    result = ""                                            #An empty variable to store the encrypted or decrypted text messsage.
    shift = shift if mode == 'encrypt' else -shift         #Performs encryption or decryption based on the mode value.

    for char in text:
        if char.isalpha():                                 #Checks the character is alphabet.
            if char.isupper():                             #Checks the character is uppercase alphabet returns 65 otherwise 95.
               shift_amount = 65    
            else:
               shift_amount = 97    
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)                #The Cipher operation is performed and stored in result.
        else:
            result += char                                                                       #Non-alphabetic characters(Numbers, Special symbols) stored if it is not an aiphabet.

    return result

def main():
    while True:
        #--------User Menu-------
        print("\nCaesar Cipher - Encryption and Decryption")
        your_choice = input("Type 'E' for Encryption or Type 'D' for Decryption: ").lower()           #User input for Encryption or Decryption.

        if your_choice not in ['e', 'd']:                                                             #Displays Warning, if input is invalid.
            print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")          
            continue

        your_message = input("Enter your message: ")                                                  #User input for desired message.
        
        #--------Exception Handling---------
        try:
            shift = int(input("Enter the shift value (1-26): "))                                      #User input for character shift value.
            if shift < 1 or shift > 26:                                                               #Determines the shift value is entered within the limit range.
                print("Invalid shift value. Please enter a number between 1 and 26.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value between 1 and 26.")
            continue

        mode = 'encrypt' if your_choice == 'e' else 'decrypt' 
        processed_message = caesar_cipher(your_message, shift, mode)                                   #Defined function is called.
        print(f"{'Encrypted' if mode == 'encrypt' else 'Decrypted'} message: {processed_message}\n")   #Displays the final output with respectice choice.  
        
        #---------End prompt---------
        while True:
            do_again = input("Do you wish to continue or exit? Type 'Y' to continue otherwise type 'N': ").lower()
            if do_again == 'y':
                break
            elif do_again == 'n':
                print("\nExiting the program.")
                return
            else:
                print("Invalid input. Please type 'Y' to continue or 'N' to exit.\n")

if __name__ == "__main__":
    main()
