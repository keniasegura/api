from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
	return{"mensaje": "API de Pedidos funcionando", "version": "1.0"}

@app route('/saludo')
def saludo():
	return{"mensaje": "Hola desde la rama de Jacky!", "estado": "exito"}

@app.route('/health')
def health_check():
	return{"status": "healthy", "service": "api_pedidos"}

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
