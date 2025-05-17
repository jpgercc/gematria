# -*- coding: utf-8 -*-
"""Gematria CLI - Converte número em letras hebraicas."""

gematria = {
    'ת': 400, 'ש': 300, 'ר': 200, 'ק': 100,
    'צ': 90, 'פ': 80, 'ע': 70, 'ס': 60, 'נ': 50, 'מ': 40,
    'ל': 30, 'כ': 20, 'י': 10, 'ט': 9, 'ח': 8, 'ז': 7, 'ו': 6,
    'ה': 5, 'ד': 4, 'ג': 3, 'ב': 2, 'א': 1
}

# Ordena os valores do maior para o menor
valores_ordenados = sorted(gematria.items(), key=lambda x: x[1], reverse=True)

def converter_para_gematria(numero):
    resultado = []
    restante = numero

    for letra, valor in valores_ordenados:
        while restante >= valor:
            resultado.append(letra)
            restante -= valor

    return ''.join(resultado)

# Loop CLI
if __name__ == "__main__":
    print("=== Gematria Hebraica ===")
    print("Digite um número inteiro positivo para ver sua gematria.\nDigite 'sair' para encerrar.\n")

    while True:
        entrada = input("Número: ").strip()

        if entrada.lower() == 'sair':
            print("Encerrando...")
            break

        if not entrada.isdigit():
            print("Por favor, insira um número válido.")
            continue

        numero = int(entrada)
        if numero <= 0:
            print("Por favor, insira um número maior que zero.")
            continue

        gematria_resultado = converter_para_gematria(numero)
        print(f"Gematria: {gematria_resultado}\n")
