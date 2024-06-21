from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

# Configuración de SES (reemplaza con tus propias credenciales)
smtp_username = "AKIA2UC27IZCBIS5ER7G"
smtp_password = "BNXVglCvJkFqftPcEmKqENsg7eMxd1Lub3uWHbdp/QsL"
smtp_server = "email-smtp.sa-east-1.amazonaws.com"
smtp_port = 587
smtp_verified_email = "alberjuan2411@gmail.com"
smtp_verified_casatayrona = "casatayrona17@gmail.com"

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
        email_body = f'''

        Se ha recibido una nueva reserva desde el formulario de Casa Tayrona:

        Nombre: {nombre} {apellido}
        Correo electrónico: {email}
        Teléfono: {telefono}
        Cantidad de noches: {cantidad_noches}
        Destino: {destino}
        Habitaciones: {habitaciones}
        Huéspedes: {huespedes}
        Precio: {precio}

        '''

        # Enviar correo usando SES
        try:
            msg = MIMEMultipart()
            msg['From'] = smtp_verified_email
            msg['To'] = smtp_verified_casatayrona
            msg['Subject'] = f'''{nombre} {apellido}'''" ha reservado desde casatayrona.com"

            msg.attach(MIMEText(email_body, 'plain'))

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()  # Iniciar TLS para encriptar la conexión
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_verified_email, smtp_verified_casatayrona, msg.as_string())
            server.quit()

            reserva_exitosa = True

        except Exception as e:
            print(f"Error al enviar el correo: {str(e)}")
            reserva_exitosa = False

    return render_template('formulario.html', reserva_exitosa=reserva_exitosa)

if __name__ == '__main__':
    app.run(debug=True)
