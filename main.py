from flask import Flask, request, jsonify
import openai

openai.api_key = "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"

palabras = ["pizza", "hamburguesa", "taco", "hot dog", "twitter", "twitch", "of", "onlyfans", "red social"]

app = Flask(__name__)

@app.route("/botopenia/v1/bot", methods=["GET", "POST"])

def responder_pregunta():

    if __name__ == '__main__':
        # Iniciamos un ciclo infinito para recibir y procesar preguntas continuamente
        while True:
            pregunta = request.form['pregunta']

            # Aquí debes incluir la lógica para procesar la pregunta y obtener la respuesta

            preguntas_min = pregunta.lower()
            palabra_encontrada = None
            for palabra in palabras:
                if palabra in preguntas_min:
                    palabra_encontrada = palabra
                    break
            if palabra_encontrada:
                print("no puedo responder esta pregunta.")
            else:
                    completion = openai.Completion.create(engine="text-davinci-003",
                                        prompt= preguntas_min,
                                        max_tokens=2048)
                    
                    respuesta = completion.choices[0].text

            # Devolvemos la respuesta en formato JSON
            return jsonify({ 'Humano': pregunta, 'IA': respuesta,})
            
    print(respuesta)

app.run(debug=True)