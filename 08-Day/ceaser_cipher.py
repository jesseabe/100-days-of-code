alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z'
]



def ceaser(original_text, shift_amount, encode_or_decode):
    
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text +=letter

        else:
            shift_position = alphabet.index(letter) + shift_amount
            shift_position = shift_position % len(alphabet)
            output_text += alphabet[shift_position]
    print(f"Here is the {direction}d result {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypts, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type you message:\n").lower()
        shift = int(input("Type the shift nunber:\n"))

        ceaser(text, shift, direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart == 'no':
            should_continue = False
            print("Goodbye")
    else:
        should_continue = False
        print("You need to choose between 'encode' or 'decode'")