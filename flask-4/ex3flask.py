# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def inici():
#     return "hello world y adios"

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/my/secret/page")
def secret_page():
    return "Top secret!"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"Q'hubo: {username}"

@app.route("/blog/post/<int:post_id>")
def show_post(post_id):
    return f"This is the page for post # {post_id}"

@app.route("/paryimpar/<int:numero>")
def par_impar(numero):
    if numero % 2 == 0:
        return f"{numero} es par."
    else:
        return f"{numero} es impar."
    
@app.route('/hello/')
@app.route('/hello/<name>')
def hello_word(name=None):
    return render_template('index.html', name=name)

@app.route("/edad100/<nombre>/<int:edad>")
def edad_100(nombre, edad): 
    return f"Holaaa {nombre} tendras 100 años en el año {2026 + (100 - edad)}"

@app.route('/formulario-edad', methods=['GET', 'POST'])
def formulario_edad():
    resultado = None
    
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')
        
        if nombre and edad:
            anio_100 = 2026 + (100 - int(edad))
            resultado = f"Hola {nombre}, tendrás 100 años en el año {anio_100}"

    return render_template('formulario_edad.html', resultado=resultado)


import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # Usuario por defecto de XAMPP
        password="",        # Contraseña por defecto (vacía)
        database="nom_mail" # Nombre de tu base de datos en la imagen
    )

@app.route("/addmail", methods=['GET', 'POST'])
def registro_usuario():
    mensaje = None
    
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('email')
        
        # Insertar en la base de datos
        db = conectar_db()
        cursor = db.cursor()
        
        sql = "INSERT INTO usuarios (Nombre, Mail) VALUES (%s, %s)"
        valores = (nombre, correo)
        
        cursor.execute(sql, valores)
        db.commit() # Importante para guardar los cambios
        
        cursor.close()
        db.close()
        
        return f"<h3>Usuario {nombre} registrado correctamente en la base de datos.</h3>"
    
    return render_template('addmail.html', mensaje=mensaje)




@app.route("/getmail", methods=['GET', 'POST'])
def buscar_email():
    if request.method == 'POST':
        nombre_buscado = request.form.get('usuario')
        
        db = conectar_db()
        cursor = db.cursor()
        
        # Usamos una consulta SQL para buscar el mail por nombre
        sql = "SELECT Mail FROM usuarios WHERE Nombre = %s"
        cursor.execute(sql, (nombre_buscado,))
        
        resultado = cursor.fetchone()
        
        cursor.close()
        db.close()
        
        if resultado:
            return f"<h3>El correo de {nombre_buscado} es: {resultado[0]}</h3><br><a href='/getmail'>Volver a buscar</a>"
        else:
            return f"<h3>No se encontró ningún usuario con el nombre '{nombre_buscado}'.</h3><br><a href='/getmail'>Reintentar</a>"
    
    # Si es GET, cargamos el formulario de búsqueda
    return render_template('getmail.html')