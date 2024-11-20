alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

original_text = input("Escreva o texto que deseja encriptar: ")
shift_amount = int(input("Digite o número de deslocamentos: "))
size_alphabet = len(alphabet)
print("Bem vindo à CIFRA DE CÉSAR!")

def encrypt(text, shift):
    text_encrypted = ""
    for letter in text:
        shifted_position = (alphabet.index(letter) + shift) % size_alphabet
        text_encrypted += alphabet[shifted_position]

    return text_encrypted

print(f" texto encriptado: {encrypt(text=original_text, shift=shift_amount)}")

def decrypt(text, shift):
    text_decrypted = ""
    for letter in text:
        shifted_position = (alphabet.index(letter) - shift) % size_alphabet
        text_decrypted += alphabet[shifted_position]

    return text_decrypted

print(f" texto decriptado: {decrypt(text=encrypt(text=original_text, shift=shift_amount), shift=shift_amount)}")

