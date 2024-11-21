alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Bem vindo à CIFRA DE CÉSAR!")

def caesar(text, shift, encode_or_decode):
    text_encrypted = ""
    non_alpha_chars = ""

    for letter in text:
        if letter in alphabet:
            original_index = alphabet.index(letter)
            if encode_or_decode == 1:
                shifted_position = (original_index + shift) % size_alphabet
            elif encode_or_decode ==2:
                shifted_position = (original_index - shift) % size_alphabet
            text_encrypted += alphabet[shifted_position]
        else:
            non_alpha_chars += letter

    text_encrypted += non_alpha_chars

    if encode_or_decode == 1:
        print(f"O texto encriptado é: {text_encrypted}")
    elif encode_or_decode == 2:
        print(f"O texto decriptado é: {text_encrypted}")
    else:
        print("Insira um valor válido!")

should_continue = True

while should_continue:
    direction = int(input("Digite '1' para encriptar ou '2' para desencriptar: "))
    original_text = input("Escreva o texto que deseja encriptar/decriptar: ")
    shift_amount = int(input("Digite o número de deslocamentos: "))
    size_alphabet = len(alphabet)

    caesar(text=original_text, shift=shift_amount, encode_or_decode=direction)

    restart = input("Digite 'sair' se quiser parar: ").lower()

    if restart == "sair":
        should_continue = False
        print("Obrigado e até mais!")

