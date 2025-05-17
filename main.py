#o código está um ****, não faz muito sentido, mas, espero que seja util, foi o GPT que fez então culpe ele qualquer coisa, minha unica culpa é ser vagabundo.

# -*- coding: utf-8 -*-
"""Calcula a Gematria de um número usando métodos guloso e tradicional."""

gematria = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
    'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
}

gematria_ordenada = sorted(gematria.items(), key=lambda item: item[1], reverse=True)

mapa_tradicional = {
    86: {'palavra': 'אלהים', 'frase': 'אהבה'},

    102: {'palavra': '', 'frase': 'ה\' רועי לא אחסר'},  # Hashem Ro'i Lo Echsar (O Senhor é o meu pastor, nada me faltará) - Salmo 23:1
    103: {'palavra': '', 'frase': 'ברוך אתה ה\' אלוקינו מלך העולם'},  # Baruch Atah Hashem Elokeinu Melech Haolam (Bendito és Tu, Senhor, nosso Deus, Rei do mundo) - Bênção judaica
    104: {'palavra': '', 'frase': 'לך אלוהים'},   # Lecha Elohim (A Ti, ó Deus) - Salmo 118:28
    105: {'palavra': '', 'frase': 'עוז ושלום אל תסור מאתנו'},  # Oz V\'Shalom Al Tasu Me\'itanu (Força e paz, não se afastem de nós) - Salmo 29:11
    106: {'palavra': '', 'frase': 'תן לנו שלום'},  # Ten Lanu Shalom (Dá-nos paz) - Salmo 122:6
    107: {'palavra': '', 'frase': 'כי תורתך'},  # Ki Toratecha (Porque tua Lei) - Salmo 119:1
    108: {'palavra': '', 'frase': 'חסד אל כל היום'},  # Chesed El Kol Hayom (A misericórdia de Deus é para sempre) - Salmo 136:1
    109: {'palavra': '', 'frase': 'ישמחו כל המחפשים את ה\''},  # Yismachu Kol Mechapsim Et Hashem (Se alegrem todos que buscam ao Senhor) - Salmo 105:3
    110: {'palavra': '', 'frase': 'ברוך הבא בשם ה\''},  # Baruch Haba B\'Shem Hashem (Bendito o que vem em nome do Senhor) - Salmo 118:26
    111: {'palavra': '', 'frase': 'חסד ורחמים'},  # Chesed U\'Rachamim (Misericórdia e compaixão) - Jeremias 31:3
    112: {'palavra': '', 'frase': 'תודה לה\' כי טוב'},  # Toda Le\'Hashem Ki Tov (Dai graças ao Senhor porque Ele é bom) - Salmo 136:1
    120: {'palavra': '', 'frase': 'תן לנו חיים'},  # Ten Lanu Chaim (Dá-nos vida) - Salmo 42:2
    130: {'palavra': '', 'frase': 'חסד אל עולם'},  # Chesed El Olam (A misericórdia de Deus é eterna) - Salmo 136:1
    150: {'palavra': '', 'frase': 'הודו לה\' כי טוב'},  # Hodu LeHashem Ki Tov (Dai graças ao Senhor porque Ele é bom) - Salmo 107:1
    160: {'palavra': '', 'frase': 'המשיח יבוא'},  # HaMashiach Yavo (O Messias virá)
    200: {'palavra': '', 'frase': 'פנים אל פנים'},  # Panim El Panim (Face a face) - Deuteronômio 5:4
    220: {'palavra': '', 'frase': 'אור חדש על ציון תאיר'},  # Or Chadash Al Tzion Tair (Uma nova luz brilhará sobre Sião) - Isaías 60:1
    230: {'palavra': '', 'frase': 'כל הנשמה תהלל י-ה'},  # Kol Haneshama Tehalel Yah (Toda alma louvará o Senhor) - Salmo 150:6
    240: {'palavra': '', 'frase': 'תפילה לב'},  # Tefilah LeLev (Oração do coração)
    300: {'palavra': '', 'frase': 'קדושה עליונה'},  # Kedushah Elyonah (Santidade suprema)
    340: {'palavra': '', 'frase': 'ברוך בואך בשם ה\''},  # Baruch Bo\'ach B\'Shem Hashem (Bendito o que vem em nome do Senhor)
    360: {'palavra': '', 'frase': 'אבן מאסו הבונים'},  # Even Masu Habanim (A pedra rejeitada pelos construtores) - Salmo 118:22
    400: {'palavra': '', 'frase': 'האמת מאירה'},  # HaEmet Me\'irah (A verdade brilha) - Isaías 45:8
    450: {'palavra': '', 'frase': 'אור של אמת'},  # Or Shel Emet (Luz da verdade)
    500: {'palavra': '', 'frase': 'רפואה שלמה'},  # Refuah Shlema (Cura completa)
    600: {'palavra': '', 'frase': 'תורה ציון ואמונה'},  # Torah Tzion V\'Emunah (Lei, Sião e Fé)
    700: {'palavra': '', 'frase': 'השלום יגיע'},  # HaShalom Yagia (A paz virá) - Isaías 57:19
    800: {'palavra': '', 'frase': 'חיים חדשים'},  # Chaim Chadashim (Vida nova)
    800: {'palavra': 'ן', 'frase': 'תחייה'} # Seu identificador adicionado AQUI nas frases também
}

