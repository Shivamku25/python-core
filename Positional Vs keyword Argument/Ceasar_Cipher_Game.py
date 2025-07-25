alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
text = input("type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter  # keep spaces and punctuation unchanged
    print(f"Here is the encoded result: {cipher_text}")

encrypt(original_text=text, shift_amount=shift)