from flask import Flask, render_template #importiamo la classe flask

#inizializza l'app Flask 
app = Flask(__name__)
lista =['casa','moto']
x = 'ciao'

#rotta principale 
@app.route('/') #visitiamo ('/'), la funzione home() viene eseguita
def home():
    return render_template('index.html', paperino = x, lista = lista )

#avvio dell'app Flask 
if __name__ == '__main__':
    app.run(debug = True) #aggiornamenti in tempo reale

