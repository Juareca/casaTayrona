from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Elnovato_#24'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'alberjuan2411@gmail.com'
app.config['MAIL_PASSWORD'] = 'vhpb uvpm fqde ifxl'  # Ajusta tu contraseña aquí

mail = Mail(app)

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
    reserva_exitosa = None
    
    if request.method == 'POST':
        destino = request.form['destino']
        habitaciones = request.form['habitaciones']
        huespedes = request.form['huespedes']
        precio = request.form['precio']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        cantidad_noches = request.form['cantidad-noches']

        # Envío de correo electrónico usando Flask-Mail
        msg = Message('Reserva desde Casa Tayrona',
                      sender='alberjuan2411@gmail.com',
                      recipients=['alberjuan2411@gmail.com'])  # Cambia al destinatario deseado
        msg.body = f'''Hola,

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
        
        try:
            mail.send(msg)
            reserva_exitosa = True
        except Exception as e:
            print(str(e))  # Imprime el error para depuración
            reserva_exitosa = False

    return render_template('formulario.html', reserva_exitosa=reserva_exitosa)

if __name__ == '__main__':
    app.run(debug=True)