mapa_tradicional_frases = {
    101: {'palavra': '', 'frase': 'אהבתך לא תחדל'},
        42: {'palavra': 'הכ', 'frase': 'Um exemplo adicional'},
    10: {'palavra': 'י', 'frase': 'Yod'},
    18: {'palavra': 'חיים', 'frase': 'Vida'},
    37: {'palavra': 'לב', 'frase': 'Coração'},
    26: {'palavra': 'כי', 'frase': 'Sim'},
    300: {'palavra': 'ש', 'frase': 'Shin'},
    400: {'palavra': 'ת', 'frase': 'Tav'},
    12: {'palavra': 'ל', 'frase': 'Lamed'},
    70: {'palavra': 'ע', 'frase': 'Ayin'},
    200: {'palavra': 'ר', 'frase': 'Resh'},
    50: {'palavra': 'נ', 'frase': 'Nun'},
    90: {'palavra': 'צ', 'frase': 'Tsade'},
    72: {'palavra': 'פ', 'frase': 'Pe'},
    34: {'palavra': 'ד', 'frase': 'Dalet'},
    60: {'palavra': 'ס', 'frase': 'Samekh'},
    100: {'palavra': 'ק', 'frase': 'Qof'},
    5: {'palavra': 'ה', 'frase': 'Hei'},
    80: {'palavra': 'כ', 'frase': 'Kaf'},
    14: {'palavra': 'מ', 'frase': 'Mem'},
    500: {'palavra': 'ך', 'frase': 'Final Kaf (Kaf Sofit)'},
    700: {'palavra': 'ם', 'frase': 'Final Mem (Mem Sofit)'},
    900: {'palavra': 'ף', 'frase': 'Final Pe (Pe Sofit)'},
    1000: {'palavra': 'ץ', 'frase': 'Final Tsade (Tsade Sofit)'},
    1: {'palavra': 'בראשית', 'frase': 'No princípio'},
    2: {'palavra': 'תורה', 'frase': 'Torah (Lei)'},
    3: {'palavra': 'שלום', 'frase': 'Shalom (Paz)'},
    4: {'palavra': 'אהבה', 'frase': 'Ahavah (Amor)'},
    19: {'palavra': 'אלוהים', 'frase': 'Elohim (Deus)'},
    7: {'palavra': 'אדון', 'frase': 'Adon (Senhor)'},
    11: {'palavra': 'צדק', 'frase': 'Tzedek (Justiça)'},
    13: {'palavra': 'ברית', 'frase': 'Brit (Aliança)'},
    17: {'palavra': 'קדוש', 'frase': 'Kadosh (Santo)'},
    21: {'palavra': 'תפילה', 'frase': 'Tefilah (Oração)'},
    25: {'palavra': 'חסד', 'frase': 'Chesed (Misericórdia)'},
    27: {'palavra': 'כבוד', 'frase': 'Kavod (Glória)'},
    29: {'palavra': 'משיח', 'frase': 'Mashiach (Messias)'},
    31: {'palavra': 'ברוך', 'frase': 'Baruch (Bendito)'},
    32: {'palavra': 'בני ישראל', 'frase': 'Bnei Yisrael (Filhos de Israel)'},
    33: {'palavra': 'השם', 'frase': 'Hashem (O Nome - uma forma de se referir a Deus)'},
    40: {'palavra': 'האנשים', 'frase': 'Ha\'anashim (As pessoas)'},
    45: {'palavra': 'תשובה', 'frase': 'Teshuvah (Arrependimento)'},
    50: {'palavra': 'יהוה', 'frase': 'YHWH (O nome sagrado de Deus)'},
    55: {'palavra': 'עבד', 'frase': 'Eved (Servo)'},
    56: {'palavra': 'אמת', 'frase': 'Emeth (Verdade)'},
    58: {'palavra': 'חיים', 'frase': 'Vida'},
    59: {'palavra': 'ברוך הבא', 'frase': 'Baruch Haba (Bem-vindo)'},
    60: {'palavra': 'רפואה', 'frase': 'Refuah (Cura)'},
    111: {'palavra': 'אור', 'frase': 'Or (Luz)'},
    150: {'palavra': 'רוח', 'frase': 'Ruach (Espírito)'},
    123: {'palavra': 'שפע', 'frase': 'Shefa (Abundância)'},
    212: {'palavra': 'חסד', 'frase': 'Chesed (Misericórdia)'},
    300: {'palavra': 'נפש', 'frase': 'Nefesh (Alma)'},
    170: {'palavra': 'מקדש', 'frase': 'Mikdash (Santuário)'},
    305: {'palavra': 'תפארת', 'frase': 'Tiferet (Beleza, Harmonia)'},
    400: {'palavra': 'ברכה', 'frase': 'Berachah (Bênção)'},
    500: {'palavra': 'שלום', 'frase': 'Shalom (Paz)'},
    666: {'palavra': 'תשובה', 'frase': 'Teshuvah (Arrependimento)'},
    800: {'palavra': 'תחייה', 'frase': 'Ressurreição'}, # Seu identificador aqui
    900: {'palavra': 'תכלית', 'frase': 'Propósito'},
    550: {'palavra': 'צדקה', 'frase': 'Tzedakah (Caridade)'},
    720: {'palavra': 'מצוות', 'frase': 'Mitzvot (Mandamentos)'},
    350: {'palavra': 'תורה', 'frase': 'Torah (Lei)'},
    530: {'palavra': 'קדושה', 'frase': 'Kedushah (Santidade)'},
    625: {'palavra': 'ברית', 'frase': 'Brit (Aliança)'},
    340: {'palavra': 'הבנה', 'frase': 'Havanah (Compreensão)'},
    900: {'palavra': 'הכנה', 'frase': 'Hakhana (Preparação)'},
    710: {'palavra': 'הצלחה', 'frase': 'Hatzlachah (Sucesso)'},
    360: {'palavra': 'השתהות', 'frase': 'Heshtahut (Paciência)'}
}

