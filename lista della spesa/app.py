from flask import Flask, render_template, request, redirect, url_for #importiamo la classe flask

#inizializza l'app Flask 
app = Flask(__name__)
lista_spesa =['casa','moto']
x = 'ciao'

#rotta principale 
@app.route('/') #visitiamo ('/'), la funzione home() viene eseguita
def home():
    return render_template('index.html', paperino = x, lista = lista_spesa )

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    #ottiene elemento dal form
    elemento = request.form['elemento']
    #aggiunge alla lista 
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice)
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota():
    lista_spesa.clear()
    return redirect(url_for('home'))

#avvio dell'app Flask 
if __name__ == '__main__':
    app.run(debug = True) #aggiornamenti in tempo reale

