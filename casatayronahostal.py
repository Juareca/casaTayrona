# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/betania')
def betania():
    return render_template('betania.html')

@app.route('/rodadero')
def rodadero():
    return render_template('rodadero.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    reserva_exitosa = False

    if request.method == 'POST':
        destino = request.form.get('destino')
        habitaciones = request.form.get('habitaciones')
        huespedes = request.form.get('huespedes')
        precio = request.form.get('precio')
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        cantidad_noches = request.form.get('cantidad-noches')

        # Construir el cuerpo del mensaje
        email_body = f'''Hola,

        Se ha recibido una nueva reserva desde el formulario de Casa Tayrona:

        Nombre: {nombre} {apellido}
        Correo electrónico: {email}
        Teléfono: {telefono}
        Cantidad de noches: {cantidad_noches}
        Destino: {destino}
        Habitaciones: {habitaciones}
        Huéspedes: {huespedes}
        Precio: {precio}

        Gracias.'''

        # Aquí podrías realizar otras acciones relacionadas con el formulario, como guardar los datos en una base de datos o enviar notificaciones, etc.

        reserva_exitosa = True  # Simplemente marcamos la reserva como exitosa para este ejemplo

    return render_template('formulario.html', reserva_exitosa=reserva_exitosa)

if __name__ == '__main__':
    app.run(debug=True)
