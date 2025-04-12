# Meu Microsserviço

Este projeto é um microsserviço desenvolvido em Python utilizando Flask. Ele se conecta a um banco de dados MySQL e expõe endpoints para verificar o status do serviço e listar usuários. O objetivo é demonstrar a integração entre um serviço web e um banco de dados relacional utilizando contêineres Docker.

## Estrutura do Projeto

- **app.py**: Código principal do microsserviço, implementado com Flask. Ele expõe endpoints para verificar o status do serviço e listar usuários do banco de dados.
- **Dockerfile**: Define a imagem Docker para o microsserviço, incluindo a instalação de dependências e configuração do ambiente.
- **init.sql**: Script SQL para inicializar o banco de dados `microssistema` e criar a tabela `usuarios` com dados de exemplo.
- **requirements.txt**: Lista as dependências Python necessárias para o projeto, como Flask e Gunicorn.
- **README.md**: Documentação do projeto, incluindo instruções de uso, descrição dos arquivos, comandos executados e como testar o microsserviço.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- [Docker](https://www.docker.com/): Para criar e gerenciar contêineres.
- [cURL](https://curl.se/): Para testar os endpoints do microsserviço.

## Comandos Executados

Aqui estão os comandos executados no terminal durante o desenvolvimento e configuração do projeto, juntamente com suas descrições e resultados:

1. **Comando:**
   ```bash
   docker build -t meu-microservico .
   ```
   **Descrição:**
   Cria a imagem Docker para o microsserviço utilizando o `Dockerfile` presente no diretório atual.
   **Resultado:**
   Imagem criada com sucesso e nomeada como `meu-microservico`.

2. **Comando:**
   ```bash
   docker run -d --name container-microservico -p 5000:5000 meu-microservico
   ```
   **Descrição:**
   Inicia um container Docker para o microsserviço, mapeando a porta 5000 do container para a porta 5000 do host.
   **Resultado:**
   Container iniciado com sucesso.

3. **Comando:**
   ```bash
   docker exec -it container-microservico bash
   ```
   **Descrição:**
   Acessa o terminal interativo do container `container-microservico` para realizar operações internas.
   **Resultado:**
   Terminal do container acessado com sucesso.

4. **Comando:**
   ```bash
   docker stats container-microservico
   ```
   **Descrição:**
   Exibe as estatísticas de uso de recursos (CPU, memória, etc.) do container `container-microservico`.
   **Resultado:**
   Estatísticas exibidas com sucesso.

5. **Comando:**
   ```bash
   docker pause container-microservico
   ```
   **Descrição:**
   Pausa a execução do container `container-microservico`.
   **Resultado:**
   Container pausado com sucesso.

6. **Comando:**
   ```bash
   docker unpause container-microservico
   ```
   **Descrição:**
   Retoma a execução do container `container-microservico` que foi pausado.
   **Resultado:**
   Container retomado com sucesso.

7. **Comando:**
   ```bash
   docker volume create dados-mysql
   ```
   **Descrição:**
   Cria um volume Docker chamado `dados-mysql` para persistir os dados do banco de dados MySQL.
   **Resultado:**
   Volume criado com sucesso.

8. **Comando:**
   ```bash
   docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=senha123 -v dados-mysql:/var/lib/mysql -v ./init.sql:/docker-entrypoint-initdb.d/init.sql -p 3306:3306 mysql:8.0
   ```
   **Descrição:**
   Inicia um container MySQL com a senha do root definida como `senha123`, utilizando o volume `dados-mysql` para persistência e o script `init.sql` para inicialização do banco de dados.
   **Resultado:**
   Container MySQL iniciado com sucesso.

9. **Comando:**
   ```bash
   docker network create minha-rede
   ```
   **Descrição:**
   Cria uma rede Docker chamada `minha-rede` para conectar os contêineres.
   **Resultado:**
   Rede criada com sucesso.

10. **Comando:**
    ```bash
    docker network connect minha-rede mysql-container
    ```
    **Descrição:**
    Conecta o container `mysql-container` à rede `minha-rede`.
    **Resultado:**
    Container conectado à rede com sucesso.

11. **Comando:**
    ```bash
    docker run -d --name container-microservico --network minha-rede -p 5000:5000 meu-microservico
    ```
    **Descrição:**
    Inicia o container do microsserviço conectado à rede `minha-rede`, mapeando a porta 5000 para o host.
    **Resultado:**
    Container iniciado com sucesso.

12. **Comando:**
    ```bash
    docker exec -it mysql-container mysql -uroot -psenha123 -e "SELECT * FROM microssistema.usuarios;"
    ```
    **Descrição:**
    Executa o cliente MySQL dentro do container `mysql-container` para listar todos os registros da tabela `usuarios` no banco de dados `microssistema`.
    **Resultado:**
    ```
    +----+----------------+-------------------+---------------------+
    | id | nome           | email             | data_criacao        |
    +----+----------------+-------------------+---------------------+
    |  1 | Usuário Teste  | teste@exemplo.com | 2025-04-12 09:45:27 |
    |  2 | Admin Sistema  | admin@exemplo.com | 2025-04-12 09:45:27 |
    +----+----------------+-------------------+---------------------+
    ```

## Como Executar o Projeto

1. Certifique-se de ter o Docker instalado em sua máquina.
2. Construa a imagem Docker:
   ```bash
   docker build -t meu-microservico .
   ```
3. Inicie o container MySQL:
   ```bash
   docker run -d --name mysql-container -e MYSQL_ROOT_PASSWORD=senha123 -e MYSQL_DATABASE=microssistema -v dados-mysql:/var/lib/mysql -p 3306:3306 mysql:8.0
   ```
4. Conecte o container MySQL à rede:
   ```bash
   docker network create minha-rede
   docker network connect minha-rede mysql-container
   ```
5. Inicie o container do microsserviço:
   ```bash
   docker run -d --name container-microservico --network minha-rede -p 5000:5000 meu-microservico
   ```
6. Acesse o microsserviço em `http://localhost:5000`.

## Como Testar o Microsserviço

1. Certifique-se de que o container do microsserviço está em execução:
   ```bash
   docker ps
   ```

2. Teste o endpoint `/status` para verificar o status do microsserviço:
   ```bash
   curl http://localhost:5000/status
   ```
   **Resultado esperado:**
   ```json
   {
     "message": "O microsserviço está funcionando corretamente!",
     "status": "online"
   }
   ```

3. Teste o endpoint `/usuarios` para listar os usuários do banco de dados:
   ```bash
   curl http://localhost:5000/usuarios
   ```
   **Resultado esperado no navegador:**
   ```json
   [
     {
       "data_criacao": "Sat, 12 Apr 2025 09:45:27 GMT",
       "email": "teste@exemplo.com",
       "id": 1,
       "nome": "Usuário Teste"
     },
     {
       "data_criacao": "Sat, 12 Apr 2025 09:45:27 GMT",
       "email": "admin@exemplo.com",
       "id": 2,
       "nome": "Admin Sistema"
     }
   ]
   ```

## Endpoints Disponíveis

- **GET /status**: Retorna o status do microsserviço.
- **GET /usuarios**: Retorna a lista de usuários do banco de dados.

## Observações Finais

- Certifique-se de que as portas 5000 e 3306 não estão sendo usadas por outros serviços antes de iniciar os contêineres. no meu caso estou usando a 3307.
- Caso encontre problemas, verifique os logs dos contêineres utilizando o comando:
  ```bash
  docker logs <container-microservico>
  ```