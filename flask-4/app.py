from flask import Flask, render_template, request
import model_db  # Importem el nostre mòdul

app = Flask(__name__)

@app.route("/")
def index():
    # Redirigim directament a getmail o mostrem una home
    return render_template('base.html')

@app.route("/getmail", methods=['GET', 'POST'])
def getmail():
    email_resultat = None
    error = None
    nom_buscat = ""

    if request.method == 'POST':
        nom_buscat = request.form.get('nombre')
        # Cridem a la funció del mòdul separat
        email_resultat = model_db.buscar_usuari(nom_buscat)
        
        if not email_resultat:
            error = "L'usuari no existeix."

    return render_template('getmail.html', 
                           email=email_resultat, 
                           nom=nom_buscat, 
                           error=error)

@app.route("/addmail", methods=['GET', 'POST'])
def addmail():
    missatge_ok = None
    missatge_error = None
    
    if request.method == 'POST':
        nom = request.form.get('nombre')
        mail = request.form.get('email')
        
        if nom and mail:
            # Cridem a la funció del mòdul separat
            exit = model_db.inserir_usuari(nom, mail)
            if exit:
                missatge_ok = f"Usuari {nom} afegit correctament."
            else:
                missatge_error = "Error: Potser l'usuari ja existeix."
        else:
            missatge_error = "Omple tots els camps."

    return render_template('addmail.html', ok=missatge_ok, error=missatge_error)

if __name__ == '__main__':
    app.run(debug=True)