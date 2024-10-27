import random
import string


def gerar_senha(tamanho=12, apenas_numeros=False):
    if apenas_numeros:
        caracteres = string.digits
    else:
        caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def main():
    print("Gerador de Senhas")
    tamanho = int(input("Digite o tamanho da senha (padrão: 12): ") or 12)
    apenas_numeros = input("Gerar senha com apenas números? (s/n): ").lower() == 's'
    senha = gerar_senha(tamanho, apenas_numeros)
    print(f"Sua senha gerada é: {senha}")

    salvar_arquivo = input("Salvar senha em um arquivo? (s/n): ").lower() == 's'
    if salvar_arquivo:
        with open("senhas.txt", "a") as arquivo:
            arquivo.write(senha + "\n")
        print("Senha salva com sucesso!")


if __name__ == "__main__":
    main()
