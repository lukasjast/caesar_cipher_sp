import string

def coder_decoder(message, shift, command):
    alphabet = list(string.ascii_lowercase)
    new_message = ""
    for letter in message:
        if letter == " ":
            new_message += " "
        elif letter.isdigit():
            new_message += letter
        else: 
            index = alphabet.index(letter)
            if command == "decode":
                new_index = (index - shift) % len(alphabet)
            elif command == "encode":
                new_index = (index + shift) % len(alphabet)
            new_message += alphabet[new_index] #asdasdasd
    return new_message

def main():
    print("Welcome to the Caesar cipher!")
    while True:
        command = input("Enter command (encode/decode) or 'exit' to quit: ")
        if command.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break
        elif command.lower() not in ["encode", "decode"]:
            print("Invalid command. Please enter 'encode', 'decode', or 'exit'.")
            continue
        message = input(f"Enter your message to {command}: ")
        shift = int(input("Enter the shift number: "))
        result = coder_decoder(message.lower(), shift, command)
        print(f"\nYour {command}d message is: {result}\n")

if __name__ == "__main__":
    main()