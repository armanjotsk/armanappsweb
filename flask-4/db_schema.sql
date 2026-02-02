--  Esborrem la base de dades si ja existeix per comenzar de zero
DROP DATABASE IF EXISTS gestor_emails;

-- Creem la base de dades
CREATE DATABASE gestor_emails;
USE gestor_emails;

-- Creem un usuari per a l'aplicació (opcional, però recomanat)
-- Si et da error de permisos, pots fer servir root al codi python
DROP USER IF EXISTS 'flask_user'@'localhost';
CREATE USER 'flask_user'@'localhost' IDENTIFIED BY 'contrasenya_segura';
GRANT ALL PRIVILEGES ON gestor_emails.* TO 'flask_user'@'localhost';
FLUSH PRIVILEGES;

-- Creem la taula
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    mail VARCHAR(100) NOT NULL
);

-- Inserim dades de prova
INSERT INTO usuarios (nombre, mail) VALUES 
('Joan', 'joan@proven.cat'),
('Maria', 'maria@proven.cat'),
('Pere', 'pere@proven.cat');