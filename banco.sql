CREATE DATABASE lad_py;
USE lad_py;

CREATE TABLE eleitores (
    id_eleitor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    titulo_eleitor CHAR(12) NOT NULL UNIQUE,
    cpf_cifrado VARCHAR(120) NOT NULL UNIQUE,
    mesario BOOLEAN NOT NULL DEFAULT FALSE,
    chave_acesso_cifrada VARCHAR(120) NOT NULL,
    ja_votou BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE partidos (
    id_partido INT AUTO_INCREMENT PRIMARY KEY,
    partido VARCHAR(50) NOT NULL,
    sigla VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE candidatos (
    id_candidato INT AUTO_INCREMENT PRIMARY KEY,
    candidato VARCHAR(100) NOT NULL,
    numero_votacao INT NOT NULL UNIQUE,
    id_partido INT NOT NULL,
    FOREIGN KEY (id_partido) REFERENCES partidos(id_partido)
);

CREATE TABLE votos (
    id_voto INT AUTO_INCREMENT PRIMARY KEY,
    id_candidato INT,
    voto_nulo BOOLEAN NOT NULL DEFAULT FALSE,
    protocolo_votacao_cifrado VARCHAR(120) NOT NULL UNIQUE,
    datetime_voto DATETIME NOT NULL,
    FOREIGN KEY (id_candidato) REFERENCES candidatos(id_candidato)
);

-- INSERT INTO partidos (partido, sigla) VALUES ('Partido Alpha', 'PA');
-- INSERT INTO partidos (partido, sigla) VALUES ('Partido Beta', 'PB');

-- INSERT INTO candidatos (candidato, numero_votacao, id_partido) VALUES ('Carlos Silva', 10, 1);
-- INSERT INTO candidatos (candidato, numero_votacao, id_partido) VALUES ('Marina Souza', 20, 2);

-- INSERT INTO eleitores (nome, titulo_eleitor, prefixo_cpf, cpf_cifrado, mesario, chave_acesso_cifrada, ja_votou)
-- VALUES ('Joao Pereira', '123456789012', '1234', 'CPFTESTE001', TRUE, 'CHAVETESTE001', FALSE);