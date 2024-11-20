alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

original_text = input("Escreva o texto que deseja encriptar: ")
shift_amount = int(input("Digite o número de deslocamentos: "))
size_alphabet = len(alphabet)
print("Bem vindo à CIFRA DE CÉSAR!")

def encrypt(text, shift):
    text_encypted = ""
    for letter in text:
        shifted_position = (alphabet.index(letter) + shift) % size_alphabet
        text_encypted += alphabet[shifted_position]

    return print(text_encypted)

encrypt(text=original_text, shift=shift_amount)