def calcular_valor(texto: str) -> int:
    """Calcula o valor gemátrico de um texto."""
    return sum(gematria.get(letra, 0) for letra in texto)

def metodo_guloso(numero: int) -> str:
    """Decompõe um número em letras hebraicas pelo método guloso."""
    letras = []
    calculo = []
    restante = numero
    for letra, valor in gematria_ordenada:
        while restante >= valor:
            letras.append(letra)
            calculo.append(f"{letra}:{valor}")
            restante -= valor
    calculo_formatado = " + ".join(calculo)
    return f"{''.join(letras)} ({calculo_formatado})" if restante == 0 else "Valor inválido após decomposição"

def metodo_tradicional(numero: int) -> str:
    """Retorna a palavra e frase hebraica associada a um número."""
    if numero in mapa_tradicional:
        resultado = mapa_tradicional[numero]
        palavra = resultado['palavra']
        frase = resultado['frase']
        valor_palavra = calcular_valor(palavra)
        valor_frase = calcular_valor(frase)
        return f"Palavra: {palavra} (Valor: {valor_palavra}), Frase: {frase} (Valor: {valor_frase})"
    elif numero in mapa_tradicional_frases:
        resultado = mapa_tradicional_frases[numero]
        palavra = resultado.get('palavra', '')
        frase = resultado.get('frase', '')
        valor_palavra = calcular_valor(palavra) if palavra else 0
        valor_frase = calcular_valor(frase) if frase else 0
        palavra_info = f"Palavra: {palavra} (Valor: {valor_palavra})" if palavra else "Palavra: Nenhuma"
        frase_info = f"Frase: {frase} (Valor: {valor_frase})" if frase else "Frase: Nenhuma"
        return f"{palavra_info}, {frase_info}"
    return "Não há mapeamento tradicional para esse número."

def calcular_gematria_completa(numero: int) -> str:
    """Calcula e retorna os resultados dos métodos guloso e tradicional."""
    resultado_guloso = metodo_guloso(numero)
    resultado_tradicional = metodo_tradicional(numero)
    return f"Calculando para {numero}:\nMétodo Guloso: {resultado_guloso}\nMétodo Tradicional: {resultado_tradicional}"

def entrada_usuario():
    """Interface de linha de comando para o calculador de Gematria."""
    print("Bem-vindo ao calculador de Gematria!")
    while True:
        try:
            entrada = input("Digite um número ('sair' para encerrar): ")
            if entrada.lower() == 'sair':
                print("Encerrando.")
                break
            numero = int(entrada)
            print(calcular_gematria_completa(numero))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'sair'.")
        except KeyboardInterrupt:
            print("\nEncerrando.")
            break

if __name__ == "__main__":
    entrada_usuario()
