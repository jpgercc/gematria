#Explicação/exemplo:
#286 seria decomposto como:
#300 (ש) não cabe, então tenta 200 (ר) → subtraímos 200.
#O que sobra é 86 → agora tenta 80 (פ) → subtraímos 80.
#O que sobra é 6 → agora tenta 6 (ו) → subtraímos 6.
#Logo, a representação será שרג.

# # Dicionário com os valores das letras hebraicas
gematria_values = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
    'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400,
    'ם': 600, 'ן': 700, 'ף': 800, 'ץ': 900  # Letras finais
}

def calcular_gematria(palavra):
    # Inicializa a soma
    valor_total = 0
    
    # Para cada letra na palavra, soma o valor correspondente
    for letra in palavra:
        if letra in gematria_values:
            valor_total += gematria_values[letra]
        else:
            print(f"Letra não reconhecida: {letra}")
    
    return valor_total

# Teste com a palavra "שלום" (Shalom)
palavra = "שלום"
valor_gematria = calcular_gematria(palavra)
print(f"O valor de Gematria para '{palavra}' é: {valor_gematria}")
