# Import logo art from separate module (art.py should be present in the same directory)
import art
print(art.logo)

# Define the English alphabet for Caesar cipher
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(original_text, shift_amount, encode_or_decode):
    """
    Encrypts or decrypts a message using the Caesar cipher algorithm.

    Parameters:
    - original_text (str): The input text to encode or decode.
    - shift_amount (int): The number of positions to shift the letters.
    - encode_or_decode (str): 'encode' for encryption, 'decode' for decryption.

    Prints:
    - The encoded or decoded result.
    """
    output_text = ""
    # Reverse shift if decoding
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        # Preserve non-alphabet characters (e.g., space, numbers, punctuation)
        if letter not in alphabet:
            output_text += letter
        else:
            # Shift letter by shift_amount within the alphabet
            shifted_position = alphabet.index(letter) + shift_amount
            # Handle wrap-around for alphabet boundaries
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Main program loop
should_continue = True

while should_continue:
    # User chooses mode: encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # User enters the message to be processed
    text = input("Type your message:\n").lower()
    # User sets the shift amount
    shift = int(input("Type the shift number:\n"))

    # Perform Caesar cipher operation
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask user if they want to continue
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
