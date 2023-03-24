import openai
from os import system
from colorama import init, Fore, Back
import time

system("cls")
init()

# Inicializar la biblioteca OpenAI con tu clave de API
openai.api_key = "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"

# Función para enviar la entrada del usuario y recibir la respuesta de GPT-3
def chat(prompt):
    # Configurar los parámetros de la solicitud de completado
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Obtener la respuesta del modelo y devolverla
    message = response.choices[0].text.strip()
    return message

# Iniciar sesión de chat
print("¡Bienvenido a Chat GPT-3! Escribe 'salir' para finalizar.")
while True:
    user_input = input(Fore.WHITE+"\nTú: ")
    if user_input.lower() == "salir":
        break
    elif user_input.lower()=="cls":
        system("cls")
        print(Fore.RED+ "Se limpio el chat")
        time.sleep(1)
        system("cls")
    else:
        response = chat(user_input)
        print(Fore.GREEN + "\nChatGPT-3: " + response)