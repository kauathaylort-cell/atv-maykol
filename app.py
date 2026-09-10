from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# --- PASSO 1-c: Rota para o Favicon ---
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# --- PASSO 2-a: Rota Raiz '/' ---
@app.route('/')
def index():
    return render_template('index.html')

# --- PASSO 2-a: Rota '/calculadora' ---
@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

# --- PASSO 2-a: Rota '/resultado' ---
@app.route('/resultado', methods=['POST'])
def resultado():
    # PASSO 2-c: Lógica do cálculo em Python
    try:
        num1 = float(request.form.get('num1', 0))
        num2 = float(request.form.get('num2', 0))
        operacao = request.form.get('operacao')
        
        if operacao == 'soma':
            res = num1 + num2
        elif operacao == 'subtracao':
            res = num1 - num2
        elif operacao == 'multiplicacao':
            res = num1 * num2
        elif operacao == 'divisao':
            res = num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
        else:
            res = "Operação inválida"
    except ValueError:
        res = "Por favor, insira números válidos."

    return render_template('resultado.html', resultado=res)

if __name__ == '__main__':
    app.run(debug=True)
