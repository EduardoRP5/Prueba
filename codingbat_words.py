def word_multiple(strings):
    word_map = {}
    for w in strings:
        if w not in word_map:
            word_map[w] = False
        else:
            word_map[w] = True
    return word_map

# Datos Prueba
strings = ["platano", "platano", "manzana", "platano", "uva", "Sandia"]
Resultado = word_multiple(strings)

print(Resultado)