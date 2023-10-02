numbers = {
    "treinta": 30,
    "cuarenta": 40,
    "cincuenta": 50,
    "sesenta": 60,
    "setenta": 70,
    "ochenta": 80,
    "noventa": 90,
    "cien": 100,
    "doscientos": 200,
    "trescientos": 300,
    "cuatrocientos": 400,
    "quinientos": 500,
    "seiscientos": 600,
    "setecientos": 700,
    "ochocientos": 800,
    "novecientos": 900
}

units = {
    "cero": 0,
    "uno": 1,
    "dos": 2,
    "tres": 3,
    "cuatro": 4,
    "cinco": 5,
    "seis": 6,
    "siete": 7,
    "ocho": 8,
    "nueve": 9,
    "diez": 10,
    "once": 11,
    "doce": 12,
    "trece": 13,
    "catorce": 14,
    "quince": 15,
    "dieciséis": 16,
    "diecisiete": 17,
    "dieciocho": 18,
    "diecinueve": 19,
    "veinte": 20,
    "veintiuno" : 21,
    "veintidos" : 22,
    "veintitres" : 23,
    "veinticuatro" : 24,
    "veinticinco" : 25,
    "veintiseis" : 26,
    "veintisiete" : 27,
    "veintiocho" : 28,
    "veintinueve" : 29,
}

quantifiers = {
    "mil": 1000,
    "millón": 1000000,
    "millones": 1000000
}

def words2num(string):
    out_string = ""
    words = string.lower().split()
    current_numb = None
    total_num = 0

    for i, word in enumerate(words):
        if word in quantifiers:
            if current_numb is not None:
                total_num += current_numb * quantifiers[word]
            else:
                total_num = quantifiers[word]
            current_numb = 0
        elif word in numbers:
            if current_numb is not None:
                current_numb += numbers[word]
            else:
                current_numb = numbers[word]
        elif word in units:
            if current_numb is not None:
                current_numb += units[word]
            else:
                current_numb = units[word]

            if i + 1 < len(words):
                if words[i + 1] not in quantifiers:
                    total_num += current_numb
                    out_string += str(total_num) + " "
                    total_num = 0
                    current_numb = None
            

        elif word == 'y':
            continue
        else:
            if current_numb is not None:
                total_num += current_numb
                out_string += str(total_num) + " "
                total_num = 0
                current_numb = None
            out_string += word + " "
        
    if current_numb is not None:
        total_num += current_numb
        out_string += str(total_num) + " "
        total_num = 0
        current_numb = None

    return out_string
