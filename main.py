alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = int(input("Digite '1' para encriptar ou '2' para desencriptar: "))
original_text = input("Escreva o texto que deseja encriptar: ")
shift_amount = int(input("Digite o número de deslocamentos: "))
size_alphabet = len(alphabet)
print("Bem vindo à CIFRA DE CÉSAR!")

def caesar(text, shift, encode_or_decode):
    text_encrypted = ""
    for letter in text:
        shifted_position = (alphabet.index(letter) + shift) % size_alphabet
        text_encrypted += alphabet[shifted_position]

    text_decrypted = ""
    for letter in text_encrypted:
        shifted_position = (alphabet.index(letter) - shift) % size_alphabet
        text_decrypted += alphabet[shifted_position]

    if encode_or_decode == 1:
        print(f"o texto encriptado é: {text_encrypted}")
    elif encode_or_decode == 2:
        print(f"o texto encriptado é: {text_encrypted}")
        print(f"o texto decriptado é: {text_decrypted}")
    else:
        print(f"insira um valor válido!") 

caesar(text=original_text, shift=shift_amount, encode_or_decode=direction)

