'''

Task-02      : Pixel Manipulation for Image Encryption
File Name    : Prasunet_CS_02
Organization : Prasunet Pvt.Ltd. Company

'''

import numpy as np                            #Importing Numpy library
from PIL import Image                         #Using Pillow library
from pathlib import Path                      #Using Pathlib library

def generate_random_sequence(key, size):
    # Seed the random number generator with the provided key
    np.random.seed(key)
    # Generate a random sequence of the given size with values between 0 and 255
    return np.random.randint(0, 256, size, dtype=np.uint8)

def xor_with_prng(image_array, key):
    # Flatten the image array to a 1D array
    flat_image_array = image_array.flatten()
    # Generate a random sequence based on the key and size of the image array
    random_sequence = generate_random_sequence(key, flat_image_array.size)
    # Perform XOR between the image array and the random sequence
    encrypted_decrypted_array = np.bitwise_xor(flat_image_array, random_sequence)
    # Reshape the 1D array back to the original image shape
    return encrypted_decrypted_array.reshape(image_array.shape)

def process_image(image_path, key, mode):
    try:
        # Open the image file
        image = Image.open(image_path)
        # Convert the image to a numpy array
        image_array = np.array(image, dtype=np.uint8)
        # Encrypt or decrypt the image using XOR with PRNG
        processed_array = xor_with_prng(image_array, key)
        # Convert the processed array back to an image
        processed_image = Image.fromarray(processed_array.astype('uint8'))
        return processed_image
    except FileNotFoundError:
        print(f"[Error!] File not found: {image_path}")
        return None
    except Exception as e:
        print(f"[Error!] An error occurred: {e}")
        return None

def save_image(image, original_path, suffix):
    try:
        # Create a Path object from the original image path
        path = Path(original_path)
        # Generate a new file name by adding the suffix
        new_stem = path.stem.replace("_encrypted", "").replace("_decrypted", "")
        new_path = path.with_name(f"{new_stem}_{suffix}.png")
        # Save the processed image to the new path
        image.save(new_path)
        return new_path
    except Exception as e:
        print(f"[Error!] An error occurred while saving the image: {e}")
        return None

def load_key(image_path):
    # Generate the key file path from the image path
    key_path = Path(image_path).with_suffix('.key')
    if key_path.exists():
        with open(key_path, 'r') as key_file:
            key = int(key_file.read())
            if 0 <= key <= 255:  # Ensure key is within uint8 range
                return key
            else:
                print(f"[Warning!] Invalid key loaded from file ({key}). Key must be in the range 0-255.")
    return None

def save_key(key, image_path):
    if 0 <= key <= 255:  # Ensure key is within uint8 range
        # Generate the key file path from the image path
        key_path = Path(image_path).with_suffix('.key')
        with open(key_path, 'w') as key_file:
            # Write the key to the file
            key_file.write(str(key))
    else:
        print(f"[Warning!] Invalid key provided ({key}). Key must be in the range 0-255.")

def main():
    print("\n********* Welcome to the Image Encryption and Decryption Tool *********\n")
    while True:
        print("\n--- New Operation ---")
        image_path = input("Enter the path to the image: ")
        if not image_path.lower().endswith('.png'):
            print("[Warning!] It's recommended to use PNG images for better encryption and decryption results.")
        
        try:
            key = int(input("Enter the key (0-255): "))
            if not 0 <= key <= 255:
                raise ValueError("Key must be in the range 0-255.")
        except ValueError as e:
            print(f"[Error!] Invalid key: {e}")
            continue

        choice = input("Do you want to encrypt or decrypt the image? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("[Error!] Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
            continue

        is_decrypt = choice == 'd'

        if is_decrypt:
            original_key = load_key(image_path)
            if original_key is None:
                print("[Warning!] No valid key found for this image. Cannot decrypt.")
                continue
            if key != original_key:
                print("[Warning!] The key does not match the original encryption key. Decryption aborted.")
                continue

        processed_image = process_image(image_path, key, choice)

        if processed_image:
            suffix = "encrypted" if choice == 'e' else "decrypted"
            processed_path = save_image(processed_image, image_path, suffix)
            if processed_path:
                print(f"\n[Success!] {suffix.capitalize()} image saved to {processed_path}")
                if choice == 'e':
                    save_key(key, processed_path)

        while True:
            repeat = input("Do you want to perform another operation? (y/n): ").lower()
            if repeat in ['y', 'n']:
                break
            else:
                print("[Error!] Invalid input. Please enter 'y' to continue or 'n' to exit.")
        
        if repeat != 'y':
            print("\nThank you for using the Image Encryption and Decryption Tool. Goodbye!")
            break

if __name__ == "__main__":
    main()
