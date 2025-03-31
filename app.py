from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo (sustituye con información real)
caso_uso = {
    "titulo": "Predicción de Fraude en Transacciones Bancarias",
    "descripcion": "Los bancos utilizan Machine Learning Supervisado para detectar transacciones fraudulentas en tiempo real.",
    "algoritmo": "Random Forest",
    "beneficios": [
        "Reducción de fraudes",
        "Mayor seguridad en transacciones",
        "Mejor experiencia para el usuario"
    ],
    "ejemplo_empresa": "Visa y Mastercard han implementado modelos de ML para detección de fraudes."
}

@app.route("/")
def home():
    return render_template("index.html", caso=caso_uso)

@app.route('/calculategrades/', methods=["GET", "POST"])
def calculategrades():
    def generate_plot():
        result = None
        img_data = generate_plot()
        
        if request.method == 'POST':
            hours = float(request.form['hours'])
            prediction = model.predict([[hours]])[0]
            result = round(prediction, 2)
        
        return render_template('calculategrades.html', result=result, img_data=img_data)

if __name__ == "__main__":
    app.run(debug=True)
