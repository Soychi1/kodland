meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado"
}


print("¡Bienvenido a la aplicación de diccionario de memes!")
print("Por favor, introduce palabras en MAYÚSCULAS para buscar su significado.")
print("Puedes buscar hasta 5 palabras en esta sesión.")


for _ in range(5):
    word = input("Escribe una palabra en MAYÚSCULAS que no entiendas (o 'exit' para salir): ")
    
    if word.lower() == 'exit':
        break
    
    if word in meme_dict:
        print(word + ": " + meme_dict[word])
    else:
        print("Lo siento, esa palabra no está en el diccionario.")

print("¡Gracias por usar nuestra aplicación de diccionario de memes!")
