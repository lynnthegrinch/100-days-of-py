alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceasar(text, shift, direction):
    coded = ""
    for i in text:
        if direction == 'encode':
           if i in alphabet:
               position = alphabet.index(i)
               n_position = position + shift
               coded += alphabet[n_position] 
           else:
               coded += i

        elif direction == 'decode':
            if i != " ":
                position = alphabet.index(i)
                n_position = position - shift
                coded += alphabet[n_position]
            elif i == " ":
                coded += " "
    print(f"your text is {coded}")
print("welcome to my ceasar encoder and decoder")
play = True
while play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar(text, shift, direction)
    play = input("wanna play again? yes or no\n")
    if play == 'no':
        print("goodbye")
        play = False
