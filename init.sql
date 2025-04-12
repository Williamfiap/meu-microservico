CREATE DATABASE microssistema;
USE microssistema;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO usuarios (nome, email) VALUES 
    ('Usuário Teste', 'teste@exemplo.com'),
    ('Admin Sistema', 'admin@exemplo.com');