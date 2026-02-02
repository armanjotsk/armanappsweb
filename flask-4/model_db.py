import mysql.connector

# Configuració de la connexió
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="flask_user",       # O 'root' si no has creat l'usuari
        password="contrasenya_segura", # O '' si és root a XAMPP
        database="gestor_emails"
    )

def buscar_usuari(nom):
    """Retorna l'email o None si no existeix"""
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "SELECT mail FROM usuarios WHERE nombre = %s"
    cursor.execute(sql, (nom,))
    resultat = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if resultat:
        return resultat[0] # Retorna només l'string del mail
    return None

def inserir_usuari(nom, mail):
    """Retorna True si s'ha inserit, False si hi ha error"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        sql = "INSERT INTO usuarios (nombre, mail) VALUES (%s, %s)"
        cursor.execute(sql, (nom, mail))
        conn.commit()
        
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Error BD: {e}")
        return False