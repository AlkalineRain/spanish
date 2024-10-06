from flask import Flask, render_template, request, redirect, url_for, jsonify
import random as r
import json

app = Flask(__name__)

# Load words and incorrect words
words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "of"},
    {"spanish": "que", "english": "that"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to"},
    {"spanish": "en", "english": "in"},
    {"spanish": "un", "english": "a"},
    {"spanish": "ser", "english": "be"},
    {"spanish": "se", "english": "self"},
    {"spanish": "no", "english": "no"},
    {"spanish": "haber", "english": "have"},
    {"spanish": "por", "english": "for"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his"},
    {"spanish": "para", "english": "for"},
    {"spanish": "como", "english": "like"},
    {"spanish": "estar", "english": "be"},
    {"spanish": "tener", "english": "have"},
    {"spanish": "le", "english": "him"},
    {"spanish": "lo", "english": "it"},
    {"spanish": "todo", "english": "all"},
    {"spanish": "pero", "english": "but"},
    {"spanish": "más", "english": "more"},
    {"spanish": "hacer", "english": "do"},
    {"spanish": "o", "english": "or"},
    {"spanish": "poder", "english": "can"},
    {"spanish": "decir", "english": "say"},
    {"spanish": "este", "english": "this"},
    {"spanish": "ir", "english": "go"},
    {"spanish": "otro", "english": "other"},
    {"spanish": "ese", "english": "that"},
    {"spanish": "la", "english": "the"},
    {"spanish": "si", "english": "if"},
    {"spanish": "me", "english": "me"},
    {"spanish": "ya", "english": "already"},
    {"spanish": "ver", "english": "see"},
    {"spanish": "porque", "english": "because"},
    {"spanish": "dar", "english": "give"},
    {"spanish": "cuando", "english": "when"},
    {"spanish": "él", "english": "he"},
    {"spanish": "muy", "english": "very"},
    {"spanish": "sin", "english": "without"},
    {"spanish": "vez", "english": "time"},
    {"spanish": "mucho", "english": "much"},
    {"spanish": "saber", "english": "know"},
    {"spanish": "qué", "english": "what"},
    {"spanish": "sobre", "english": "about"},
    {"spanish": "mi", "english": "my"},
    {"spanish": "alguno", "english": "some"},
    {"spanish": "mismo", "english": "same"},
    {"spanish": "yo", "english": "I"},
    {"spanish": "también", "english": "also"},
    {"spanish": "hasta", "english": "until"},
    {"spanish": "año", "english": "year"},
    {"spanish": "dos", "english": "two"},
    {"spanish": "querer", "english": "want"},
    {"spanish": "entre", "english": "between"},
    {"spanish": "así", "english": "so"},
    {"spanish": "primero", "english": "first"},
    {"spanish": "desde", "english": "from"},
    {"spanish": "grande", "english": "big"},
    {"spanish": "eso", "english": "that"},
    {"spanish": "ni", "english": "neither"},
    {"spanish": "nos", "english": "us"},
    {"spanish": "llegar", "english": "arrive"},
    {"spanish": "pasar", "english": "happen"},
    {"spanish": "tiempo", "english": "time"},
    {"spanish": "ella", "english": "she"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "día", "english": "day"},
    {"spanish": "uno", "english": "one"},
    {"spanish": "bien", "english": "well"},
    {"spanish": "poco", "english": "little"},
    {"spanish": "deber", "english": "must"},
    {"spanish": "entonces", "english": "then"},
    {"spanish": "poner", "english": "put"},
    {"spanish": "cosa", "english": "thing"},
    {"spanish": "tanto", "english": "so much"},
    {"spanish": "hombre", "english": "man"},
    {"spanish": "parecer", "english": "seem"},
    {"spanish": "nuestro", "english": "our"},
    {"spanish": "tan", "english": "so"},
    {"spanish": "donde", "english": "where"},
    {"spanish": "ahora", "english": "now"},
    {"spanish": "parte", "english": "part"},
    {"spanish": "después", "english": "after"},
    {"spanish": "vida", "english": "life"},
    {"spanish": "quedar", "english": "stay"},
    {"spanish": "siempre", "english": "always"},
    {"spanish": "creer", "english": "believe"},
    {"spanish": "hablar", "english": "talk"},
    {"spanish": "llevar", "english": "carry"},
    {"spanish": "dejar", "english": "leave"},
    {"spanish": "nada", "english": "nothing"},
    {"spanish": "cada", "english": "each"},
    {"spanish": "seguir", "english": "follow"},
    {"spanish": "menos", "english": "less"},
    {"spanish": "nuevo", "english": "new"},
    {"spanish": "encontrar", "english": "find"},
    {"spanish": "algo", "english": "something"},
    {"spanish": "solo", "english": "only"},
    {"spanish": "pues", "english": "then"},
    {"spanish": "llamar", "english": "call"},
    {"spanish": "venir", "english": "come"},
    {"spanish": "pensar", "english": "think"},
    {"spanish": "salir", "english": "leave"},
    {"spanish": "volver", "english": "return"},
    {"spanish": "tomar", "english": "take"},
    {"spanish": "conocer", "english": "know"},
    {"spanish": "vivir", "english": "live"},
    {"spanish": "sentir", "english": "feel"},
    {"spanish": "tratar", "english": "try"},
    {"spanish": "mirar", "english": "look"},
    {"spanish": "contar", "english": "tell"},
    {"spanish": "empezar", "english": "start"},
    {"spanish": "esperar", "english": "wait"},
    {"spanish": "buscar", "english": "search"},
    {"spanish": "existir", "english": "exist"},
    {"spanish": "entrar", "english": "enter"},
    {"spanish": "trabajar", "english": "work"},
    {"spanish": "escribir", "english": "write"},
    {"spanish": "perder", "english": "lose"},
    {"spanish": "producir", "english": "produce"},
    {"spanish": "ocurrir", "english": "happen"},
    {"spanish": "entender", "english": "understand"},
    {"spanish": "pedir", "english": "ask"},
    {"spanish": "recibir", "english": "receive"},
    {"spanish": "recordar", "english": "remember"},
    {"spanish": "terminar", "english": "finish"},
    {"spanish": "permitir", "english": "allow"},
    {"spanish": "aparecer", "english": "appear"},
    {"spanish": "conseguir", "english": "get"},
    {"spanish": "comenzar", "english": "begin"},
    {"spanish": "servir", "english": "serve"},
    {"spanish": "sacar", "english": "take out"},
    {"spanish": "necesitar", "english": "need"},
    {"spanish": "mantener", "english": "maintain"},
    {"spanish": "resultar", "english": "result"},
    {"spanish": "leer", "english": "read"},
    {"spanish": "caer", "english": "fall"},
    {"spanish": "cambiar", "english": "change"},
    {"spanish": "presentar", "english": "present"},
    {"spanish": "crear", "english": "create"},
    {"spanish": "abrir", "english": "open"},
    {"spanish": "considerar", "english": "consider"},
    {"spanish": "oír", "english": "hear"},
    {"spanish": "acabar", "english": "finish"},
    {"spanish": "convertir", "english": "convert"},
    {"spanish": "ganar", "english": "win"},
    {"spanish": "formar", "english": "form"},
    {"spanish": "traer", "english": "bring"},
    {"spanish": "partir", "english": "divide"},
    {"spanish": "morir", "english": "die"},
    {"spanish": "aceptar", "english": "accept"},
    {"spanish": "realizar", "english": "perform"},
    {"spanish": "suponer", "english": "suppose"},
    {"spanish": "comprender", "english": "understand"},
    {"spanish": "lograr", "english": "achieve"},
    {"spanish": "explicar", "english": "explain"},
    {"spanish": "preguntar", "english": "ask"},
    {"spanish": "tocar", "english": "touch"},
    {"spanish": "reconocer", "english": "recognize"},
    {"spanish": "estudiar", "english": "study"},
    {"spanish": "alcanzar", "english": "reach"},
    {"spanish": "nacer", "english": "be born"},
    {"spanish": "dirigir", "english": "direct"},
    {"spanish": "correr", "english": "run"},
    {"spanish": "utilizar", "english": "use"},
    {"spanish": "pagar", "english": "pay"},
    {"spanish": "ayudar", "english": "help"},
    {"spanish": "gustar", "english": "like"},
    {"spanish": "jugar", "english": "play"},
    {"spanish": "escuchar", "english": "listen"},
    {"spanish": "cumplir", "english": "fulfill"},
    {"spanish": "ofrecer", "english": "offer"},
    {"spanish": "descubrir", "english": "discover"},
    {"spanish": "levantar", "english": "lift"},
    {"spanish": "intentar", "english": "try"},
    {"spanish": "usar", "english": "use"},
    {"spanish": "decidir", "english": "decide"},
    {"spanish": "repetir", "english": "repeat"},
    {"spanish": "aprender", "english": "learn"},
    {"spanish": "comer", "english": "eat"},
    {"spanish": "desarrollar", "english": "develop"},
    {"spanish": "morir", "english": "die"},
    {"spanish": "olvidar", "english": "forget"},
    {"spanish": "comprar", "english": "buy"},
    {"spanish": "beber", "english": "drink"}
]

def load_incorrect_words():
    try:
        with open('incorrect_words.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_incorrect_words(incorrect_words):
    with open('incorrect_words.json', 'w') as file:
        json.dump(incorrect_words, file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn', methods=['GET', 'POST'])
def learn():
    incorrect_words = load_incorrect_words()
    if request.method == 'POST':
        user_input = request.form.get('translation')
        spanish_word = request.form.get('spanish_word')
        correct_word = next((word['english'] for word in words if word['spanish'] == spanish_word), None)

        if user_input == correct_word:
            result = "Correct!"
        else:
            result = f"Incorrect! The correct translation is {correct_word}"
            incorrect_words.append({"spanish": spanish_word, "english": correct_word})
            save_incorrect_words(incorrect_words)

        return render_template('learn.html', result=result, spanish_word=spanish_word)

    # Shuffle words for learning
    r.shuffle(words)
    current_word = words[0]  # Get the first word for the quiz
    return render_template('learn.html', spanish_word=current_word['spanish'])

@app.route('/incorrect')
def incorrect():
    incorrect_words = load_incorrect_words()
    return render_template('incorrect.html', incorrect_words=incorrect_words)

if __name__ == "__main__":
    app.run()